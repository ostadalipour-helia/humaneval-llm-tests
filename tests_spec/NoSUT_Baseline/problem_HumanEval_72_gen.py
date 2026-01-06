import unittest
import sut.problem_HumanEval_72 as mod

class TestHybrid(unittest.TestCase):
    def test_01_both_conditions_true_typical(self):
            # Example 3: Balanced and sum <= w
            self.assertEqual(mod.will_it_fly([3, 2, 3], 9), True)

    def test_02_palindrome_sum_exceeds_w_boundary(self):
            # Example 2: Balanced, but sum > w (boundary condition for sum)
            self.assertEqual(mod.will_it_fly([3, 2, 3], 1), False)

    def test_03_not_palindrome_sum_within_w(self):
            # Example 1: Not balanced, but sum <= w
            self.assertEqual(mod.will_it_fly([1, 2], 5), False)

    def test_04_empty_list_q_and_w_zero_edge_case(self):
            # Edge case: Empty list (is a palindrome), sum is 0, w is 0 (boundary for sum)
            self.assertEqual(mod.will_it_fly([], 0), True)

    def test_05_single_element_list_q_sum_equals_w_edge_case(self):
            # Edge case: Single element list (is a palindrome), sum equals w (boundary for sum)
            self.assertEqual(mod.will_it_fly([5], 5), True)

    def test_06_palindrome_sum_exactly_equals_w_boundary(self):
            # Boundary: Palindrome, sum(q) == w
            self.assertEqual(mod.will_it_fly([1, 2, 1], 4), True)

    def test_07_palindrome_sum_one_more_than_w_boundary(self):
            # Boundary: Palindrome, sum(q) = w + 1 (off-by-one for w)
            self.assertEqual(mod.will_it_fly([1, 2, 1], 3), False)

    def test_08_palindrome_sum_one_less_than_w_boundary(self):
            # Boundary: Palindrome, sum(q) = w - 1 (off-by-one for w)
            self.assertEqual(mod.will_it_fly([1, 2, 1], 5), True)

    def test_09_not_palindrome_and_sum_exceeds_w_both_false(self):
            # Logic mutation: Both conditions are false
            self.assertEqual(mod.will_it_fly([1, 2, 3], 1), False)

    def test_10_long_palindrome_large_numbers_extreme_input(self):
            # Extreme input: Longer list, larger numbers, both conditions true
            self.assertEqual(mod.will_it_fly([100, 200, 300, 200, 100], 1000), True)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_palindromic_sum_ok(self):
            q = [3, 2, 3]
            w = 9
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, True)
            self.assertEqual(q, original_q) # Invariant check

    def test_normal_not_palindromic(self):
            q = [1, 2]
            w = 5
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, False)
            self.assertEqual(q, original_q) # Invariant check

    def test_normal_palindromic_sum_too_high(self):
            q = [3, 2, 3]
            w = 1
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, False)
            self.assertEqual(q, original_q) # Invariant check

    def test_edge_empty_list(self):
            q = []
            w = 5
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, True)
            self.assertEqual(q, original_q) # Invariant check

    def test_edge_single_element_list(self):
            q = [3]
            w = 5
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, True)
            self.assertEqual(q, original_q) # Invariant check

    def test_edge_sum_exactly_w(self):
            q = [1, 2, 1]
            w = 4
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, True)
            self.assertEqual(q, original_q) # Invariant check

    def test_edge_negative_numbers(self):
            q = [-1, 0, -1]
            w = -2
            original_q = list(q) # For invariant check
            result = mod.will_it_fly(q, w)
            self.assertEqual(result, True)
            self.assertEqual(q, original_q) # Invariant check

    def test_error_q_not_list(self):
            q = "not a list"
            w = 5
            with self.assertRaises(TypeError):
                mod.will_it_fly(q, w)

    def test_error_w_not_int(self):
            q = [1, 2, 3]
            w = "not an int"
            original_q = list(q) # For invariant check, though error should prevent modification
            with self.assertRaises(TypeError):
                mod.will_it_fly(q, w)
            self.assertEqual(q, original_q) # Invariant check

    def test_error_q_elements_not_int(self):
            q = [1, "a", 3]
            w = 5
            original_q = list(q) # For invariant check, though error should prevent modification
            with self.assertRaises(TypeError):
                mod.will_it_fly(q, w)
            self.assertEqual(q, original_q) # Invariant check

