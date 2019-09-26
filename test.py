import unittest
from main import sum_of_list
class TestSum(unittest.TestCase):
    def test_sum_of_integers(self):
        data = [1, 2, 3, 4] # Arrange
        result = sum_of_list(data) # Act
        self.assertEqual(result, 10)
    def test_sum_of_floats(self):
        data = [0.1, 0.5, 0.3]
        result = sum_of_list(data)
        result = round(result, 1)
        self.assertEqual(result, 0.9)
    def test_string_input(self):
        s = 'this is string'
        with self.assertRaises(TypeError):
            sum_of_list(s)