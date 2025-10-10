import unittest
from sut_llm.problem_HumanEval_43 import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_docstring_example_false_1(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))

    def test_docstring_example_true_1(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

    def test_single_element_list(self):
        self.assertFalse(pairs_sum_to_zero([7]))

    def test_two_elements_sum_to_zero(self):
        self.assertTrue(pairs_sum_to_zero([10, -10]))

    def test_two_elements_no_sum_to_zero(self):
        self.assertFalse(pairs_sum_to_zero([5, 8]))

    def test_multiple_elements_no_sum_to_zero(self):
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 4, 5]))

    def test_multiple_elements_with_sum_to_zero(self):
        self.assertTrue(pairs_sum_to_zero([-1, 2, -3, 1, 4]))

    def test_only_zeros_no_distinct_pair(self):
        self.assertTrue(pairs_sum_to_zero([0, 0, 0, 0]))

    def test_zero_and_other_numbers_with_pair(self):
        self.assertTrue(pairs_sum_to_zero([0, 5, -5, 1]))