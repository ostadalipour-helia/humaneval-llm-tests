import unittest
from sut_llm.problem_HumanEval_85 import add

class TestAddFunction(unittest.TestCase):

    def test_example_from_docstring(self):
        # Test the example provided in the docstring
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_single_element_list(self):
        # Edge case: a list with a single element. Index 0 is even, so no addition.
        self.assertEqual(add([10]), 0)

    def test_no_matching_elements_all_odd_indices_odd_elements(self):
        # Logic mutation: odd index, but element is also odd. Should sum to 0.
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_no_matching_elements_all_even_indices_even_elements(self):
        # Logic mutation: element is even, but index is even. Should sum to 0.
        # Changed input to ensure no even elements are at odd indices,
        # thus correctly resulting in a sum of 0.
        self.assertEqual(add([2, 3, 6, 7]), 0)

    def test_mixed_elements_and_indices_positive_sum(self):
        # Typical input with multiple elements contributing to a positive sum.
        # Indices: 0, 1, 2, 3, 4, 5
        # Elements: 1, 2, 3, 4, 5, 6
        # Odd indices with even elements: lst[1]=2, lst[3]=4, lst[5]=6
        self.assertEqual(add([1, 2, 3, 4, 5, 6]), 12)

    def test_negative_even_elements(self):
        # Sign testing: Test with negative even numbers at odd indices.
        # Odd indices with even elements: lst[1]=-2, lst[3]=-4, lst[5]=-6
        self.assertEqual(add([1, -2, 3, -4, 5, -6]), -12)

    def test_zero_as_even_element(self):
        # Sign testing: Test with zero as an even element at odd indices.
        # Odd indices with even elements: lst[1]=0, lst[3]=4, lst[5]=0
        self.assertEqual(add([1, 0, 3, 4, 5, 0]), 4)

    def test_boundary_last_element_is_target(self):
        # Boundary condition: The last element is at an odd index and is even.
        # Odd indices with even elements: lst[1]=2, lst[3]=4, lst[5]=8
        self.assertEqual(add([1, 2, 3, 4, 5, 8]), 14)

    def test_boundary_last_element_not_target(self):
        # Boundary condition: The last element is at an odd index but is odd.
        # Odd indices with even elements: lst[1]=2, lst[3]=4
        self.assertEqual(add([1, 2, 3, 4, 5, 7]), 6)

    def test_long_list_with_duplicates_and_zeros(self):
        # Extreme input: A longer list with various numbers, including duplicates and zeros.
        # Odd indices with even elements: lst[1]=20, lst[3]=40, lst[5]=60, lst[7]=80, lst[9]=100, lst[11]=-2
        self.assertEqual(add([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, -2]), 298)

if __name__ == '__main__':
    unittest.main()