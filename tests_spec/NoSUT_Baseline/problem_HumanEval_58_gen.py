import unittest
import sut.problem_HumanEval_58 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Typical case with duplicates in input lists, verifies uniqueness and sorting
            l1 = [1, 4, 3, 34, 653, 2, 5]
            l2 = [5, 7, 1, 5, 9, 653, 121]
            expected = [1, 5, 653]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_docstring_example_2(self):
            # Typical case where one list is a subset of the other, verifies sorting
            l1 = [5, 3, 2, 8]
            l2 = [3, 2]
            expected = [2, 3]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_empty_lists(self):
            # Edge case: both lists are empty
            l1 = []
            l2 = []
            expected = []
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_one_empty_list(self):
            # Edge case: one list is empty, the other is not
            l1 = [1, 2, 3]
            l2 = []
            expected = []
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_no_common_elements(self):
            # Boundary case: lists have no elements in common
            # Catches logic mutations like 'and' becoming 'or'
            l1 = [1, 2, 3]
            l2 = [4, 5, 6]
            expected = []
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_all_common_elements(self):
            # Boundary case: all elements are common and in order
            l1 = [1, 2, 3]
            l2 = [1, 2, 3]
            expected = [1, 2, 3]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_negative_numbers_and_zero(self):
            # Extreme case: includes negative numbers and zero, verifies sorting
            l1 = [-1, 0, 5, -3]
            l2 = [0, -3, 7, 5]
            expected = [-3, 0, 5]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_duplicates_in_both_lists_complex_order(self):
            # Edge case: multiple duplicates in both lists, verifies uniqueness and sorting
            l1 = [10, 20, 10, 30, 20]
            l2 = [20, 10, 40, 10, 50]
            expected = [10, 20]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_single_common_element_large_numbers(self):
            # Boundary/Extreme case: single common element with large numbers
            l1 = [1000000, 2, 3]
            l2 = [4, 1000000, 5]
            expected = [1000000]
            self.assertListEqual(mod.common(l1, l2), expected)

    def test_normal_case_1(self):
            l1 = [1, 4, 3, 34, 653, 2, 5]
            l2 = [5, 7, 1, 5, 9, 653, 121]
            expected_output = [1, 5, 653]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_normal_case_2(self):
            l1 = [5, 3, 2, 8]
            l2 = [3, 2]
            expected_output = [2, 3]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_normal_case_3(self):
            l1 = [10, 20, 30]
            l2 = [20, 40, 10]
            expected_output = [10, 20]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_empty_l1(self):
            l1 = []
            l2 = [1, 2, 3]
            expected_output = []
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_empty_l2(self):
            l1 = [1, 2, 3]
            l2 = []
            expected_output = []
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_both_empty(self):
            l1 = []
            l2 = []
            expected_output = []
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_no_common_elements(self):
            l1 = [1, 2, 3]
            l2 = [4, 5, 6]
            expected_output = []
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_with_duplicates_in_input(self):
            l1 = [1, 1, 2, 2, 3]
            l2 = [1, 2, 2, 4]
            expected_output = [1, 2]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_identical_lists(self):
            l1 = [1, 2, 3]
            l2 = [1, 2, 3]
            expected_output = [1, 2, 3]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_edge_string_elements(self):
            l1 = ["a", "b", "c"]
            l2 = ["c", "a", "d"]
            expected_output = ["a", "c"]
            self.assertEqual(mod.common(l1, l2), expected_output)

    def test_error_l2_not_list(self):
            l1 = [1, 2]
            l2 = None
            with self.assertRaises(TypeError):
                mod.common(l1, l2)

    def test_error_uncomparable_elements(self):
            # Dictionaries are not comparable by default for sorting or set operations
            l1 = [1, "a", {}]
            l2 = [1, "a", 3]
            with self.assertRaises(TypeError):
                mod.common(l1, l2)

