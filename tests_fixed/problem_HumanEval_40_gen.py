import unittest
from sut_llm.problem_HumanEval_40 import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_docstring_example_true_repeated_value(self):
        # Test case from docstring: [1, 3, -2, 1] -> True (1 + (-2) + 1 = 0, using elements at different indices)
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))

    def test_docstring_example_false_no_triplet(self):
        # Test case from docstring: [1, 3, 5, 0] -> False
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))

    def test_docstring_example_true_mixed_numbers(self):
        # Test case from docstring: [2, 4, -5, 3, 9, 7] -> True (e.g., 2 + 3 + (-5) = 0)
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))

    def test_smallest_true_case(self):
        # Smallest possible list with three distinct elements that sum to zero
        self.assertTrue(triples_sum_to_zero([-1, 0, 1]))

    def test_smallest_false_case(self):
        # Smallest possible list with three elements that do not sum to zero
        self.assertFalse(triples_sum_to_zero([1, 2, 3]))

    def test_list_with_two_elements(self):
        # List with fewer than three elements should always return False
        self.assertFalse(triples_sum_to_zero([1, -1]))

    def test_list_with_one_element(self):
        # List with fewer than three elements should always return False
        self.assertFalse(triples_sum_to_zero([0]))

    def test_empty_list(self):
        # An empty list should always return False
        self.assertFalse(triples_sum_to_zero([]))

    def test_multiple_zeros_form_triplet(self):
        # Test case with multiple zeros, where three zeros sum to zero
        self.assertTrue(triples_sum_to_zero([0, 0, 0, 5]))

    def test_mixed_numbers_with_duplicates_no_sum_to_zero(self):
        # Test case with mixed numbers and duplicates, but no three distinct elements sum to zero
        self.assertFalse(triples_sum_to_zero([1, 1, 1, -1, -1, -1]))

if __name__ == '__main__':
    unittest.main()