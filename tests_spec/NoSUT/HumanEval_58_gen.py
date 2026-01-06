import unittest
from sut.problem_HumanEval_58 import common

class Test_common(unittest.TestCase):

    def test_normal_case_1(self):
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        expected_output = [1, 5, 653]
        self.assertEqual(common(l1, l2), expected_output)

    def test_normal_case_2(self):
        l1 = [5, 3, 2, 8]
        l2 = [3, 2]
        expected_output = [2, 3]
        self.assertEqual(common(l1, l2), expected_output)

    def test_normal_case_3(self):
        l1 = [10, 20, 30]
        l2 = [20, 40, 10]
        expected_output = [10, 20]
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_empty_l1(self):
        l1 = []
        l2 = [1, 2, 3]
        expected_output = []
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_empty_l2(self):
        l1 = [1, 2, 3]
        l2 = []
        expected_output = []
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_both_empty(self):
        l1 = []
        l2 = []
        expected_output = []
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_no_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        expected_output = []
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_with_duplicates_in_input(self):
        l1 = [1, 1, 2, 2, 3]
        l2 = [1, 2, 2, 4]
        expected_output = [1, 2]
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_identical_lists(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(common(l1, l2), expected_output)

    def test_edge_string_elements(self):
        l1 = ["a", "b", "c"]
        l2 = ["c", "a", "d"]
        expected_output = ["a", "c"]
        self.assertEqual(common(l1, l2), expected_output)

    def test_error_l1_not_list(self):
        l1 = "not a list"
        l2 = [1, 2]
        with self.assertRaises(TypeError):
            common(l1, l2)

    def test_error_l2_not_list(self):
        l1 = [1, 2]
        l2 = None
        with self.assertRaises(TypeError):
            common(l1, l2)

    def test_error_uncomparable_elements(self):
        # Dictionaries are not comparable by default for sorting or set operations
        l1 = [1, "a", {}]
        l2 = [1, "a", 3]
        with self.assertRaises(TypeError):
            common(l1, l2)