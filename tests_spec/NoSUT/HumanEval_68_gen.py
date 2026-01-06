import unittest
from sut.problem_HumanEval_68 import pluck

class Test_pluck(unittest.TestCase):
    def test_normal_smallest_even_middle(self):
        """Test case where the smallest even number is in the middle."""
        arr = [4, 2, 3]
        expected_output = [2, 1]
        self.assertEqual(pluck(arr), expected_output)

    def test_normal_smallest_even_first_occurrence(self):
        """Test case with multiple occurrences of the smallest even number, picking the first index."""
        arr = [5, 0, 3, 0, 4, 2]
        expected_output = [0, 1]
        self.assertEqual(pluck(arr), expected_output)

    def test_normal_ascending_even(self):
        """Test case with even numbers in ascending order."""
        arr = [2, 4, 6, 8, 10]
        expected_output = [2, 0]
        self.assertEqual(pluck(arr), expected_output)

    def test_edge_empty_array(self):
        """Test case with an empty input array."""
        arr = []
        expected_output = []
        self.assertEqual(pluck(arr), expected_output)

    def test_edge_no_even_numbers(self):
        """Test case where the array contains no even numbers."""
        arr = [1, 3, 5, 7]
        expected_output = []
        self.assertEqual(pluck(arr), expected_output)

    def test_edge_single_zero(self):
        """Test case with a single element array containing 0."""
        arr = [0]
        expected_output = [0, 0]
        self.assertEqual(pluck(arr), expected_output)

    def test_edge_zero_at_end(self):
        """Test case where 0 is the smallest even number and appears at the end."""
        arr = [1, 0]
        expected_output = [0, 1]
        self.assertEqual(pluck(arr), expected_output)

    def test_error_not_list(self):
        """Test case where the input is not a list."""
        with self.assertRaises(TypeError):
            pluck(None)

    def test_error_non_integer_float(self):
        """Test case where the array contains non-integer (float) elements."""
        arr = [1, 2.5, 3]
        with self.assertRaises(TypeError):
            pluck(arr)

    def test_error_negative_integer(self):
        """Test case where the array contains negative integer elements."""
        arr = [1, -2, 3]
        with self.assertRaises(ValueError):
            pluck(arr)

    def test_error_non_integer_string(self):
        """Test case where the array contains non-integer (string) elements."""
        arr = [1, 'a', 3]
        with self.assertRaises(TypeError):
            pluck(arr)