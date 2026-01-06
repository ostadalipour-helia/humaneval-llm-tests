import unittest
import sut.problem_HumanEval_39 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_1(self):
            # Boundary test: first element in the sequence
            # Edge case: smallest valid input for n
            self.assertEqual(mod.prime_fib(1), 2)

    def test_n_is_2(self):
            # Boundary test: second element, often critical for off-by-one errors
            # Edge case: small input
            self.assertEqual(mod.prime_fib(2), 3)

    def test_n_is_3(self):
            # Typical input: verifies correct progression
            self.assertEqual(mod.prime_fib(3), 5)

    def test_n_is_4(self):
            # Typical input: verifies correct progression
            self.assertEqual(mod.prime_fib(4), 13)

    def test_n_is_5(self):
            # Boundary test: last example from docstring
            self.assertEqual(mod.prime_fib(5), 89)

    def test_n_is_6(self):
            # Extreme/Unusual input: one beyond the docstring examples
            # Tests for correct skipping of non-prime Fibonacci numbers (e.g., 144)
            self.assertEqual(mod.prime_fib(6), 233)

    def test_n_is_7(self):
            # Extreme/Unusual input: requires more computation to find
            # Tests robustness for larger numbers and prime checking logic
            self.assertEqual(mod.prime_fib(7), 1597)

    def test_edge_smallest_valid_n(self):
            """
            Edge case: Smallest valid input for n (n=1).
            """
            self.assertEqual(mod.prime_fib(1), 2)

    def test_error_n_is_string(self):
            """
            Error case: Input n is a string, but must be an integer.
            Should raise TypeError.
            """
            with self.assertRaises(TypeError):
                mod.prime_fib("2")

