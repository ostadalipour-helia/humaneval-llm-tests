import unittest
from sut.problem_HumanEval_85 import add

class Test_add(unittest.TestCase):

    def test_normal_mixed_elements(self):
        lst = [4, 2, 6, 7]
        original_lst = list(lst) # For invariance check
        result = add(lst)
        self.assertEqual(result, 2)
        self.assertEqual(lst, original_lst) # Check invariance

    def test_normal_multiple_matches(self):
        lst = [1, 2, 3, 4, 5, 6]
        original_lst = list(lst)
        result = add(lst)
        self.assertEqual(result, 8) # 2 (at index 1) + 6 (at index 5)
        self.assertEqual(lst, original_lst)

    def test_normal_larger_values(self):
        lst = [10, 20, 30, 40, 50]
        original_lst = list(lst)
        result = add(lst)
        self.assertEqual(result, 60) # 20 (at index 1) + 40 (at index 3)
        self.assertEqual(lst, original_lst)

    def test_edge_all_odd_elements(self):
        lst = [1, 3, 5, 7]
        original_lst = list(lst)
        result = add(lst)
        self.assertEqual(result, 0)
        self.assertEqual(lst, original_lst)

    def test_edge_all_even_elements(self):
        lst = [2, 4, 6, 8]
        original_lst = list(lst)
        result = add(lst)
        self.assertEqual(result, 12) # 4 (at index 1) + 8 (at index 3)
        self.assertEqual(lst, original_lst)

    def test_edge_single_element(self):
        lst = [100]
        original_lst = list(lst)
        result = add(lst)
        self.assertEqual(result, 0) # Element at index 0 (even index)
        self.assertEqual(lst, original_lst)

    def test_edge_zeros_and_negatives(self):
        lst = [0, 0, 0, 0, -2, -4, -6, -8]
        original_lst = list(lst)
        result = add(lst)
        # 0 (idx 1) + 0 (idx 3) + -4 (idx 5) + -8 (idx 7) = -12
        self.assertEqual(result, -12)
        self.assertEqual(lst, original_lst)

    def test_error_empty_list(self):
        with self.assertRaises(ValueError):
            add([])

    def test_error_non_integer_element(self):
        with self.assertRaises(TypeError):
            add([1, 'a', 3])

    def test_error_input_not_list_none(self):
        with self.assertRaises(TypeError):
            add(None)

    def test_error_input_not_list_int(self):
        with self.assertRaises(TypeError):
            add(123)