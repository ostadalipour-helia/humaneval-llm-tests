import unittest
from sut.problem_HumanEval_138 import is_equal_to_sum_even

class Test_is_equal_to_sum_even(unittest.TestCase):
    def test_normal_eight(self):
        # n = 8, output = True, reasoning: 8 is an even number and 8 >= 8. It can be written as 2 + 2 + 2 + 2.
        self.assertTrue(is_equal_to_sum_even(8))

    def test_normal_ten(self):
        # n = 10, output = True, reasoning: 10 is an even number and 10 >= 8. It can be written as 2 + 2 + 2 + 4.
        self.assertTrue(is_equal_to_sum_even(10))

    def test_normal_twelve(self):
        # n = 12, output = True, reasoning: 12 is an even number and 12 >= 8. It can be written as 2 + 2 + 4 + 4.
        self.assertTrue(is_equal_to_sum_even(12))

    def test_edge_four(self):
        # n = 4, output = False, reasoning: 4 is an even number but 4 < 8. The minimum sum of 4 positive even numbers is 8.
        self.assertFalse(is_equal_to_sum_even(4))

    def test_edge_six(self):
        # n = 6, output = False, reasoning: 6 is an even number but 6 < 8. The minimum sum of 4 positive even numbers is 8.
        self.assertFalse(is_equal_to_sum_even(6))

    def test_edge_seven(self):
        # n = 7, output = False, reasoning: 7 is an odd number. The sum of 4 even numbers must always be even.
        self.assertFalse(is_equal_to_sum_even(7))

    def test_edge_nine(self):
        # n = 9, output = False, reasoning: 9 is an odd number. The sum of 4 even numbers must always be even.
        self.assertFalse(is_equal_to_sum_even(9))

    def test_edge_zero(self):
        # n = 0, output = False, reasoning: 0 is an even number but 0 < 8. Also, positive even numbers cannot sum to zero.
        self.assertFalse(is_equal_to_sum_even(0))

    def test_edge_negative_two(self):
        # n = -2, output = False, reasoning: -2 is a negative number. Positive even numbers cannot sum to a negative number.
        self.assertFalse(is_equal_to_sum_even(-2))

    def test_error_float_input(self):
        # n = 8.5, exception = TypeError, reasoning: The input `n` must be an integer, not a float.
        with self.assertRaises(TypeError):
            is_equal_to_sum_even(8.5)

    def test_error_string_input(self):
        # n = 'hello', exception = TypeError, reasoning: The input `n` must be an integer, not a string.
        with self.assertRaises(TypeError):
            is_equal_to_sum_even('hello')

    def test_error_none_input(self):
        # n = None, exception = TypeError, reasoning: The input `n` must be an integer, not None.
        with self.assertRaises(TypeError):
            is_equal_to_sum_even(None)