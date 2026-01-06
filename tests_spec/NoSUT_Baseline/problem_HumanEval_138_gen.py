import unittest
import sut.problem_HumanEval_138 as mod

class TestHybrid(unittest.TestCase):
    def test_minimum_true_case(self):
            # Boundary test: Smallest number that can be a sum of 4 positive even numbers (2+2+2+2=8)
            # Also an edge case for the lower bound of 'True' results.
            self.assertEqual(mod.is_equal_to_sum_even(8), True)

    def test_one_below_minimum_true_case_odd(self):
            # Boundary test: One less than the minimum true case, and it's odd.
            # Catches off-by-one errors and logic mutations (e.g., changing >= to > or issues with odd numbers).
            self.assertEqual(mod.is_equal_to_sum_even(7), False)

    def test_one_below_minimum_true_case_even(self):
            # Boundary test: One less than the minimum true case, and it's even.
            # Catches off-by-one errors and logic mutations (e.g., changing >= to >).
            self.assertEqual(mod.is_equal_to_sum_even(6), False)

    def test_typical_even_number(self):
            # Typical input: A common even number well above the boundary.
            self.assertEqual(mod.is_equal_to_sum_even(10), True)

    def test_typical_odd_number_above_boundary(self):
            # Logic mutation test: Number is >= 8 but is odd.
            # Verifies the 'even' condition is correctly applied.
            self.assertEqual(mod.is_equal_to_sum_even(9), False)

    def test_zero_input(self):
            # Edge case: Zero input.
            # Tests handling of non-positive numbers.
            self.assertEqual(mod.is_equal_to_sum_even(0), False)

    def test_negative_even_input(self):
            # Edge case: Negative even number.
            # Tests handling of negative numbers.
            self.assertEqual(mod.is_equal_to_sum_even(-2), False)

    def test_large_even_number(self):
            # Extreme input: A very large even number.
            # Checks scalability and ensures logic holds for large values.
            self.assertEqual(mod.is_equal_to_sum_even(1000000), True)

    def test_large_odd_number(self):
            # Extreme input: A very large odd number.
            # Checks scalability and ensures odd numbers are correctly rejected even if large.
            self.assertEqual(mod.is_equal_to_sum_even(1000001), False)

    def test_another_small_even_false_case(self):
            # Edge case: Another small even number that should be false.
            # Reinforces the lower bound for 'True' results.
            self.assertEqual(mod.is_equal_to_sum_even(4), False)

    def test_normal_eight(self):
            # n = 8, output = True, reasoning: 8 is an even number and 8 >= 8. It can be written as 2 + 2 + 2 + 2.
            self.assertTrue(mod.is_equal_to_sum_even(8))

    def test_normal_ten(self):
            # n = 10, output = True, reasoning: 10 is an even number and 10 >= 8. It can be written as 2 + 2 + 2 + 4.
            self.assertTrue(mod.is_equal_to_sum_even(10))

    def test_normal_twelve(self):
            # n = 12, output = True, reasoning: 12 is an even number and 12 >= 8. It can be written as 2 + 2 + 4 + 4.
            self.assertTrue(mod.is_equal_to_sum_even(12))

    def test_edge_four(self):
            # n = 4, output = False, reasoning: 4 is an even number but 4 < 8. The minimum sum of 4 positive even numbers is 8.
            self.assertFalse(mod.is_equal_to_sum_even(4))

    def test_edge_six(self):
            # n = 6, output = False, reasoning: 6 is an even number but 6 < 8. The minimum sum of 4 positive even numbers is 8.
            self.assertFalse(mod.is_equal_to_sum_even(6))

    def test_edge_seven(self):
            # n = 7, output = False, reasoning: 7 is an odd number. The sum of 4 even numbers must always be even.
            self.assertFalse(mod.is_equal_to_sum_even(7))

    def test_edge_nine(self):
            # n = 9, output = False, reasoning: 9 is an odd number. The sum of 4 even numbers must always be even.
            self.assertFalse(mod.is_equal_to_sum_even(9))

    def test_edge_zero(self):
            # n = 0, output = False, reasoning: 0 is an even number but 0 < 8. Also, positive even numbers cannot sum to zero.
            self.assertFalse(mod.is_equal_to_sum_even(0))

    def test_edge_negative_two(self):
            # n = -2, output = False, reasoning: -2 is a negative number. Positive even numbers cannot sum to a negative number.
            self.assertFalse(mod.is_equal_to_sum_even(-2))

    def test_error_string_input(self):
            # n = 'hello', exception = TypeError, reasoning: The input `n` must be an integer, not a string.
            with self.assertRaises(TypeError):
                mod.is_equal_to_sum_even('hello')

    def test_error_none_input(self):
            # n = None, exception = TypeError, reasoning: The input `n` must be an integer, not None.
            with self.assertRaises(TypeError):
                mod.is_equal_to_sum_even(None)

