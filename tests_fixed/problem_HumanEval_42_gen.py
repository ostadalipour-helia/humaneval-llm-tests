import unittest
from sut_llm.problem_HumanEval_42 import incr_list

class TestIncrList(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertListEqual(incr_list([]), [])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertListEqual(incr_list([1]), [2])

    def test_docstring_example_1(self):
        """Test with the first example from the docstring."""
        self.assertListEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_docstring_example_2(self):
        """Test with the second example from the docstring."""
        self.assertListEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_list_with_zero(self):
        """Test with a list containing zero, a boundary value."""
        self.assertListEqual(incr_list([0]), [1])

    def test_list_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertListEqual(incr_list([-1, -5, 0]), [0, -4, 1])

    def test_list_with_large_numbers(self):
        """Test with a list containing very large numbers."""
        self.assertListEqual(incr_list([999999, 1000000]), [1000000, 1000001])

    def test_list_with_all_same_values(self):
        """Test with a list where all elements are identical."""
        self.assertListEqual(incr_list([7, 7, 7, 7]), [8, 8, 8, 8])

    def test_list_with_mixed_values_and_duplicates(self):
        """Test with a list containing a mix of positive, negative, zero, and duplicate values."""
        self.assertListEqual(incr_list([0, -1, 1, 0, -1, 100]), [1, 0, 2, 1, 0, 101])

    def test_list_with_single_large_positive_number(self):
        """Test with a single large positive number, checking boundary for magnitude."""
        self.assertListEqual(incr_list([10**9]), [10**9 + 1])

if __name__ == '__main__':
    unittest.main()