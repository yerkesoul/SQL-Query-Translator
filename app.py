import sqlite3
from flask import Flask, request, jsonify, render_template
from model.llama_model import LlamaModel

app = Flask(__name__)
llama_model = LlamaModel()

DATABASE = 'sample.db'

def execute_sql_query(query):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()
        return {"columns": columns, "rows": result}
    except Exception as e:
        conn.close()
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    try:
        sql_query = llama_model.query(question)
        if sql_query.startswith("Error:"):
            return jsonify({'error': sql_query}), 400
        query_result = execute_sql_query(sql_query)
        return jsonify({'sql_query': sql_query, 'result': query_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
