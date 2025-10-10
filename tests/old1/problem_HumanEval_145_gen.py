import unittest
from sut.problem_HumanEval_145 import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element_list(self):
        self.assertEqual(order_by_points([5]), [5])

    def test_positive_integers_no_ties(self):
        # Sums: 1, 2, 3, 1 (for 10), 2 (for 11)
        # Expected order by sum: 1, 1, 2, 2, 3
        # Tie-breaking by original index: 1 (idx 0), 10 (idx 3), 2 (idx 1), 11 (idx 4), 3 (idx 2)
        self.assertEqual(order_by_points([1, 2, 3, 10, 11]), [1, 10, 2, 11, 3])

    def test_positive_integers_with_ties_stable_sort(self):
        # All have sum of digits = 1. Order by original index.
        self.assertEqual(order_by_points([10, 1, 100]), [10, 1, 100])

    def test_mixed_positive_negative_example_interpretation(self):
        # Based on docstring text: sum_digits(abs(n)), then stable sort by original index.
        # 1 (sum 1, idx 0), 11 (sum 2, idx 1), -1 (sum 1, idx 2), -11 (sum 2, idx 3), -12 (sum 3, idx 4)
        # Sorted: (1,0,1), (1,2,-1), (2,1,11), (2,3,-11), (3,4,-12)
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [1, -1, 11, -11, -12])

    def test_all_negative_integers_no_ties(self):
        # Sums (abs): 1, 2, 3, 1 (for -10), 2 (for -11)
        # Expected order by sum: 1, 1, 2, 2, 3
        # Tie-breaking by original index: -1 (idx 0), -10 (idx 3), -2 (idx 1), -11 (idx 4), -3 (idx 2)
        self.assertEqual(order_by_points([-1, -2, -3, -10, -11]), [-1, -10, -2, -11, -3])

    def test_all_negative_integers_with_ties_stable_sort(self):
        # All have sum of digits (abs) = 1. Order by original index.
        self.assertEqual(order_by_points([-10, -1, -100]), [-10, -1, -100])

    def test_list_with_zero(self):
        # Sums: 0 (for 0), 1 (for 10), 1 (for -1), 1 (for 1)
        # Sorted: 0 (idx 0), 10 (idx 1), -1 (idx 2), 1 (idx 3)
        self.assertEqual(order_by_points([0, 10, -1, 1]), [0, 10, -1, 1])

    def test_larger_numbers_complex_sums(self):
        # 123 (sum 6, idx 0)
        # 45 (sum 9, idx 1)
        # 6 (sum 6, idx 2)
        # 789 (sum 24, idx 3)
        # 1000 (sum 1, idx 4)
        # Sorted: (1,4,1000), (6,0,123), (6,2,6), (9,1,45), (24,3,789)
        self.assertEqual(order_by_points([123, 45, 6, 789, 1000]), [1000, 123, 6, 45, 789])

    def test_list_with_duplicate_numbers(self):
        # All have sum of digits = 1. Order by original index.
        self.assertEqual(order_by_points([1, 10, 1, 100, 10]), [1, 10, 1, 100, 10])

if __name__ == '__main__':
    unittest.main()