import unittest
from sut_llm.problem_HumanEval_68 import pluck

class TestPluck(unittest.TestCase):

    def test_1_empty_array(self):
        # Edge Case: Empty array, should return an empty list.
        # Covers: Empty collections, return path for no even values.
        self.assertEqual(pluck([]), [])

    def test_2_array_with_only_odd_numbers(self):
        # Edge Case: Array with no even numbers, should return an empty list.
        # Covers: No even values, return path, logic mutation (e.g., if 'and' was 'or' for condition).
        self.assertEqual(pluck([1, 3, 5, 7, 9]), [])

    def test_3_single_element_array_even(self):
        # Boundary Test: Smallest valid length (1 element), with an even number.
        # Covers: Single element collection, smallest even at index 0.
        self.assertEqual(pluck([10]), [10, 0])

    def test_4_single_element_array_odd(self):
        # Boundary Test: Smallest valid length (1 element), with an odd number.
        # Covers: Single element collection, no even values.
        self.assertEqual(pluck([9]), [])

    def test_5_basic_case_smallest_even_in_middle(self):
        # Typical Input: Example 1 from docstring.
        # Covers: Standard functionality, smallest even in a mixed array.
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_6_smallest_even_is_zero_with_duplicates(self):
        # Boundary Test & Logic Mutation: Smallest possible even value (0), with duplicates.
        # Covers: Zero testing, duplicate smallest even values, smallest index rule (Example 4).
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_7_smallest_even_at_beginning_of_array(self):
        # Off-by-One Error Test: Smallest even value is at the first index.
        # Covers: Array index 0, boundary condition for index.
        self.assertEqual(pluck([2, 4, 6, 8, 10]), [2, 0])

    def test_8_smallest_even_at_end_of_array(self):
        # Off-by-One Error Test: Smallest even value is at the last index.
        # Covers: Last array index, boundary condition for index.
        self.assertEqual(pluck([9, 7, 5, 3, 2]), [2, 4])

    def test_9_multiple_even_values_only_one_is_smallest(self):
        # Logic Mutation Test: Ensures the smallest even value is correctly identified among others.
        # Covers: Comparison logic, distinguishing smallest from other even numbers.
        self.assertEqual(pluck([10, 8, 12, 6, 14, 16]), [6, 3])

    def test_10_array_with_all_same_even_values(self):
        # Edge Case: Array where all elements are the same even value.
        # Covers: Duplicate values, all same values, smallest index rule.
        self.assertEqual(pluck([4, 4, 4, 4, 4]), [4, 0])