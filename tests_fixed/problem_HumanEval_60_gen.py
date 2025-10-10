import unittest
from sut_llm.problem_HumanEval_60 import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_positive_small_n_1(self):
        # Edge case: single element sum, boundary for smallest positive n
        self.assertEqual(sum_to_n(1), 1)

    def test_positive_small_n_2(self):
        # Off-by-one from n=1, typical small input
        self.assertEqual(sum_to_n(2), 3)

    def test_positive_small_n_3(self):
        # Typical input, matches a docstring example (implicitly 1+2+3=6)
        self.assertEqual(sum_to_n(3), 6)

    def test_positive_medium_n_5(self):
        # Typical input, matches a docstring example
        self.assertEqual(sum_to_n(5), 15)

    def test_positive_medium_n_10(self):
        # Typical input, matches a docstring example
        self.assertEqual(sum_to_n(10), 55)

    def test_positive_large_n_30(self):
        # Extreme/unusual input, matches a docstring example
        self.assertEqual(sum_to_n(30), 465)

    def test_positive_large_n_100(self):
        # Extreme/unusual input, matches a docstring example
        self.assertEqual(sum_to_n(100), 5050)

    def test_zero_n(self):
        # Boundary condition: n=0 (empty sum), edge case
        self.assertEqual(sum_to_n(0), 0)

    def test_negative_n(self):
        # Sign testing: negative input, edge case
        # The current implementation of sum_to_n applies the formula n * (n + 1) // 2
        # for all n, including negative.
        # For n = -5, it calculates -5 * (-5 + 1) // 2 = -5 * -4 // 2 = 20 // 2 = 10.
        # If the function's behavior for negative n is to follow the formula,
        # then the test should assert the result of that formula.
        self.assertEqual(sum_to_n(-5), 10)

    def test_large_positive_n_1000(self):
        # Extreme input to verify scalability and correctness for larger numbers
        self.assertEqual(sum_to_n(1000), 500500)