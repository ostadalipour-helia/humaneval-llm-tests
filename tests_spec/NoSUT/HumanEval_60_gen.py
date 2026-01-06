import unittest
from sut.problem_HumanEval_60 import sum_to_n

class Test_sum_to_n(unittest.TestCase):
    def test_normal_positive_30(self):
        """
        Test with a typical positive integer input: n = 30.
        Expected output: 465.
        """
        self.assertEqual(sum_to_n(30), 465)

    def test_normal_positive_100(self):
        """
        Test with a larger positive integer input: n = 100.
        Expected output: 5050.
        """
        self.assertEqual(sum_to_n(100), 5050)

    def test_normal_positive_5(self):
        """
        Test with another typical positive integer input: n = 5.
        Expected output: 15.
        """
        self.assertEqual(sum_to_n(5), 15)

    def test_edge_zero(self):
        """
        Test with the smallest valid non-negative input: n = 0.
        Represents an empty sum, expected output: 0.
        """
        self.assertEqual(sum_to_n(0), 0)

    def test_edge_one(self):
        """
        Test with the smallest positive integer input: n = 1.
        Sums only itself, expected output: 1.
        """
        self.assertEqual(sum_to_n(1), 1)

    def test_error_negative_input(self):
        """
        Test with a negative integer input: n = -5.
        Should raise a ValueError as 'n' must be non-negative.
        """
        with self.assertRaises(ValueError):
            sum_to_n(-5)

    def test_error_float_input(self):
        """
        Test with a float input: n = 3.5.
        Should raise a TypeError as 'n' must be an integer.
        """
        with self.assertRaises(TypeError):
            sum_to_n(3.5)

    def test_error_string_input(self):
        """
        Test with a string input: n = 'abc'.
        Should raise a TypeError as 'n' must be an integer.
        """
        with self.assertRaises(TypeError):
            sum_to_n('abc')