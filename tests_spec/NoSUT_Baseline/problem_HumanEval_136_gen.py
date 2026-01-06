import unittest
import sut.problem_HumanEval_136 as mod

class TestHybrid(unittest.TestCase):
    def test_mixed_pos_neg_typical(self):
            # Typical case with both positive and negative numbers
            self.assertEqual(mod.largest_smallest_integers([-5, -2, 1, 3, 7]), (-2, 1))

    def test_all_positives(self):
            # Edge case: list contains only positive numbers
            self.assertEqual(mod.largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_all_negatives(self):
            # Edge case: list contains only negative numbers
            self.assertEqual(mod.largest_smallest_integers([-10, -5, -1, -8]), (-1, None))

    def test_empty_list(self):
            # Edge case: empty list
            self.assertEqual(mod.largest_smallest_integers([]), (None, None))

    def test_list_with_only_zero(self):
            # Edge case: list contains only zero
            self.assertEqual(mod.largest_smallest_integers([0]), (None, None))

    def test_mixed_with_zero(self):
            # Boundary test: list contains zero along with positive and negative numbers
            self.assertEqual(mod.largest_smallest_integers([-3, 0, 5, -1, 2]), (-1, 2))

    def test_boundary_one_and_minus_one(self):
            # Boundary test: smallest magnitude non-zero integers
            self.assertEqual(mod.largest_smallest_integers([-1, 1]), (-1, 1))

    def test_large_numbers(self):
            # Extreme input: list with large positive and negative numbers
            self.assertEqual(mod.largest_smallest_integers([-1000, -500, 100, 2000]), (-500, 100))

    def test_duplicates_and_mixed_order(self):
            # Logic mutation: list with duplicate values and mixed order
            self.assertEqual(mod.largest_smallest_integers([5, -2, 3, -2, 1, 5]), (-2, 1))

    def test_single_positive_and_single_negative(self):
            # Off-by-one: list with exactly one positive and one negative number
            self.assertEqual(mod.largest_smallest_integers([-5, 5]), (-5, 5))
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_mixed_pos_neg_integers(self):
            self.assertEqual(mod.largest_smallest_integers([1, 2, 3, -1, -2, -3]), (-1, 1))

    def test_normal_mixed_pos_neg_different_ranges(self):
            self.assertEqual(mod.largest_smallest_integers([-10, -5, -1, 1, 5, 10]), (-1, 1))

    def test_normal_only_positive_integers(self):
            self.assertEqual(mod.largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_normal_only_negative_integers(self):
            self.assertEqual(mod.largest_smallest_integers([-1, -5, -10, -2]), (-1, None))
    
        # Edge Cases

    def test_edge_empty_list(self):
            self.assertEqual(mod.largest_smallest_integers([]), (None, None))

    def test_edge_list_with_only_zero(self):
            self.assertEqual(mod.largest_smallest_integers([0]), (None, None))

    def test_edge_single_negative_integer(self):
            self.assertEqual(mod.largest_smallest_integers([-1]), (-1, None))

    def test_edge_single_positive_integer(self):
            self.assertEqual(mod.largest_smallest_integers([1]), (None, 1))

    def test_edge_list_with_zero_and_extremes(self):
            self.assertEqual(mod.largest_smallest_integers([-5, 0, 5]), (-5, 5))

    def test_edge_smallest_negative_and_smallest_positive(self):
            self.assertEqual(mod.largest_smallest_integers([-1, 1]), (-1, 1))
    
        # Error Cases

    def test_error_input_is_none(self):
            with self.assertRaises(TypeError):
                mod.largest_smallest_integers(None)

    def test_error_input_is_not_list(self):
            with self.assertRaises(TypeError):
                mod.largest_smallest_integers(123)

    def test_error_list_contains_string(self):
            with self.assertRaises(TypeError):
                mod.largest_smallest_integers([1, "a", 3])

