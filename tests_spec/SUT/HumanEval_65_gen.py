import unittest
from sut.problem_HumanEval_65 import circular_shift

class Test_circular_shift(unittest.TestCase):

    def test_normal_case_single_shift(self):
        self.assertEqual(circular_shift(x=12345, shift=1), '51234')

    def test_normal_case_multiple_shifts(self):
        self.assertEqual(circular_shift(x=12345, shift=3), '34512')

    def test_normal_case_full_cycle(self):
        self.assertEqual(circular_shift(x=123, shift=3), '123')

    def test_edge_case_docstring_1(self):
        self.assertEqual(circular_shift(x=12, shift=1), '21')

    def test_edge_case_docstring_2(self):
        self.assertEqual(circular_shift(x=12, shift=2), '12')

    def test_edge_case_zero_shift(self):
        self.assertEqual(circular_shift(x=123, shift=0), '123')

    def test_edge_case_single_digit(self):
        self.assertEqual(circular_shift(x=5, shift=1), '5')

    def test_edge_case_zero_input(self):
        self.assertEqual(circular_shift(x=0, shift=1), '0')

    def test_edge_case_shift_greater_than_digits_reverse(self):
        self.assertEqual(circular_shift(x=123, shift=4), '321')

    def test_edge_case_shift_much_greater_reverse(self):
        self.assertEqual(circular_shift(x=123, shift=10), '321')