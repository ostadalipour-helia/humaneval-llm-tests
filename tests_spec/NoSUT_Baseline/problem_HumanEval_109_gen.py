import unittest
import sut.problem_HumanEval_109 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_array(self):
            # Edge case: Empty array, explicitly stated to return True
            self.assertEqual(mod.move_one_ball([]), True)

    def test_single_element_array(self):
            # Edge case: Single element array, already sorted
            self.assertEqual(mod.move_one_ball([7]), True)

    def test_already_sorted_array(self):
            # Boundary condition: Array is already sorted (0 shifts needed)
            self.assertEqual(mod.move_one_ball([1, 2, 3, 4, 5]), True)

    def test_one_shift_needed_at_end(self):
            # Boundary condition: Array needs one right shift to be sorted
            # This means the smallest element is at the second position
            self.assertEqual(mod.move_one_ball([5, 1, 2, 3, 4]), True)

    def test_n_minus_one_shifts_needed_at_start(self):
            # Boundary condition: Array needs N-1 right shifts to be sorted
            # This means the largest element is at the second to last position
            self.assertEqual(mod.move_one_ball([2, 3, 4, 5, 1]), True)

    def test_docstring_example_true(self):
            # Typical input: Example from docstring that returns True
            self.assertEqual(mod.move_one_ball([3, 4, 5, 1, 2]), True)

    def test_docstring_example_false(self):
            # Typical input: Example from docstring that returns False
            # This tests for multiple "descents" or non-rotatable sequences
            self.assertEqual(mod.move_one_ball([3, 5, 4, 1, 2]), False)

    def test_one_descent_but_not_rotatable(self):
            # Extreme/unusual input: Has only one "descent" point, but cannot be sorted by rotation
            # This tests the full logic, not just counting descents
            self.assertEqual(mod.move_one_ball([1, 5, 2, 3, 4]), False)

    def test_negative_numbers_and_zero_rotatable(self):
            # Extreme/unusual input: Array with negative numbers and zero, rotatable
            # Tests sign handling
            self.assertEqual(mod.move_one_ball([-5, -3, 0, 2, -7]), True)

    def test_large_numbers_one_shift_rotatable(self):
            # Extreme/unusual input: Array with large numbers, rotatable
            # Tests handling of large integer values
            self.assertEqual(mod.move_one_ball([1000000, 1, 2, 3, 4]), True)

    def test_normal_case_rotatable_1(self):
            arr = [3, 4, 5, 1, 2]
            original_arr = list(arr) # Create a copy to check for modification
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr) # Ensure input array is not modified

    def test_normal_case_not_rotatable(self):
            arr = [3, 5, 4, 1, 2]
            original_arr = list(arr)
            self.assertFalse(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_normal_case_already_sorted(self):
            arr = [1, 2, 3, 4, 5]
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_normal_case_rotatable_2(self):
            arr = [2, 3, 4, 5, 1]
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_edge_case_empty_array(self):
            arr = []
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_edge_case_single_element(self):
            arr = [7]
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_edge_case_two_elements_rotatable(self):
            arr = [2, 1]
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_edge_case_two_elements_already_sorted(self):
            arr = [1, 2]
            original_arr = list(arr)
            self.assertTrue(mod.move_one_ball(arr))
            self.assertEqual(arr, original_arr)

    def test_error_case_none_input(self):
            with self.assertRaises(TypeError):
                mod.move_one_ball(None)

    def test_error_case_int_input(self):
            with self.assertRaises(TypeError):
                mod.move_one_ball(123)

    def test_error_case_mixed_type_list(self):
            # Comparing int with str will raise TypeError
            with self.assertRaises(TypeError):
                mod.move_one_ball([1, 'a', 3])

