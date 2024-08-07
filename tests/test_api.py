import unittest
from app import app, execute_sql_query

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Welcome to the NLP to SQL Translator!')

    def test_translate(self):
        response = self.app.post('/translate', json={'question': 'Show me all orders'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('sql_query', response.json)
        self.assertIn('result', response.json)

    def test_execute_sql_query(self):
        query = 'SELECT * FROM orders'
        result = execute_sql_query(query)
        self.assertIn('columns', result)
        self.assertIn('rows', result)
        self.assertGreater(len(result['rows']), 0)

if __name__ == '__main__':
    unittest.main()
