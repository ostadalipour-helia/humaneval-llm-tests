import unittest
import sut.problem_HumanEval_133 as mod

class TestHybrid(unittest.TestCase):
    def test_example_1_positive_integers(self):
            # Typical input, all positive integers
            # [1,2,3] -> ceil([1,2,3]) -> [1,2,3] -> 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
            self.assertEqual(mod.sum_squares([1, 2, 3]), 14)

    def test_example_2_positive_floats_and_zero(self):
            # Typical input, positive floats and zero, tests ceiling behavior
            # [1.4,4.2,0] -> ceil([1.4,4.2,0]) -> [2,5,0] -> 2^2 + 5^2 + 0^2 = 4 + 25 + 0 = 29
            self.assertEqual(mod.sum_squares([1.4, 4.2, 0]), 29)

    def test_example_3_negative_float_and_positives(self):
            # Critical test for negative float ceiling behavior
            # [-2.4,1,1] -> ceil([-2.4,1,1]) -> [-2,1,1] -> (-2)^2 + 1^2 + 1^2 = 4 + 1 + 1 = 6
            self.assertEqual(mod.sum_squares([-2.4, 1, 1]), 6)

    def test_empty_list_edge_case(self):
            # Edge case: empty list, should return 0
            self.assertEqual(mod.sum_squares([]), 0)

    def test_single_element_positive_float_boundary(self):
            # Edge case: single element, positive float, tests ceiling
            # [3.1] -> ceil([3.1]) -> [4] -> 4^2 = 16
            self.assertEqual(mod.sum_squares([3.1]), 16)

    def test_single_element_negative_float_boundary(self):
            # Edge case: single element, negative float, tests ceiling
            # [-3.9] -> ceil([-3.9]) -> [-3] -> (-3)^2 = 9
            self.assertEqual(mod.sum_squares([-3.9]), 9)

    def test_all_negative_integers(self):
            # Extreme input: all negative integers
            # [-1,-2,-3] -> ceil([-1,-2,-3]) -> [-1,-2,-3] -> (-1)^2 + (-2)^2 + (-3)^2 = 1 + 4 + 9 = 14
            self.assertEqual(mod.sum_squares([-1, -2, -3]), 14)

    def test_mixed_signs_and_floats_around_zero(self):
            # Logic mutation test: floats around zero and integers, mixed signs
            # [-0.5, 0.5, 1.5] -> ceil([-0.5, 0.5, 1.5]) -> [0, 1, 2] -> 0^2 + 1^2 + 2^2 = 0 + 1 + 4 = 5
            self.assertEqual(mod.sum_squares([-0.5, 0.5, 1.5]), 5)

    def test_boundary_just_below_and_above_integer(self):
            # Boundary testing for ceiling function: values just below, just above, and exact integer
            # [0.99, 1.01, 2.0] -> ceil([0.99, 1.01, 2.0]) -> [1, 2, 2] -> 1^2 + 2^2 + 2^2 = 1 + 4 + 4 = 9
            self.assertEqual(mod.sum_squares([0.99, 1.01, 2.0]), 9)

    def test_large_numbers_and_duplicates_after_ceiling(self):
            # Extreme input: large numbers, and values that become duplicates after ceiling
            # [99.1, 99.9, 100] -> ceil([99.1, 99.9, 100]) -> [100, 100, 100] -> 100^2 + 100^2 + 100^2 = 10000 + 10000 + 10000 = 30000
            self.assertEqual(mod.sum_squares([99.1, 99.9, 100]), 30000)

    def test_normal_all_positive_integers(self):
            # Description: All positive integers.
            original_lst = [1, 2, 3]
            lst_to_pass = list(original_lst) # Create a copy to check invariant
            result = mod.sum_squares(lst_to_pass)
            self.assertEqual(result, 14)
            self.assertEqual(lst_to_pass, original_lst, "Input list should not be modified.")

    def test_normal_mixed_floats_and_zero(self):
            # Description: Mixed positive floats and zero, demonstrating ceiling operation.
            original_lst = [1.4, 4.2, 0]
            lst_to_pass = list(original_lst) # Create a copy to check invariant
            result = mod.sum_squares(lst_to_pass)
            self.assertEqual(result, 29)
            self.assertEqual(lst_to_pass, original_lst, "Input list should not be modified.")

    def test_normal_mixed_negative_float(self):
            # Description: Mixed negative float and positive integers, demonstrating ceiling operation for negative numbers.
            lst = [-2.4, 1, 1]
            result = mod.sum_squares(lst)
            self.assertEqual(result, 6)

    def test_edge_empty_list(self):
            # Description: An empty list should return 0.
            lst = []
            result = mod.sum_squares(lst)
            self.assertEqual(result, 0)

    def test_edge_single_positive_float(self):
            # Description: A list with a single positive float, demonstrating ceiling.
            lst = [3.1]
            result = mod.sum_squares(lst)
            self.assertEqual(result, 16) # ceil(3.1) = 4, 4*4 = 16

    def test_edge_only_negative_floats(self):
            # Description: A list with only negative floats, demonstrating ceiling for negative numbers.
            lst = [-1.5, -3.8]
            result = mod.sum_squares(lst)
            self.assertEqual(result, 10) # ceil(-1.5) = -1, ceil(-3.8) = -3. (-1)^2 + (-3)^2 = 1 + 9 = 10

    def test_edge_numbers_close_to_zero(self):
            # Description: Numbers close to zero, demonstrating ceiling behavior.
            lst = [0.1, -0.1]
            result = mod.sum_squares(lst)
            self.assertEqual(result, 1) # ceil(0.1) = 1, ceil(-0.1) = 0. 1^2 + 0^2 = 1

    def test_error_input_is_none(self):
            # Description: Input is not a list (e.g., None).
            with self.assertRaises(TypeError):
                mod.sum_squares(None)

    def test_error_input_is_string(self):
            # Description: Input is not a list (e.g., string).
            with self.assertRaises(TypeError):
                mod.sum_squares("not_a_list")

    def test_error_list_contains_string(self):
            # Description: List contains non-numeric elements (e.g., string).
            with self.assertRaises(TypeError):
                mod.sum_squares([1, "a", 3])

    def test_error_list_contains_nested_list(self):
            # Description: List contains non-numeric elements (e.g., nested list).
            with self.assertRaises(TypeError):
                mod.sum_squares([1, [2, 3], 4])

