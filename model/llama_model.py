import requests
from config import TOGETHER_AI_API_KEY, TOGETHER_AI_API_URL
from schema_info import get_schema_info

class LlamaModel:
    def __init__(self, api_key=TOGETHER_AI_API_KEY, api_url=TOGETHER_AI_API_URL, database='sample.db'):
        self.api_key = api_key
        self.api_url = api_url
        self.schema_info = get_schema_info(database)

    def query(self, question):
        prompt = self.construct_prompt(question)
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'model': 'meta-llama/Llama-3-70b-hf',
            'prompt': prompt,
            'max_tokens': 200
        }
        response = requests.post(self.api_url, json=data, headers=headers)
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err} - {response.text}"
        except Exception as err:
            return f"Other error occurred: {err}"

        response_json = response.json()
        # Extract SQL query from the 'choices' field
        try:
            text = response_json['choices'][0]['text'].strip()
            sql_query = self.extract_sql_query(text)
            return sql_query
        except KeyError as e:
            return f"Unexpected response format: {response_json}"

    def construct_prompt(self, question):
        # Create the schema information string
        schema_str = "Database schema:\n"
        for table, columns in self.schema_info.items():
            schema_str += f"Table {table}:\n"
            for col_name, col_type in columns:
                schema_str += f"  - {col_name} ({col_type})\n"
        
        # Define the prompt template with schema information and instructions
        prompt_template = f"""
        You are an expert SQL query generator. Convert the following natural language question into an SQL query. Use the provided database schema information to construct the query.

        {schema_str}

        Question: {question}

        SQL Query:
        """
        return prompt_template

    def extract_sql_query(self, text):
        """Extract the SQL query from the response text."""
        # Strip any leading or trailing characters and ensure it starts with 'SELECT', 'INSERT', 'UPDATE', etc.
        text = text.strip()
        if text.lower().startswith(("select", "insert", "update", "delete")):
            return text
        return "Error: The response does not contain a valid SQL query."
