import unittest
from sut.problem_HumanEval_55 import fib

class Test_fib(unittest.TestCase):
    def test_normal_n_10(self):
        # Normal case: n = 10
        self.assertEqual(fib(10), 55)

    def test_normal_n_8(self):
        # Normal case: n = 8
        self.assertEqual(fib(8), 21)

    def test_normal_n_5(self):
        # Normal case: n = 5
        self.assertEqual(fib(5), 5)

    def test_edge_n_1_smallest_valid(self):
        # Edge case: Smallest valid input n = 1
        self.assertEqual(fib(1), 1)

    def test_edge_n_2_second_smallest(self):
        # Edge case: Second smallest valid input n = 2
        self.assertEqual(fib(2), 1)

    def test_edge_n_3_third_smallest(self):
        # Edge case: Third smallest valid input n = 3
        self.assertEqual(fib(3), 2)

    def test_error_n_zero(self):
        # Error case: n = 0 (violates n >= 1)
        with self.assertRaises(ValueError):
            fib(0)

    def test_error_n_negative(self):
        # Error case: n = -5 (violates n >= 1)
        with self.assertRaises(ValueError):
            fib(-5)

    def test_error_n_float(self):
        # Error case: n is a float (violates n must be an integer)
        with self.assertRaises(TypeError):
            fib(10.5)

    def test_error_n_string(self):
        # Error case: n is a string (violates n must be an integer)
        with self.assertRaises(TypeError):
            fib("abc")