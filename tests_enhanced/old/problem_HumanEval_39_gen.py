import unittest
from sut_llm.problem_HumanEval_39 import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_6(self):
        self.assertEqual(prime_fib(6), 233)

    def test_prime_fib_7(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_prime_fib_8(self):
        self.assertEqual(prime_fib(8), 28657)

    def test_prime_fib_9(self):
        self.assertEqual(prime_fib(9), 514229)

    def test_is_prime_even_number_greater_than_two(self):
        # Covers line 8: `if num % 2 == 0:`
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(100))

    def test_prime_fib_n_not_positive(self):
        # Covers line 45: `raise ValueError("n must be a positive integer")`
        with self.assertRaises(ValueError):
            prime_fib(0)
        with self.assertRaises(ValueError):
            prime_fib(-1)
        with self.assertRaises(ValueError):
            prime_fib(-5)

