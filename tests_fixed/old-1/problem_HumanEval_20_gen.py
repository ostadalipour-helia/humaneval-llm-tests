import unittest
from sut_llm.problem_HumanEval_20 import find_closest_elements

class TestFindClosestElements(unittest.TestCase):

    def test_docstring_example_1(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        expected = (2.0, 2.2)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_docstring_example_2_duplicates(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        expected = (2.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_two_elements_simple(self):
        numbers = [1.0, 2.0]
        expected = (1.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_three_elements_first_pair_closest(self):
        numbers = [1.0, 1.1, 2.0]
        expected = (1.0, 1.1)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_three_elements_last_pair_closest(self):
        numbers = [1.0, 2.0, 2.1]
        expected = (2.0, 2.1)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_three_elements_non_adjacent_closest(self):
        numbers = [1.0, 5.0, 1.1]
        expected = (1.0, 1.1)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_negative_numbers(self):
        numbers = [-1.0, -2.0, -1.1]
        expected = (-1.1, -1.0)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_mixed_positive_negative_numbers(self):
        numbers = [-5.0, 0.0, 5.0, 0.1]
        expected = (0.0, 0.1)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_numbers_with_many_decimal_places(self):
        numbers = [0.123, 0.124, 0.500]
        expected = (0.123, 0.124)
        self.assertEqual(find_closest_elements(numbers), expected)

    def test_multiple_pairs_same_min_diff(self):
        # If multiple pairs have the same minimum non-zero difference,
        # the problem statement doesn't specify tie-breaking.
        # A common deterministic approach is to return the pair that appears first
        # when iterating or the one with the smallest first element after sorting.
        # We'll assume (1.0, 2.0) is a valid output for this case.
        numbers = [1.0, 2.0, 3.0, 4.0]
        expected = (1.0, 2.0)
        self.assertEqual(find_closest_elements(numbers), expected)

if __name__ == '__main__':
    unittest.main()