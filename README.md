# NLP to SQL Translator

This project demonstrates a system that uses the Llama 3 70B model to translate natural language questions about business data into SQL queries.

## Project Structure

- `app.py`: The main Flask application.
- `model/llama_model.py`: The LlamaModel class that interacts with the Together.ai API.
- `templates/index.html`: A simple front-end for testing the translator.
- `tests/`: Unit tests for the API and model.
- `requirements.txt`: Python dependencies.
- `config.py`: Configuration file for the Together.ai API.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```
5. Open `http://127.0.0.1:5000` in your browser to see the demo.

## Testing

Run the unit tests:
```bash
python -m unittest discover tests
