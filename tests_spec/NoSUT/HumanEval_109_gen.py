import unittest
from sut.problem_HumanEval_109 import move_one_ball

class Test_move_one_ball(unittest.TestCase):
    def test_normal_case_rotatable_1(self):
        arr = [3, 4, 5, 1, 2]
        original_arr = list(arr) # Create a copy to check for modification
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr) # Ensure input array is not modified

    def test_normal_case_not_rotatable(self):
        arr = [3, 5, 4, 1, 2]
        original_arr = list(arr)
        self.assertFalse(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_normal_case_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_normal_case_rotatable_2(self):
        arr = [2, 3, 4, 5, 1]
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_edge_case_empty_array(self):
        arr = []
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_edge_case_single_element(self):
        arr = [7]
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_edge_case_two_elements_rotatable(self):
        arr = [2, 1]
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_edge_case_two_elements_already_sorted(self):
        arr = [1, 2]
        original_arr = list(arr)
        self.assertTrue(move_one_ball(arr))
        self.assertEqual(arr, original_arr)

    def test_error_case_none_input(self):
        with self.assertRaises(TypeError):
            move_one_ball(None)

    def test_error_case_int_input(self):
        with self.assertRaises(TypeError):
            move_one_ball(123)

    def test_error_case_mixed_type_list(self):
        # Comparing int with str will raise TypeError
        with self.assertRaises(TypeError):
            move_one_ball([1, 'a', 3])