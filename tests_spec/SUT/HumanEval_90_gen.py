import unittest
from sut.problem_HumanEval_90 import next_smallest

class Test_next_smallest(unittest.TestCase):

    def test_normal_case_sorted(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_normal_case_mixed_order(self):
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_normal_case_larger_numbers(self):
        self.assertEqual(next_smallest([10, 20, 30, 40, 50]), 20)

    def test_with_negative_numbers(self):
        # Note: The spec's expected output is -1, but the implementation correctly returns -5.
        # The test asserts the implementation's behavior.
        self.assertEqual(next_smallest([-5, -1, -10, 0, 5]), -5)

    def test_with_duplicates(self):
        self.assertEqual(next_smallest([100, 10, 20, 30, 100]), 20)

    def test_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_single_element_list(self):
        self.assertIsNone(next_smallest([1]))

    def test_one_distinct_element(self):
        self.assertIsNone(next_smallest([1, 1, 1, 1]))

    def test_two_distinct_elements(self):
        self.assertEqual(next_smallest([1, 2]), 2)

    def test_two_distinct_elements_with_duplicates(self):
        self.assertEqual(next_smallest([2, 2, 1, 1]), 2)