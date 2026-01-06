import unittest
import sut.problem_HumanEval_116 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_array(self):
            # Edge case: Test with an empty list.
            self.assertListEqual(mod.sort_array([]), [])

    def test_single_element_array(self):
            # Edge case: Test with a list containing a single element.
            # 7 (binary 111) has 3 ones.
            self.assertListEqual(mod.sort_array([7]), [7])

    def test_all_same_bit_count_different_decimal(self):
            # Boundary condition: All numbers have the same number of set bits (1 one).
            # This test verifies the secondary sorting criterion (decimal value).
            # 1 (001), 2 (010), 4 (100), 8 (1000) all have 1 one.
            self.assertListEqual(mod.sort_array([8, 1, 4, 2]), [1, 2, 4, 8])

    def test_different_bit_counts_no_decimal_tie(self):
            # Logic mutation: Test where the primary sort key (bit count) is sufficient,
            # and no decimal tie-breaking is strictly necessary for the final order.
            # 0 (0) -> 0 ones
            # 1 (01) -> 1 one
            # 3 (11) -> 2 ones
            # 5 (101) -> 2 ones (decimal tie with 3, but 3 comes first)
            self.assertListEqual(mod.sort_array([3, 1, 5, 0]), [0, 1, 3, 5])

    def test_mixed_bit_counts_and_decimal_ties(self):
            # Typical input: Verifies both primary (bit count) and secondary (decimal) sort.
            # This test uses values from a docstring example, but applies the described sorting logic.
            # 1 (01) -> 1 one
            # 5 (101) -> 2 ones
            # 2 (10) -> 1 one
            # 3 (11) -> 2 ones
            # 4 (100) -> 1 one
            # Expected: [1, 2, 4] (1 one, sorted by decimal), then [3, 5] (2 ones, sorted by decimal).
            self.assertListEqual(mod.sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])

    def test_zero_and_other_numbers(self):
            # Typical input: Includes zero, verifying its correct placement (0 ones).
            # This test uses values from a docstring example, but applies the described sorting logic.
            # 0 (0) -> 0 ones
            # 1 (01) -> 1 one
            # 2 (10) -> 1 one
            # 3 (11) -> 2 ones
            # 4 (100) -> 1 one
            # Expected: [0] (0 ones), then [1, 2, 4] (1 one, sorted by decimal), then [3] (2 ones).
            self.assertListEqual(mod.sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 4, 3])

    def test_duplicates_and_mixed_counts(self):
            # Edge case: Test with duplicate values and mixed bit counts.
            # 6 (110) -> 2 ones
            # 3 (011) -> 2 ones
            # 5 (101) -> 2 ones
            # 1 (001) -> 1 one
            # Expected: [1] (1 one), then [3, 5, 6, 6] (2 ones, sorted by decimal).
            self.assertListEqual(mod.sort_array([6, 3, 5, 6, 1]), [1, 3, 5, 6, 6])

    def test_large_numbers_mixed_counts(self):
            # Extreme input: Test with larger numbers to ensure bit counting works for more bits.
            # 15 (1111) -> 4 ones
            # 7 (0111) -> 3 ones
            # 31 (11111) -> 5 ones
            # 10 (1010) -> 2 ones
            # Expected: [10] (2 ones), then [7] (3 ones), then [15] (4 ones), then [31] (5 ones).
            self.assertListEqual(mod.sort_array([15, 7, 31, 10]), [10, 7, 15, 31])

    def test_boundary_values_zero_one_two_three_bits(self):
            # Boundary condition: Test a range of small numbers covering 0, 1, 2, and 3 set bits.
            # This checks various combinations of primary and secondary sorting.
            # 0 (0) -> 0 ones
            # 1 (01) -> 1 one
            # 2 (10) -> 1 one
            # 3 (11) -> 2 ones
            # 4 (100) -> 1 one
            # 5 (101) -> 2 ones
            # 6 (110) -> 2 ones
            # 7 (111) -> 3 ones
            # Expected: [0] (0 ones), [1, 2, 4] (1 one), [3, 5, 6] (2 ones), [7] (3 ones).
            self.assertListEqual(mod.sort_array([0, 1, 2, 3, 4, 5, 6, 7]), [0, 1, 2, 4, 3, 5, 6, 7])

    def test_all_same_value(self):
            # Edge case: Test with all elements being identical.
            # 5 (101) has 2 ones.
            self.assertListEqual(mod.sort_array([5, 5, 5]), [5, 5, 5])

    def test_error_input_none(self):
            with self.assertRaises(TypeError):
                mod.sort_array(None)

    def test_error_input_not_list_int(self):
            with self.assertRaises(TypeError):
                mod.sort_array(123)

    def test_error_contains_float(self):
            arr = [1, 2.5, 3]
            with self.assertRaises(TypeError):
                mod.sort_array(arr)

    def test_error_contains_string(self):
            arr = [1, 'a', 3]
            with self.assertRaises(TypeError):
                mod.sort_array(arr)

