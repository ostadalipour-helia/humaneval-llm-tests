import unittest
from sut_llm.problem_HumanEval_68 import pluck

class TestPluck(unittest.TestCase):

    def test_example_1(self):
        # Basic case: smallest even value is unique
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_example_2(self):
        # Basic case: smallest even value with odd numbers present
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_example_3_empty_array(self):
        # Edge case: empty input array
        self.assertEqual(pluck([]), [])

    def test_example_4_multiple_smallest_even(self):
        # Tie-breaking: multiple occurrences of the smallest even value, pick smallest index
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_values(self):
        # Case: array contains only odd numbers
        self.assertEqual(pluck([1, 3, 5, 7, 9]), [])

    def test_single_even_element(self):
        # Edge case: array with a single even element
        self.assertEqual(pluck([6]), [6, 0])

    def test_single_odd_element(self):
        # Edge case: array with a single odd element
        self.assertEqual(pluck([7]), [])

    def test_all_even_values_descending(self):
        # Case: all values are even, smallest is at the end
        self.assertEqual(pluck([10, 8, 6, 4, 2]), [2, 4])

    def test_zero_at_start(self):
        # Case: zero is the smallest even value and at the beginning
        self.assertEqual(pluck([0, 1, 2, 3]), [0, 0])

    def test_larger_values_with_smallest_even(self):
        # Case: array with larger numbers, smallest even is 2
        self.assertEqual(pluck([100, 20, 500, 2, 10]), [2, 3])

if __name__ == '__main__':
    unittest.main()