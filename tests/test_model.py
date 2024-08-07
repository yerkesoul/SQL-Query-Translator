import unittest
from model.llama_model import LlamaModel

class LlamaModelTestCase(unittest.TestCase):
    def setUp(self):
        self.model = LlamaModel()

    def test_query(self):
        result = self.model.query('Show me all orders from last month')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
