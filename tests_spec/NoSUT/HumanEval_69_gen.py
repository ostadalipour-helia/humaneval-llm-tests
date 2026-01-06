import unittest
from sut.problem_HumanEval_69 import search

class Test_search(unittest.TestCase):

    # Normal Cases
    def test_normal_case_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_normal_case_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_normal_case_3(self):
        self.assertEqual(search([1, 1, 1, 1, 1]), 1)

    def test_normal_case_4(self):
        self.assertEqual(search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10)

    # Edge Cases
    def test_edge_case_single_element_satisfying(self):
        self.assertEqual(search([1]), 1)

    def test_edge_case_single_element_not_satisfying(self):
        self.assertEqual(search([2]), -1)

    def test_edge_case_no_elements_satisfying(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_edge_case_only_one_satisfying_among_many(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), 1)

    def test_edge_case_multiple_satisfying_with_non_satisfying(self):
        self.assertEqual(search([1, 1, 2, 2, 3, 3]), 2)

    # Error Cases
    def test_error_empty_list(self):
        with self.assertRaises((ValueError, AssertionError)):
            search([])

    def test_error_non_positive_integer_in_list(self):
        with self.assertRaises((ValueError, AssertionError)):
            search([-1, 2, 3])

    def test_error_float_in_list(self):
        with self.assertRaises((TypeError, ValueError, AssertionError)):
            search([1, 2.5, 3])

    def test_error_string_in_list(self):
        with self.assertRaises((TypeError, ValueError, AssertionError)):
            search([1, 'a', 3])

    def test_error_none_as_input(self):
        with self.assertRaises(TypeError):
            search(None)