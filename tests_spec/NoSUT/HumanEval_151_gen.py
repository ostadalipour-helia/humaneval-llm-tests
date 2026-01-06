import unittest
from sut.problem_HumanEval_151 import double_the_difference

class Test_double_the_difference(unittest.TestCase):
    def test_normal_case_positive_odd_and_even(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_normal_case_positive_odd_and_negative(self):
        self.assertEqual(double_the_difference([9, -2]), 81)

    def test_normal_case_multiple_positive_odd(self):
        self.assertEqual(double_the_difference([5, 7, 10, 11]), 195)

    def test_edge_case_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_edge_case_only_negative_and_zero(self):
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_edge_case_only_even_numbers(self):
        self.assertEqual(double_the_difference([2, 4, 6]), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(double_the_difference([0]), 0)

    def test_edge_case_single_positive_odd_number(self):
        self.assertEqual(double_the_difference([7]), 49)

    def test_edge_case_mixed_types_and_valid_numbers(self):
        self.assertEqual(double_the_difference([1.5, 3, 'a', 5, -3.0]), 34)

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            double_the_difference(None)

    def test_error_case_integer_input(self):
        with self.assertRaises(TypeError):
            double_the_difference(123)

    def test_error_case_string_input(self):
        with self.assertRaises(TypeError):
            double_the_difference("hello")