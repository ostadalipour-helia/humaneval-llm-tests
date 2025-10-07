import unittest
from sut_llm.problem_HumanEval_57 import monotonic

class TestMonotonic(unittest.TestCase):

    def test_strictly_increasing(self):
        self.assertTrue(monotonic([1, 2, 3, 4]))

    def test_strictly_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))

    def test_non_monotonic_up_then_down(self):
        self.assertFalse(monotonic([1, 2, 1]))

    def test_non_monotonic_down_then_up(self):
        self.assertFalse(monotonic([2, 1, 2]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_single_element_list(self):
        self.assertTrue(monotonic([5]))

    def test_two_elements_increasing(self):
        self.assertTrue(monotonic([1, 2]))

    def test_two_elements_decreasing(self):
        self.assertTrue(monotonic([2, 1]))

    def test_non_strictly_increasing_with_duplicates(self):
        # The function's implementation uses '<=' and '>=' for checking monotonicity,
        # which means it considers non-strictly increasing/decreasing sequences as monotonic.
        # Therefore, [1, 1, 2] is considered non-strictly increasing.
        self.assertTrue(monotonic([1, 1, 2]))

    def test_non_strictly_decreasing_with_duplicates(self):
        # The function's implementation allows for non-strict monotonicity (i.e., includes equality).
        # [3, 2, 2] is non-strictly decreasing.
        self.assertTrue(monotonic([3, 2, 2]))

if __name__ == '__main__':
    unittest.main()