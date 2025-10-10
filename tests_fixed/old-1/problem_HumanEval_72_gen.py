import unittest
from sut_llm.problem_HumanEval_72 import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_example_true_case_1(self):
        # Docstring example: balanced and sum <= w
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_example_true_case_2(self):
        # Docstring example: balanced (single element) and sum <= w
        self.assertTrue(will_it_fly([3], 5))

    def test_example_false_case_1(self):
        # Docstring example: sum <= w, but unbalanced
        self.assertFalse(will_it_fly([1, 2], 5))

    def test_example_false_case_2(self):
        # Docstring example: balanced, but sum > w
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_balanced_and_sum_less_than_w(self):
        # Balanced list, sum well within w
        self.assertTrue(will_it_fly([1, 2, 2, 1], 10))

    def test_empty_list_and_zero_weight(self):
        # Empty list is balanced, sum is 0, w is 0
        self.assertTrue(will_it_fly([], 0))

    def test_balanced_but_sum_equals_w(self):
        # Balanced list, sum exactly equals w
        self.assertTrue(will_it_fly([5, 0, 5], 10))

    def test_unbalanced_and_sum_less_than_w(self):
        # Unbalanced list, sum less than w
        self.assertFalse(will_it_fly([1, 2, 3], 10))

    def test_balanced_but_sum_greater_than_w(self):
        # Balanced list, sum greater than w
        self.assertFalse(will_it_fly([10, 5, 10], 20))

    def test_unbalanced_and_sum_greater_than_w(self):
        # Unbalanced list, sum greater than w
        self.assertFalse(will_it_fly([1, 5, 2], 5))

if __name__ == '__main__':
    unittest.main()