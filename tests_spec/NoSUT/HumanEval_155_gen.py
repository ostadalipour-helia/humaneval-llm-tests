import unittest
from sut.problem_HumanEval_155 import even_odd_count

class Test_even_odd_count(unittest.TestCase):
    def test_normal_mixed_positive_123(self):
        # Description: Mixed even and odd digits in a positive number.
        num = 123
        expected_output = (1, 2)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_normal_mixed_positive_45678(self):
        # Description: Another positive number with mixed digits.
        num = 45678
        expected_output = (3, 2)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_normal_contains_zero_100(self):
        # Description: Number containing zero digits.
        num = 100
        expected_output = (2, 1)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_negative_number(self):
        # Description: Negative number with mixed digits.
        num = -12
        expected_output = (1, 1)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_zero_input(self):
        # Description: Input is zero (0 is an even digit).
        num = 0
        expected_output = (1, 0)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_single_odd_digit(self):
        # Description: Single odd digit number.
        num = 5
        expected_output = (0, 1)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_all_even_digits(self):
        # Description: All even digits.
        num = 246
        expected_output = (3, 0)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_all_odd_digits(self):
        # Description: All odd digits.
        num = 135
        expected_output = (0, 3)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_edge_large_negative_number(self):
        # Description: Large negative number with mixed digits.
        num = -987654321
        expected_output = (4, 5)
        self.assertEqual(even_odd_count(num), expected_output)

    def test_error_string_input(self):
        # Description: Input is a string instead of an integer.
        num = "123"
        with self.assertRaises(TypeError):
            even_odd_count(num)

    def test_error_float_input(self):
        # Description: Input is a float instead of an integer.
        num = 12.5
        with self.assertRaises(TypeError):
            even_odd_count(num)

    def test_error_list_input(self):
        # Description: Input is a list instead of an integer.
        num = [1, 2, 3]
        with self.assertRaises(TypeError):
            even_odd_count(num)