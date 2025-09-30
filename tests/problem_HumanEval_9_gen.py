import unittest
from sut.problem_HumanEval_9 import rolling_max


class TestRollingMax(unittest.TestCase):

    def test_docstring_example(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_all_increasing_elements(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_decreasing_elements(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_all_same_elements(self):
        self.assertEqual(rolling_max([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_mixed_positive_and_negative(self):
        self.assertEqual(rolling_max([-1, -5, 0, 3, -2]), [-1, -1, 0, 3, 3])

    def test_list_with_zeros(self):
        self.assertEqual(rolling_max([0, -1, 2, 0, 5]), [0, 0, 2, 2, 5])

    def test_longer_list_complex_pattern(self):
        self.assertEqual(rolling_max([10, 1, 20, 5, 15, 30, 2]), [10, 10, 20, 20, 20, 30, 30])

    def test_max_at_beginning_then_decreasing(self):
        self.assertEqual(rolling_max([100, 90, 80, 70, 60]), [100, 100, 100, 100, 100])


if __name__ == '__main__':
    unittest.main()