import unittest
import sut.problem_HumanEval_163 as mod

class TestHybrid(unittest.TestCase):
    def test_basic_range(self):
            # Typical input, range includes multiple even digits
            self.assertListEqual(mod.generate_integers(2, 8), [2, 4, 6, 8])

    def test_reversed_range(self):
            # Input with b < a, should still return ascending order
            self.assertListEqual(mod.generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_single_digit_evens_in_range(self):
            # Range where no single-digit even numbers exist (example from docstring)
            self.assertListEqual(mod.generate_integers(10, 14), [])

    def test_single_even_output(self):
            # Boundary case: range includes exactly one even digit
            self.assertListEqual(mod.generate_integers(2, 3), [2])

    def test_a_equals_b_even(self):
            # Edge case: a and b are the same even digit
            self.assertListEqual(mod.generate_integers(4, 4), [4])

    def test_a_equals_b_odd(self):
            # Edge case: a and b are the same odd digit
            self.assertListEqual(mod.generate_integers(5, 5), [])

    def test_range_from_one(self):
            # Boundary case: range starts from 1, includes some even digits
            self.assertListEqual(mod.generate_integers(1, 5), [2, 4])

    def test_full_single_digit_range(self):
            # Extreme input: range covers all possible single-digit even numbers
            self.assertListEqual(mod.generate_integers(1, 9), [2, 4, 6, 8])

    def test_large_range_no_evens(self):
            # Extreme input: large numbers, ensuring "digit" constraint is respected
            self.assertListEqual(mod.generate_integers(100, 200), [])

    def test_upper_boundary_single_even(self):
            # Boundary case: range at the upper end of single digits, includes only one even
            self.assertListEqual(mod.generate_integers(7, 9), [8])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_range_ascending(self):
            # Normal case: a < b, multiple even numbers in range
            self.assertEqual(mod.generate_integers(2, 8), [2, 4, 6, 8])

    def test_normal_range_descending(self):
            # Normal case: a > b, multiple even numbers in range (checks invariant)
            self.assertEqual(mod.generate_integers(8, 2), [2, 4, 6, 8])

    def test_normal_odd_bounds(self):
            # Normal case: odd bounds, even numbers in between
            self.assertEqual(mod.generate_integers(3, 7), [4, 6])

    def test_normal_single_element(self):
            # Normal case: a == b, and it's an even single-digit number
            self.assertEqual(mod.generate_integers(2, 2), [2])

    def test_edge_no_single_digit_evens(self):
            # Edge case: range contains only numbers > 9
            self.assertEqual(mod.generate_integers(10, 14), [])

    def test_edge_one_even_at_end(self):
            # Edge case: range starts with odd, ends with even, only one even number
            self.assertEqual(mod.generate_integers(1, 2), [2])

    def test_edge_very_large_range(self):
            # Edge case: very large range, but only single-digit evens are included
            self.assertEqual(mod.generate_integers(1, 100), [2, 4, 6, 8])

    def test_edge_same_odd_bounds(self):
            # Edge case: a == b, and it's an odd number
            self.assertEqual(mod.generate_integers(9, 9), [])

    def test_error_b_string(self):
            # Error case: b is not an integer
            with self.assertRaises(TypeError):
                mod.generate_integers(2, 'b')

