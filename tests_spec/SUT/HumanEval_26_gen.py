import unittest
from sut.problem_HumanEval_26 import remove_duplicates

class Test_remove_duplicates(unittest.TestCase):

    def test_mixed_unique_and_duplicates(self):
        # Test case from HumanEval specification
        # description: "Example from docstring: mixed unique and duplicate elements."
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_all_unique(self):
        # Test case from HumanEval specification
        # description: "All elements are unique, so all should be kept."
        self.assertEqual(remove_duplicates([5, 6, 7, 8]), [5, 6, 7, 8])

    def test_multiple_duplicates(self):
        # Test case from HumanEval specification
        # description: "Multiple elements appear more than once, some appear once."
        self.assertEqual(remove_duplicates([10, 20, 10, 30, 20, 40]), [30, 40])

    def test_empty_list(self):
        # Test case from HumanEval specification
        # description: "Empty input list."
        self.assertEqual(remove_duplicates([]), [])

    def test_all_duplicates(self):
        # Test case from HumanEval specification
        # description: "All elements are duplicates, so the output should be an empty list."
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [])

    def test_single_element(self):
        # Test case from HumanEval specification
        # description: "List with a single unique element."
        self.assertEqual(remove_duplicates([7]), [7])

    def test_negative_and_zero(self):
        # Test case from HumanEval specification
        # description: "List containing negative numbers and zero."
        self.assertEqual(remove_duplicates([-1, 0, -1, 2]), [0, 2])

    def test_order_preserved(self):
        # Re-testing a case to emphasize order preservation
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_no_change_for_unique_list(self):
        # Re-testing a case where the output should be identical to the input
        self.assertEqual(remove_duplicates([5, 6, 7, 8]), [5, 6, 7, 8])

    def test_removes_all_occurrences_of_duplicates(self):
        # Re-testing a case to ensure all instances of duplicated numbers are removed
        self.assertEqual(remove_duplicates([10, 20, 10, 30, 20, 40]), [30, 40])