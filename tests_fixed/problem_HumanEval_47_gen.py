import unittest
from sut_llm.problem_HumanEval_47 import median

class TestMedianFunction(unittest.TestCase):

    def test_docstring_example_1_odd_length(self):
        """Test with the first example from the docstring (odd length list)."""
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_docstring_example_2_even_length(self):
        """Test with the second example from the docstring (even length list, float result)."""
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 8.0)

    def test_single_element_list_boundary(self):
        """Test with a list containing a single element (smallest odd length)."""
        self.assertEqual(median([7]), 7)

    def test_two_element_list_boundary(self):
        """Test with a list containing two elements (smallest even length)."""
        self.assertEqual(median([10, 20]), 15.0)

    def test_odd_length_negative_numbers(self):
        """Test with an odd length list containing only negative numbers."""
        self.assertEqual(median([-5, -1, -3]), -3)

    def test_even_length_negative_numbers(self):
        """Test with an even length list containing only negative numbers."""
        self.assertEqual(median([-10, -20, -30, -40]), -25.0)

    def test_list_with_zero_and_mixed_signs(self):
        """Test with a list containing zero and mixed positive/negative numbers."""
        self.assertEqual(median([-5, 0, 5]), 0)

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate values."""
        self.assertEqual(median([1, 5, 2, 5, 3]), 3)

    def test_list_all_same_values(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(median([7, 7, 7, 7]), 7.0)

    def test_larger_even_list_mixed_values(self):
        """Test with a larger even length list with mixed values to check index calculation."""
        # Sorted: [0, 1, 2, 3, 4, 50, 99, 100]
        # Middle elements: 3, 4. Median: (3+4)/2 = 3.5
        self.assertEqual(median([100, 1, 50, 2, 99, 3, 4, 0]), 3.5)

if __name__ == '__main__':
    unittest.main()