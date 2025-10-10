import unittest
from sut_llm.problem_HumanEval_163 import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_basic_range(self):
        # Typical input, range includes multiple even digits
        self.assertListEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_reversed_range(self):
        # Input with b < a, should still return ascending order
        self.assertListEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_single_digit_evens_in_range(self):
        # Range where no single-digit even numbers exist (example from docstring)
        self.assertListEqual(generate_integers(10, 14), [])

    def test_single_even_output(self):
        # Boundary case: range includes exactly one even digit
        self.assertListEqual(generate_integers(2, 3), [2])

    def test_a_equals_b_even(self):
        # Edge case: a and b are the same even digit
        self.assertListEqual(generate_integers(4, 4), [4])

    def test_a_equals_b_odd(self):
        # Edge case: a and b are the same odd digit
        self.assertListEqual(generate_integers(5, 5), [])

    def test_range_from_one(self):
        # Boundary case: range starts from 1, includes some even digits
        self.assertListEqual(generate_integers(1, 5), [2, 4])

    def test_full_single_digit_range(self):
        # Extreme input: range covers all possible single-digit even numbers
        self.assertListEqual(generate_integers(1, 9), [2, 4, 6, 8])

    def test_large_range_no_evens(self):
        # Extreme input: large numbers, ensuring "digit" constraint is respected
        self.assertListEqual(generate_integers(100, 200), [])

    def test_upper_boundary_single_even(self):
        # Boundary case: range at the upper end of single digits, includes only one even
        self.assertListEqual(generate_integers(7, 9), [8])

if __name__ == '__main__':
    unittest.main()