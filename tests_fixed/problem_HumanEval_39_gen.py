import unittest
from sut_llm.problem_HumanEval_39 import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_n_is_1(self):
        # Boundary test: first element in the sequence
        # Edge case: smallest valid input for n
        self.assertEqual(prime_fib(1), 2)

    def test_n_is_2(self):
        # Boundary test: second element, often critical for off-by-one errors
        # Edge case: small input
        self.assertEqual(prime_fib(2), 3)

    def test_n_is_3(self):
        # Typical input: verifies correct progression
        self.assertEqual(prime_fib(3), 5)

    def test_n_is_4(self):
        # Typical input: verifies correct progression
        self.assertEqual(prime_fib(4), 13)

    def test_n_is_5(self):
        # Boundary test: last example from docstring
        self.assertEqual(prime_fib(5), 89)

    def test_n_is_6(self):
        # Extreme/Unusual input: one beyond the docstring examples
        # Tests for correct skipping of non-prime Fibonacci numbers (e.g., 144)
        self.assertEqual(prime_fib(6), 233)

    def test_n_is_7(self):
        # Extreme/Unusual input: requires more computation to find
        # Tests robustness for larger numbers and prime checking logic
        self.assertEqual(prime_fib(7), 1597)

    def test_n_is_8(self):
        # Extreme/Unusual input: even larger number, pushes computation further
        # F19 = 4181 is not prime (37 * 113).
        # The 8th prime Fibonacci number is F23 = 28657.
        self.assertEqual(prime_fib(8), 28657)

    def test_n_is_9(self):
        # Extreme/Unusual input: very large number, tests for potential performance issues
        # or correctness with larger primes/fibs
        self.assertEqual(prime_fib(9), 514229)

    def test_n_is_10(self):
        # Extreme/Unusual input: largest test case, ensures robustness and efficiency
        self.assertEqual(prime_fib(10), 433494437)