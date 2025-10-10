import unittest
from sut_llm.problem_HumanEval_73 import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical input, multiple changes needed
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)

    def test_docstring_example_2(self):
        # Typical input, odd length, one change needed
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_docstring_example_3_already_palindrome(self):
        # Typical input, already a palindrome, odd length
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_empty_array(self):
        # Edge case: empty array
        self.assertEqual(smallest_change([]), 0)

    def test_single_element_array(self):
        # Edge case: single element array
        self.assertEqual(smallest_change([5]), 0)

    def test_even_length_all_different(self):
        # Boundary case: even length array, all elements need changing
        self.assertEqual(smallest_change([1, 2, 3, 4]), 2)

    def test_odd_length_all_different(self):
        # Boundary case: odd length array, all outer pairs need changing, middle ignored
        self.assertEqual(smallest_change([1, 2, 3, 4, 5]), 2)

    def test_even_length_already_palindrome(self):
        # Boundary case: even length array, already a palindrome
        self.assertEqual(smallest_change([1, 2, 2, 1]), 0)

    def test_with_negative_and_zero_values(self):
        # Extreme/unusual input: array with negative and zero values, one change needed
        self.assertEqual(smallest_change([-1, 0, 1, 0, -2]), 1)

    def test_large_array_half_changes(self):
        # Extreme/unusual input: large array where all pairs are different
        # This tests loop boundaries and performance for larger inputs
        arr = list(range(50)) + list(range(50, 100)) # [0, 1, ..., 49, 50, ..., 99]
        self.assertEqual(smallest_change(arr), 50)

if __name__ == '__main__':
    unittest.main()