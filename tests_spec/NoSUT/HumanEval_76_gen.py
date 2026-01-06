import unittest
from sut.problem_HumanEval_76 import is_simple_power

class Test_is_simple_power(unittest.TestCase):

    # Normal cases
    def test_x_is_one_any_n_true(self):
        # x=1, n=4, output: true (4^0 = 1)
        self.assertTrue(is_simple_power(1, 4))

    def test_base_equals_power_true(self):
        # x=2, n=2, output: true (2^1 = 2)
        self.assertTrue(is_simple_power(2, 2))

    def test_normal_power_true(self):
        # x=8, n=2, output: true (2^3 = 8)
        self.assertTrue(is_simple_power(8, 2))

    def test_normal_not_power_false(self):
        # x=3, n=2, output: false (3 is not a power of 2)
        self.assertFalse(is_simple_power(3, 2))

    def test_large_power_true(self):
        # x=27, n=3, output: true (3^3 = 27)
        self.assertTrue(is_simple_power(27, 3))

    # Edge cases
    def test_x_is_one_n_is_one_true(self):
        # x=1, n=1, output: true (1^0 = 1)
        self.assertTrue(is_simple_power(1, 1))

    def test_x_not_one_n_is_one_false(self):
        # x=3, n=1, output: false (1^k is always 1)
        self.assertFalse(is_simple_power(3, 1))

    def test_prime_not_power_false(self):
        # x=7, n=2, output: false (7 is a prime number and not a power of 2)
        self.assertFalse(is_simple_power(7, 2))

    def test_higher_power_true(self):
        # x=16, n=2, output: true (2^4 = 16)
        self.assertTrue(is_simple_power(16, 2))

    # Error conditions (assuming ValueError for out-of-range integers, TypeError for wrong types)
    def test_error_x_zero(self):
        # x=0, n=2, behavior: raises an error (violates x >= 1 precondition)
        with self.assertRaises(ValueError):
            is_simple_power(0, 2)

    def test_error_n_zero(self):
        # x=8, n=0, behavior: raises an error (violates n >= 1 precondition)
        with self.assertRaises(ValueError):
            is_simple_power(8, 0)

    def test_error_x_float(self):
        # x=8.0, n=2, behavior: raises an error (violates integer type precondition)
        with self.assertRaises(TypeError):
            is_simple_power(8.0, 2)

    def test_error_n_float(self):
        # x=8, n=2.5, behavior: raises an error (violates integer type precondition)
        with self.assertRaises(TypeError):
            is_simple_power(8, 2.5)