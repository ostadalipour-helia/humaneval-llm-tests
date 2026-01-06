import unittest
from sut.problem_HumanEval_146 import specialFilter

class Test_specialFilter(unittest.TestCase):
    def test_normal_example_one(self):
        # Example from docstring: 15 matches (15 > 10, first digit 1 odd, last digit 5 odd).
        # Other numbers do not meet the criteria.
        nums = [15, -73, 14, -15]
        expected_output = 1
        self.assertEqual(specialFilter(nums), expected_output)

    def test_normal_example_two(self):
        # Example from docstring: 33 matches (33 > 10, first digit 3 odd, last digit 3 odd).
        # 109 matches (109 > 10, first digit 1 odd, last digit 9 odd).
        # Other numbers do not meet the criteria.
        nums = [33, -2, -3, 45, 21, 109]
        expected_output = 2
        self.assertEqual(specialFilter(nums), expected_output)

    def test_normal_all_match(self):
        # All numbers in the list are greater than 10 and have both first and last digits odd.
        nums = [11, 13, 15, 17, 19]
        expected_output = 5
        self.assertEqual(specialFilter(nums), expected_output)

    def test_normal_large_numbers(self):
        # Large numbers where both first and last digits are odd and are greater than 10.
        nums = [123456789, 987654321]
        expected_output = 2
        self.assertEqual(specialFilter(nums), expected_output)

    def test_edge_empty_list(self):
        # An empty list should result in 0 matching elements.
        nums = []
        expected_output = 0
        self.assertEqual(specialFilter(nums), expected_output)

    def test_edge_no_matches(self):
        # List with no matching elements (either not greater than 10 or digits are not both odd).
        nums = [10, 20, 30, 40, 1, 9, 0, -100]
        expected_output = 0
        self.assertEqual(specialFilter(nums), expected_output)

    def test_edge_greater_than_10_but_digits_not_odd(self):
        # Numbers greater than 10 but with at least one even digit (first or last).
        nums = [12, 14, 16, 21, 43, 65]
        expected_output = 0
        self.assertEqual(specialFilter(nums), expected_output)

    def test_edge_middle_digits_can_be_even_or_zero(self):
        # Numbers with first and last digits odd, but middle digits can be even/zero.
        nums = [101, 103, 105, 107, 109]
        expected_output = 5
        self.assertEqual(specialFilter(nums), expected_output)

    def test_error_input_not_a_list(self):
        # Raise a TypeError because the input is not a list.
        nums = "not_a_list"
        with self.assertRaises(TypeError):
            specialFilter(nums)

    def test_error_list_contains_non_integer_string(self):
        # Raise a TypeError because the list contains non-integer elements.
        nums = [1, 2, "three", 4]
        with self.assertRaises(TypeError):
            specialFilter(nums)

    def test_error_list_contains_non_integer_none(self):
        # Raise a TypeError because the list contains non-integer elements (null in JSON is None in Python).
        nums = [1, 2, None, 4]
        with self.assertRaises(TypeError):
            specialFilter(nums)