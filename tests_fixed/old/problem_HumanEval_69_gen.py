import unittest
from sut_llm.problem_HumanEval_69 import search

class TestSearchFunction(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_example_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_example_3_no_candidate(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_all_same_valid(self):
        self.assertEqual(search([1, 1, 1]), 1)

    def test_all_distinct_no_candidate(self):
        self.assertEqual(search([10, 20, 30]), -1)

    def test_multiple_candidates_greatest_is_not_smallest_value(self):
        self.assertEqual(search([2, 2, 2, 1, 1, 1, 1]), 2)

    def test_single_element_valid(self):
        self.assertEqual(search([1]), 1)

    def test_single_element_not_valid(self):
        self.assertEqual(search([5]), -1)

    def test_multiple_candidates_greatest_is_not_largest_number_in_list(self):
        self.assertEqual(search([10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5]), 5)

    def test_multiple_candidates_greatest_is_largest_number_in_list(self):
        self.assertEqual(search([7, 7, 7, 7, 7, 7, 7, 3, 3, 3]), 7)