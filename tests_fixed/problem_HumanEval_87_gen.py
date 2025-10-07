import unittest
from sut_llm.problem_HumanEval_87 import get_row

class TestGetRow(unittest.TestCase):

    def test_example_1(self):
        # Example from docstring: multiple occurrences, different rows, specific sorting
        lst = [
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ]
        x = 1
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_example_2_empty_list(self):
        # Example from docstring: empty input list
        lst = []
        x = 1
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_example_3_mixed_rows(self):
        # Example from docstring: empty inner list, single element inner list, x found once
        lst = [[], [1], [1, 2, 3]]
        x = 3
        expected = [(2, 2)]
        self.assertEqual(get_row(lst, x), expected)

    def test_x_not_found(self):
        # x is not present in the list
        lst = [[1,2,3],[4,5,6]]
        x = 7
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_single_occurrence_single_row(self):
        # x found once in a single-row list
        lst = [[10, 20, 30, 40]]
        x = 20
        expected = [(0, 1)]
        self.assertEqual(get_row(lst, x), expected)

    def test_multiple_occurrences_same_row_different_rows(self):
        # x found multiple times in the same row and different rows, testing sorting
        lst = [[1, 2, 1], [3, 1, 4, 1], [5, 6]]
        x = 1
        # Expected: (0,2), (0,0) then (1,3), (1,1)
        expected = [(0, 2), (0, 0), (1, 3), (1, 1)]
        self.assertEqual(get_row(lst, x), expected)

    def test_x_at_boundaries_of_rows(self):
        # x found at the beginning and end of rows
        lst = [[7, 8, 7], [7, 9, 10, 7]]
        x = 7
        # Expected: (0,2), (0,0) then (1,3), (1,0)
        expected = [(0, 2), (0, 0), (1, 3), (1, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_all_elements_are_x(self):
        # All elements in the list are x
        lst = [[5, 5], [5, 5, 5], [5]]
        x = 5
        # Expected: (0,1), (0,0) then (1,2), (1,1), (1,0) then (2,0)
        expected = [(0, 1), (0, 0), (1, 2), (1, 1), (1, 0), (2, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_list_with_only_empty_rows(self):
        # Input list contains only empty inner lists
        lst = [[], [], []]
        x = 1
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_x_is_zero(self):
        # Test with x being 0 and list containing 0s
        lst = [[0, 1, 0], [2, 0], [0]]
        x = 0
        # Expected: (0,2), (0,0) then (1,1) then (2,0)
        expected = [(0, 2), (0, 0), (1, 1), (2, 0)]
        self.assertEqual(get_row(lst, x), expected)

if __name__ == '__main__':
    unittest.main()