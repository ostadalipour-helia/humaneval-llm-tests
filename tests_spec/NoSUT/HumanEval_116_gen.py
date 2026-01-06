import unittest
import copy
from sut.problem_HumanEval_116 import sort_array

class Test_sort_array(unittest.TestCase):

    def test_normal_positive_integers(self):
        arr = [1, 5, 2, 3, 4]
        arr_copy = copy.deepcopy(arr)
        expected_output = [1, 2, 3, 4, 5]
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr) # Ensure a new list is returned
        self.assertEqual(arr, arr_copy) # Ensure original list is not modified
        self.assertEqual(len(result), len(arr_copy)) # Invariant: length
        self.assertEqual(sorted(result), sorted(arr_copy)) # Invariant: permutation

    def test_normal_mixed_integers(self):
        arr = [10, -5, 0, 3, -8, 7]
        arr_copy = copy.deepcopy(arr)
        expected_output = [-8, -5, 0, 3, 7, 10]
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr)
        self.assertEqual(arr, arr_copy)
        self.assertEqual(len(result), len(arr_copy))
        self.assertEqual(sorted(result), sorted(arr_copy))

    def test_normal_duplicate_integers(self):
        arr = [7, 2, 7, 1, 4, 2]
        arr_copy = copy.deepcopy(arr)
        expected_output = [1, 2, 2, 4, 7, 7]
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr)
        self.assertEqual(arr, arr_copy)
        self.assertEqual(len(result), len(arr_copy))
        self.assertEqual(sorted(result), sorted(arr_copy))

    def test_edge_empty_list(self):
        arr = []
        arr_copy = copy.deepcopy(arr)
        expected_output = []
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr)
        self.assertEqual(arr, arr_copy)
        self.assertEqual(len(result), len(arr_copy))
        self.assertEqual(sorted(result), sorted(arr_copy))

    def test_edge_single_element(self):
        arr = [42]
        arr_copy = copy.deepcopy(arr)
        expected_output = [42]
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr)
        self.assertEqual(arr, arr_copy)
        self.assertEqual(len(result), len(arr_copy))
        self.assertEqual(sorted(result), sorted(arr_copy))

    def test_edge_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        arr_copy = copy.deepcopy(arr)
        expected_output = [1, 2, 3, 4, 5]
        
        result = sort_array(arr)
        
        self.assertEqual(result, expected_output)
        self.assertIsNot(result, arr)
        self.assertEqual(arr, arr_copy)
        self.assertEqual(len(result), len(arr_copy))
        self.assertEqual(sorted(result), sorted(arr_copy))

    def test_error_input_none(self):
        with self.assertRaises(TypeError):
            sort_array(None)

    def test_error_input_not_list_int(self):
        with self.assertRaises(TypeError):
            sort_array(123)

    def test_error_contains_float(self):
        arr = [1, 2.5, 3]
        with self.assertRaises(TypeError):
            sort_array(arr)

    def test_error_contains_string(self):
        arr = [1, 'a', 3]
        with self.assertRaises(TypeError):
            sort_array(arr)