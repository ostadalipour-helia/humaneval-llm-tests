import unittest
from sut.problem_HumanEval_163 import generate_integers

class Test_generate_integers(unittest.TestCase):

    def test_normal_range_ascending(self):
        # Normal case: a < b, multiple even numbers in range
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_normal_range_descending(self):
        # Normal case: a > b, multiple even numbers in range (checks invariant)
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_normal_odd_bounds(self):
        # Normal case: odd bounds, even numbers in between
        self.assertEqual(generate_integers(3, 7), [4, 6])

    def test_normal_single_element(self):
        # Normal case: a == b, and it's an even single-digit number
        self.assertEqual(generate_integers(2, 2), [2])

    def test_edge_no_single_digit_evens(self):
        # Edge case: range contains only numbers > 9
        self.assertEqual(generate_integers(10, 14), [])

    def test_edge_one_even_at_end(self):
        # Edge case: range starts with odd, ends with even, only one even number
        self.assertEqual(generate_integers(1, 2), [2])

    def test_edge_very_large_range(self):
        # Edge case: very large range, but only single-digit evens are included
        self.assertEqual(generate_integers(1, 100), [2, 4, 6, 8])

    def test_edge_same_odd_bounds(self):
        # Edge case: a == b, and it's an odd number
        self.assertEqual(generate_integers(9, 9), [])

    def test_error_a_zero(self):
        # Error case: a is not positive
        with self.assertRaises(ValueError):
            generate_integers(0, 8)

    def test_error_a_negative(self):
        # Error case: a is not positive
        with self.assertRaises(ValueError):
            generate_integers(-2, 8)

    def test_error_b_zero(self):
        # Error case: b is not positive
        with self.assertRaises(ValueError):
            generate_integers(2, 0)

    def test_error_b_string(self):
        # Error case: b is not an integer
        with self.assertRaises(TypeError):
            generate_integers(2, 'b')