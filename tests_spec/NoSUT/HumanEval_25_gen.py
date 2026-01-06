import unittest
from sut.problem_HumanEval_25 import factorize

class Test_factorize(unittest.TestCase):

    # Normal cases
    def test_normal_eight(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_normal_twenty_five(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_normal_seventy(self):
        self.assertEqual(factorize(70), [2, 5, 7])

    # Edge cases
    def test_edge_one(self):
        self.assertEqual(factorize(1), [])

    def test_edge_prime_two(self):
        self.assertEqual(factorize(2), [2])

    def test_edge_prime_seventeen(self):
        self.assertEqual(factorize(17), [17])

    def test_edge_perfect_square_four(self):
        self.assertEqual(factorize(4), [2, 2])

    def test_edge_large_prime(self):
        self.assertEqual(factorize(997), [997])

    # Error cases
    def test_error_zero(self):
        # Precondition: n must be greater than or equal to 1
        with self.assertRaises(ValueError):
            factorize(0)

    def test_error_negative(self):
        # Precondition: n must be greater than or equal to 1
        with self.assertRaises(ValueError):
            factorize(-5)

    def test_error_float(self):
        # Precondition: n must be an integer
        with self.assertRaises(TypeError):
            factorize(3.14)

    def test_error_string(self):
        # Precondition: n must be an integer
        with self.assertRaises(TypeError):
            factorize("abc")