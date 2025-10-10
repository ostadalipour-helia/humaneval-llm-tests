import unittest
from sut_llm.problem_HumanEval_15 import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_n_is_zero_boundary(self):
        # Boundary Testing: Tests the exact lower boundary (n=0).
        # Edge Case: Represents a single-element sequence.
        self.assertEqual(string_sequence(0), '0')

    def test_n_is_one_off_by_one(self):
        # Off-by-One Error: Tests n=1 to catch common errors like range(n) instead of range(n+1).
        # Boundary Testing: Checks the next step from the minimum valid input.
        self.assertEqual(string_sequence(1), '0 1')

    def test_n_is_two_small_sequence(self):
        # Off-by-One Error: Further checks loop boundaries and iteration for a small sequence.
        # Typical Input: A common small positive integer input.
        self.assertEqual(string_sequence(2), '0 1 2')

    def test_n_is_five_docstring_example(self):
        # Typical Input: Verifies the example provided in the function's docstring.
        # Return Value Testing: Confirms the exact output for a standard case.
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_n_is_negative_one_edge_case(self):
        # Edge Case: Tests with a negative input (n=-1), which is not explicitly covered by examples.
        # Sign and Zero Testing: Checks behavior for negative 'n'.
        # Expected: An empty string, as range(0) would be empty.
        self.assertEqual(string_sequence(-1), '')

    def test_n_is_negative_five_extreme_negative(self):
        # Extreme/Unusual Input: Tests with a more extreme negative input (n=-5).
        # Edge Case: Further verifies robustness for unexpected negative values.
        self.assertEqual(string_sequence(-5), '')

    def test_n_is_large_positive_extreme(self):
        # Extreme/Unusual Input: Tests with a large positive number (n=100) to check scalability.
        # Return Value Testing: Ensures correct string generation for longer sequences.
        expected_output = ' '.join(str(i) for i in range(101))
        self.assertEqual(string_sequence(100), expected_output)

    def test_n_is_ten_typical_larger(self):
        # Typical Input: Tests a moderately larger positive integer.
        # Logic Mutations: Ensures correct sequence generation and joining for a common input size.
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_n_is_three_logic_check(self):
        # Logic Mutations: Tests a small sequence to ensure correct iteration and string concatenation.
        # Return Value Testing: Verifies the exact output for a specific sequence length.
        self.assertEqual(string_sequence(3), '0 1 2 3')

    def test_n_is_zero_reconfirm_boundary(self):
        # Boundary Testing: Reconfirms the lower boundary (n=0) to catch any regressions or mutations.
        # Logic Mutations: Specifically targets mutations that might incorrectly handle the base case (e.g., starting from 1).
        self.assertEqual(string_sequence(0), '0')