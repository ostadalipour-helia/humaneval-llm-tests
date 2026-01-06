import unittest
import sut.problem_HumanEval_20 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one_from_docstring(self):
            # Typical case: positive floats, non-zero difference, unsorted input
            numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
            expected = (2.0, 2.2)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_example_two_from_docstring_duplicates(self):
            # Edge case: duplicate numbers resulting in zero difference
            numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
            expected = (2.0, 2.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_minimum_length_list(self):
            # Boundary case: list with the minimum allowed length (2 elements)
            numbers = [5.0, 2.0]
            expected = (2.0, 5.0) # Ensure order (smaller, larger)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_negative_numbers(self):
            # Sign testing: all negative numbers, ensuring correct absolute difference and ordering
            numbers = [-1.0, -5.0, -2.0]
            expected = (-2.0, -1.0) # Closest are -2.0 and -1.0, ordered
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_mixed_positive_negative_zero(self):
            # Sign testing: mixed positive, negative, and zero values
            numbers = [0.0, -1.0, 1.0, 0.5]
            expected = (0.0, 0.5) # Closest are 0.0 and 0.5
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_all_same_values(self):
            # Edge case: all elements are identical, resulting in zero difference
            numbers = [3.0, 3.0, 3.0, 3.0]
            expected = (3.0, 3.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_large_numbers_and_small_difference(self):
            # Extreme input: large numbers with a very small difference, testing precision
            numbers = [1000000.0, 1000000.1, 1.0, 2.0]
            expected = (1000000.0, 1000000.1)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_numbers_with_different_magnitudes(self):
            # Typical case: numbers with varied magnitudes, ensuring the correct pair is found
            numbers = [1.0, 100.0, 1.1, 0.9, 50.0]
            expected = (0.9, 1.0) # Difference 0.1
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_reverse_sorted_list(self):
            # Logic mutation: ensure it works correctly regardless of input order, specifically reverse sorted
            # Assuming the first pair encountered with the minimum difference is returned.
            numbers = [5.0, 4.0, 3.0, 2.0]
            expected = (4.0, 5.0) # (5.0, 4.0) is the first pair with diff 1.0, returned as (4.0, 5.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_multiple_pairs_with_same_min_difference(self):
            # Logic mutation: test tie-breaking for minimum difference when multiple pairs exist
            # (1.0, 2.0) has diff 1.0, (4.0, 5.0) has diff 1.0. Expect the first encountered.
            numbers = [1.0, 2.0, 4.0, 5.0]
            expected = (1.0, 2.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected)

    def test_normal_distinct_closest(self):
            # "Typical case with distinct closest elements."
            numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
            expected_output = (2.0, 2.2)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_normal_non_adjacent_closest(self):
            # "Closest elements are not adjacent in the input list."
            numbers = [10.0, 1.0, 5.0, 8.0]
            expected_output = (8.0, 10.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_edge_identical_elements_multiple_times(self):
            # "Closest elements are identical and appear multiple times."
            numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
            expected_output = (2.0, 2.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_edge_two_elements_list(self):
            # "List with exactly two elements, requiring ordering."
            numbers = [5.0, 1.0]
            expected_output = (1.0, 5.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_edge_negative_numbers(self):
            # "List containing negative numbers."
            numbers = [-1.0, -2.0, -1.5]
            expected_output = (-1.5, -1.0)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_edge_high_precision_numbers(self):
            # "Numbers with high precision."
            numbers = [1.234567, 1.234568, 1.0]
            expected_output = (1.234567, 1.234568)
            self.assertEqual(mod.find_closest_elements(numbers), expected_output)

    def test_error_input_not_list(self):
            # "Input is not a list."
            numbers = None
            with self.assertRaises(TypeError):
                mod.find_closest_elements(numbers)

    def test_error_list_contains_string(self):
            # "Input list contains non-float elements (string)."
            numbers = [1.0, '2.0', 3.0]
            with self.assertRaises(TypeError):
                mod.find_closest_elements(numbers)

