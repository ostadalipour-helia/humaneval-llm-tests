import unittest
import sut.problem_HumanEval_85 as mod

class TestHybrid(unittest.TestCase):
    def test_example_from_docstring(self):
            # Test the example provided in the docstring
            self.assertEqual(mod.add([4, 2, 6, 7]), 2)

    def test_single_element_list(self):
            # Edge case: a list with a single element. Index 0 is even, so no addition.
            self.assertEqual(mod.add([10]), 0)

    def test_no_matching_elements_all_odd_indices_odd_elements(self):
            # Logic mutation: odd index, but element is also odd. Should sum to 0.
            self.assertEqual(mod.add([1, 3, 5, 7]), 0)

    def test_mixed_elements_and_indices_positive_sum(self):
            # Typical input with multiple elements contributing to a positive sum.
            # Indices: 0, 1, 2, 3, 4, 5
            # Elements: 1, 2, 3, 4, 5, 6
            # Odd indices with even elements: lst[1]=2, lst[3]=4, lst[5]=6
            self.assertEqual(mod.add([1, 2, 3, 4, 5, 6]), 12)

    def test_negative_even_elements(self):
            # Sign testing: Test with negative even numbers at odd indices.
            # Odd indices with even elements: lst[1]=-2, lst[3]=-4, lst[5]=-6
            self.assertEqual(mod.add([1, -2, 3, -4, 5, -6]), -12)

    def test_zero_as_even_element(self):
            # Sign testing: Test with zero as an even element at odd indices.
            # Odd indices with even elements: lst[1]=0, lst[3]=4, lst[5]=0
            self.assertEqual(mod.add([1, 0, 3, 4, 5, 0]), 4)

    def test_boundary_last_element_is_target(self):
            # Boundary condition: The last element is at an odd index and is even.
            # Odd indices with even elements: lst[1]=2, lst[3]=4, lst[5]=8
            self.assertEqual(mod.add([1, 2, 3, 4, 5, 8]), 14)

    def test_boundary_last_element_not_target(self):
            # Boundary condition: The last element is at an odd index but is odd.
            # Odd indices with even elements: lst[1]=2, lst[3]=4
            self.assertEqual(mod.add([1, 2, 3, 4, 5, 7]), 6)

    def test_long_list_with_duplicates_and_zeros(self):
            # Extreme input: A longer list with various numbers, including duplicates and zeros.
            # Odd indices with even elements: lst[1]=20, lst[3]=40, lst[5]=60, lst[7]=80, lst[9]=100, lst[11]=-2
            self.assertEqual(mod.add([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, -2]), 298)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_mixed_elements(self):
            lst = [4, 2, 6, 7]
            original_lst = list(lst) # For invariance check
            result = mod.add(lst)
            self.assertEqual(result, 2)
            self.assertEqual(lst, original_lst) # Check invariance

    def test_normal_multiple_matches(self):
            lst = [1, 2, 3, 4, 5, 6]
            original_lst = list(lst)
            result = mod.add(lst)
            self.assertEqual(result, 8) # 2 (at index 1) + 6 (at index 5)
            self.assertEqual(lst, original_lst)

    def test_normal_larger_values(self):
            lst = [10, 20, 30, 40, 50]
            original_lst = list(lst)
            result = mod.add(lst)
            self.assertEqual(result, 60) # 20 (at index 1) + 40 (at index 3)
            self.assertEqual(lst, original_lst)

    def test_edge_all_odd_elements(self):
            lst = [1, 3, 5, 7]
            original_lst = list(lst)
            result = mod.add(lst)
            self.assertEqual(result, 0)
            self.assertEqual(lst, original_lst)

    def test_edge_all_even_elements(self):
            lst = [2, 4, 6, 8]
            original_lst = list(lst)
            result = mod.add(lst)
            self.assertEqual(result, 12) # 4 (at index 1) + 8 (at index 3)
            self.assertEqual(lst, original_lst)

    def test_edge_single_element(self):
            lst = [100]
            original_lst = list(lst)
            result = mod.add(lst)
            self.assertEqual(result, 0) # Element at index 0 (even index)
            self.assertEqual(lst, original_lst)

    def test_edge_zeros_and_negatives(self):
            lst = [0, 0, 0, 0, -2, -4, -6, -8]
            original_lst = list(lst)
            result = mod.add(lst)
            # 0 (idx 1) + 0 (idx 3) + -4 (idx 5) + -8 (idx 7) = -12
            self.assertEqual(result, -12)
            self.assertEqual(lst, original_lst)

    def test_error_non_integer_element(self):
            with self.assertRaises(TypeError):
                mod.add([1, 'a', 3])

    def test_error_input_not_list_none(self):
            with self.assertRaises(TypeError):
                mod.add(None)

    def test_error_input_not_list_int(self):
            with self.assertRaises(TypeError):
                mod.add(123)

