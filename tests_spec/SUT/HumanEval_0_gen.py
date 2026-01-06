import unittest
from sut.problem_HumanEval_0 import has_close_elements

class Test_has_close_elements(unittest.TestCase):

    def test_normal_case_no_close_elements(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0, 2.0, 3.0], threshold=0.5),
            False
        )

    def test_normal_case_with_close_elements(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0, 2.8, 3.0, 4.0, 5.0, 2.0], threshold=0.3),
            True
        )

    def test_normal_case_with_small_difference(self):
        self.assertEqual(
            has_close_elements(numbers=[10.0, 10.05, 10.1, 10.2], threshold=0.06),
            True
        )

    def test_edge_case_empty_list(self):
        self.assertEqual(
            has_close_elements(numbers=[], threshold=0.5),
            False
        )

    def test_edge_case_single_element(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0], threshold=0.5),
            False
        )

    def test_edge_case_identical_elements(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0, 1.0, 2.0], threshold=0.1),
            True
        )

    def test_edge_case_zero_threshold(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0, 2.0, 3.0], threshold=0.0),
            False
        )

    def test_edge_case_large_threshold(self):
        self.assertEqual(
            has_close_elements(numbers=[1.0, 100.0], threshold=200.0),
            True
        )

    def test_edge_case_negative_numbers(self):
        self.assertEqual(
            has_close_elements(numbers=[-1.0, -1.2, 0.0], threshold=0.3),
            True
        )

    def test_invariant_input_list_not_modified(self):
        numbers_original = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        numbers_copy = list(numbers_original)
        has_close_elements(numbers_original, 0.3)
        self.assertListEqual(numbers_original, numbers_copy)