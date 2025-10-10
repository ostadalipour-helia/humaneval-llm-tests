import unittest
from sut_llm.problem_HumanEval_136 import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_mixed_pos_neg_typical(self):
        # Typical case with both positive and negative numbers
        self.assertEqual(largest_smallest_integers([-5, -2, 1, 3, 7]), (-2, 1))

    def test_all_positives(self):
        # Edge case: list contains only positive numbers
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_all_negatives(self):
        # Edge case: list contains only negative numbers
        self.assertEqual(largest_smallest_integers([-10, -5, -1, -8]), (-1, None))

    def test_empty_list(self):
        # Edge case: empty list
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_list_with_only_zero(self):
        # Edge case: list contains only zero
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_mixed_with_zero(self):
        # Boundary test: list contains zero along with positive and negative numbers
        self.assertEqual(largest_smallest_integers([-3, 0, 5, -1, 2]), (-1, 2))

    def test_boundary_one_and_minus_one(self):
        # Boundary test: smallest magnitude non-zero integers
        self.assertEqual(largest_smallest_integers([-1, 1]), (-1, 1))

    def test_large_numbers(self):
        # Extreme input: list with large positive and negative numbers
        self.assertEqual(largest_smallest_integers([-1000, -500, 100, 2000]), (-500, 100))

    def test_duplicates_and_mixed_order(self):
        # Logic mutation: list with duplicate values and mixed order
        self.assertEqual(largest_smallest_integers([5, -2, 3, -2, 1, 5]), (-2, 1))

    def test_single_positive_and_single_negative(self):
        # Off-by-one: list with exactly one positive and one negative number
        self.assertEqual(largest_smallest_integers([-5, 5]), (-5, 5))

if __name__ == '__main__':
    unittest.main()