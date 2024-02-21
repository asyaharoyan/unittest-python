import unittest
from even import even_numbers_of_even

class TestEvens(unittest.TestCase):
    
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_numbers_of_even, 4)

    def test_values_in_list(self):
        self.assertEqual(even_numbers_of_even([]), False)
        self.assertEqual(even_numbers_of_even([2, 4]), True)
        self.assertEqual(even_numbers_of_even([2]), False)
        self.assertEqual(even_numbers_of_even([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()