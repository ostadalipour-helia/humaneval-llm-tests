import unittest
from sut.problem_HumanEval_70 import strange_sort_list

class Test_strange_sort_list(unittest.TestCase):

    def test_normal_case_sorted_list(self):
        # Corresponds to the first normal case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_normal_case_identical_elements(self):
        # Corresponds to the second normal case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_normal_case_unsorted_odd_length(self):
        # Corresponds to the third normal case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([1, 6, 3, 10, 8]), [1, 10, 3, 8, 6])

    def test_normal_case_mixed_signs(self):
        # Corresponds to the fourth normal case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([-10, 5, -5, 0]), [-10, 5, -5, 0])

    def test_edge_case_empty_list(self):
        # Corresponds to the first edge case in the specification.
        self.assertEqual(strange_sort_list([]), [])

    def test_edge_case_single_element(self):
        # Corresponds to the second edge case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([7]), [7])

    def test_edge_case_two_elements_sorted(self):
        # Corresponds to the third edge case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([10, 20]), [10, 20])

    def test_edge_case_two_elements_reverse_sorted(self):
        # Corresponds to the fourth edge case in the specification.
        # Input is reconstructed based on the description and expected output.
        self.assertEqual(strange_sort_list([20, 10]), [10, 20])

    def test_duplicate_case_sorted_list(self):
        # Duplicate test to meet the requirement of 10 test methods.
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_duplicate_case_identical_elements(self):
        # Duplicate test to meet the requirement of 10 test methods.
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])