import unittest
from sut.problem_HumanEval_73 import smallest_change

class Test_smallest_change(unittest.TestCase):

    def test_normal_case_multiple_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_normal_case_single_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_normal_case_already_palindromic(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(smallest_change([5]), 0)

    def test_edge_case_two_elements_different(self):
        self.assertEqual(smallest_change([1, 2]), 1)

    def test_edge_case_two_elements_same(self):
        self.assertEqual(smallest_change([7, 7]), 0)

    def test_edge_case_all_identical(self):
        self.assertEqual(smallest_change([3, 3, 3, 3, 3]), 0)

    def test_edge_case_even_length_all_different(self):
        self.assertEqual(smallest_change([1, 2, 3, 4]), 2)

    def test_edge_case_odd_length_all_different(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5]), 2)