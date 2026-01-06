import unittest
from sut.problem_HumanEval_53 import add

class Test_add(unittest.TestCase):

    def test_normal_positive_integers_1(self):
        # Adding two positive integers.
        self.assertEqual(add(2, 3), 5)

    def test_normal_positive_integers_2(self):
        # Another example of adding two positive integers.
        self.assertEqual(add(10, 20), 30)

    def test_edge_one_input_zero(self):
        # One input is zero.
        self.assertEqual(add(0, 5), 5)

    def test_edge_both_inputs_zero(self):
        # Both inputs are zero.
        self.assertEqual(add(0, 0), 0)

    def test_edge_negative_and_positive_result_positive(self):
        # Adding a negative and a positive integer, result is positive.
        self.assertEqual(add(-2, 3), 1)

    def test_edge_positive_and_negative_result_negative(self):
        # Adding a positive and a negative integer, result is negative.
        self.assertEqual(add(2, -3), -1)

    def test_edge_two_negative_integers(self):
        # Adding two negative integers.
        self.assertEqual(add(-5, -7), -12)

    def test_edge_additive_inverse(self):
        # Adding a number and its additive inverse.
        self.assertEqual(add(5, -5), 0)

    def test_edge_large_integers(self):
        # Adding very large integers (Python handles arbitrary precision).
        self.assertEqual(add(1000000000000000000, 2000000000000000000), 3000000000000000000)

    def test_error_x_not_integer(self):
        # Input x is not an integer.
        with self.assertRaises(TypeError):
            add(2.5, 3)

    def test_error_y_not_integer(self):
        # Input y is not an integer.
        with self.assertRaises(TypeError):
            add(2, 'a')

    def test_error_both_not_integers(self):
        # Both inputs are not integers.
        with self.assertRaises(TypeError):
            add('hello', 'world')