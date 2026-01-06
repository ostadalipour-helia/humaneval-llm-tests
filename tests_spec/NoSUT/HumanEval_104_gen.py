import unittest
from sut.problem_HumanEval_104 import unique_digits

class Test_unique_digits(unittest.TestCase):

    def test_normal_case_basic(self):
        # Normal case with a mix of qualifying and non-qualifying numbers
        x = [15, 33, 1422, 1]
        expected_output = [1, 15, 33]
        self.assertEqual(unique_digits(x), expected_output)

    def test_normal_case_no_matches(self):
        # Normal case where no numbers qualify
        x = [152, 323, 1422, 10]
        expected_output = []
        self.assertEqual(unique_digits(x), expected_output)

    def test_normal_case_all_matches(self):
        # Normal case where all numbers qualify
        x = [1, 3, 5, 7, 9]
        expected_output = [1, 3, 5, 7, 9]
        self.assertEqual(unique_digits(x), expected_output)

    def test_edge_case_empty_list(self):
        # Edge case: empty input list
        x = []
        expected_output = []
        self.assertEqual(unique_digits(x), expected_output)

    def test_edge_case_duplicates(self):
        # Edge case: input list contains duplicate qualifying numbers
        x = [15, 1, 33, 15]
        expected_output = [1, 15, 15, 33]
        self.assertEqual(unique_digits(x), expected_output)

    def test_error_input_not_list(self):
        # Error case: input `x` is not a list (e.g., None)
        with self.assertRaises(TypeError):
            unique_digits(None)

    def test_error_list_contains_float(self):
        # Error case: list `x` contains non-integer elements (float)
        with self.assertRaises(TypeError):
            unique_digits([1, 2.5, 3])

    def test_error_list_contains_negative(self):
        # Error case: list `x` contains non-positive integers (negative)
        with self.assertRaises(ValueError):
            unique_digits([1, -5, 3])

    def test_error_list_contains_zero(self):
        # Error case: list `x` contains non-positive integers (zero)
        with self.assertRaises(ValueError):
            unique_digits([1, 0, 3])