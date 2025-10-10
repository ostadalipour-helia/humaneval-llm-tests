import unittest
from sut.problem_HumanEval_72 import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_01_both_conditions_true_typical(self):
        # Example 3: Balanced and sum <= w
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)

    def test_02_palindrome_sum_exceeds_w_boundary(self):
        # Example 2: Balanced, but sum > w (boundary condition for sum)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)

    def test_03_not_palindrome_sum_within_w(self):
        # Example 1: Not balanced, but sum <= w
        self.assertEqual(will_it_fly([1, 2], 5), False)

    def test_04_empty_list_q_and_w_zero_edge_case(self):
        # Edge case: Empty list (is a palindrome), sum is 0, w is 0 (boundary for sum)
        self.assertEqual(will_it_fly([], 0), True)

    def test_05_single_element_list_q_sum_equals_w_edge_case(self):
        # Edge case: Single element list (is a palindrome), sum equals w (boundary for sum)
        self.assertEqual(will_it_fly([5], 5), True)

    def test_06_palindrome_sum_exactly_equals_w_boundary(self):
        # Boundary: Palindrome, sum(q) == w
        self.assertEqual(will_it_fly([1, 2, 1], 4), True)

    def test_07_palindrome_sum_one_more_than_w_boundary(self):
        # Boundary: Palindrome, sum(q) = w + 1 (off-by-one for w)
        self.assertEqual(will_it_fly([1, 2, 1], 3), False)

    def test_08_palindrome_sum_one_less_than_w_boundary(self):
        # Boundary: Palindrome, sum(q) = w - 1 (off-by-one for w)
        self.assertEqual(will_it_fly([1, 2, 1], 5), True)

    def test_09_not_palindrome_and_sum_exceeds_w_both_false(self):
        # Logic mutation: Both conditions are false
        self.assertEqual(will_it_fly([1, 2, 3], 1), False)

    def test_10_long_palindrome_large_numbers_extreme_input(self):
        # Extreme input: Longer list, larger numbers, both conditions true
        self.assertEqual(will_it_fly([100, 200, 300, 200, 100], 1000), True)

if __name__ == '__main__':
    unittest.main()