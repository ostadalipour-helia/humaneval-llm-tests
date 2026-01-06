import unittest
from sut.problem_HumanEval_39 import prime_fib

class Test_prime_fib(unittest.TestCase):
    def test_normal_first_prime_fib(self):
        """
        Test case for n=1, the first prime Fibonacci number.
        """
        self.assertEqual(prime_fib(1), 2)

    def test_normal_second_prime_fib(self):
        """
        Test case for n=2, the second prime Fibonacci number.
        """
        self.assertEqual(prime_fib(2), 3)

    def test_normal_third_prime_fib(self):
        """
        Test case for n=3, the third prime Fibonacci number.
        """
        self.assertEqual(prime_fib(3), 5)

    def test_normal_fourth_prime_fib(self):
        """
        Test case for n=4, the fourth prime Fibonacci number.
        """
        self.assertEqual(prime_fib(4), 13)

    def test_normal_fifth_prime_fib(self):
        """
        Test case for n=5, the fifth prime Fibonacci number.
        """
        self.assertEqual(prime_fib(5), 89)

    def test_edge_smallest_valid_n(self):
        """
        Edge case: Smallest valid input for n (n=1).
        """
        self.assertEqual(prime_fib(1), 2)

    def test_error_n_is_zero(self):
        """
        Error case: Input n is zero, which is not a positive integer.
        Should raise ValueError.
        """
        with self.assertRaises(ValueError):
            prime_fib(0)

    def test_error_n_is_negative(self):
        """
        Error case: Input n is a negative integer, which is not a positive integer.
        Should raise ValueError.
        """
        with self.assertRaises(ValueError):
            prime_fib(-1)

    def test_error_n_is_float(self):
        """
        Error case: Input n is a float, but must be an integer.
        Should raise TypeError.
        """
        with self.assertRaises(TypeError):
            prime_fib(1.5)

    def test_error_n_is_string(self):
        """
        Error case: Input n is a string, but must be an integer.
        Should raise TypeError.
        """
        with self.assertRaises(TypeError):
            prime_fib("2")