import unittest
from sut.problem_HumanEval_87 import get_row

class TestGetRow(unittest.TestCase):

    def test_example_one(self):
        """
        Tests the first example from the docstring, covering multiple matches,
        multiple rows, and both sorting criteria (row ascending, col descending).
        """
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        x = 1
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_example_empty_list(self):
        """
        Tests the edge case of an empty input list `lst`.
        """
        lst = []
        x = 1
        expected = []
        self.assertListEqual(get_row(lst, x), expected)

    def test_example_ragged_list_single_match(self):
        """
        Tests a ragged list with empty sublists and a single match,
        verifying correct coordinate and sorting for a single result.
        """
        lst = [[], [1], [1, 2, 3]]
        x = 3
        expected = [(2, 2)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_no_match_found(self):
        """
        Tests the scenario where the target integer `x` is not present in the list.
        Should return an empty list.
        """
        lst = [[1, 2], [3, 4], [5, 6]]
        x = 7
        expected = []
        self.assertListEqual(get_row(lst, x), expected)

    def test_x_at_all_boundaries_and_middle(self):
        """
        Tests `x` at various boundary positions: (0,0), (last_row, last_col),
        and middle positions. Also tests multiple occurrences in one row
        and across rows, verifying both sorting criteria.
        """
        lst = [
            [7, 2, 7],
            [3, 7, 4],
            [7, 5, 6, 7]
        ]
        x = 7
        # Expected: (0,2), (0,0) | (1,1) | (2,3), (2,0)
        expected = [(0, 2), (0, 0), (1, 1), (2, 3), (2, 0)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_single_row_multiple_matches_descending_cols(self):
        """
        Focuses on the column descending sort within a single row,
        testing boundary conditions for columns (first, middle, last).
        """
        lst = [[10, 20, 10, 30, 10, 40, 10]]
        x = 10
        # Expected: (0,6), (0,4), (0,2), (0,0)
        expected = [(0, 6), (0, 4), (0, 2), (0, 0)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_all_elements_are_x(self):
        """
        Tests an extreme case where every element in the nested list is `x`.
        Verifies comprehensive iteration and correct coordinate generation and sorting.
        """
        lst = [
            [5, 5],
            [5, 5, 5],
            [5]
        ]
        x = 5
        # Expected: (0,1), (0,0) | (1,2), (1,1), (1,0) | (2,0)
        expected = [(0, 1), (0, 0), (1, 2), (1, 1), (1, 0), (2, 0)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_negative_and_zero_values(self):
        """
        Tests the function with negative numbers and zero for both `x` and list elements,
        ensuring correct handling of different numeric signs.
        """
        lst = [
            [-1, 0, -1],
            [5, -1, 0],
            [0, 0]
        ]
        x = -1
        # Expected: (0,2), (0,0) | (1,1)
        expected = [(0, 2), (0, 0), (1, 1)]
        self.assertListEqual(get_row(lst, x), expected)

    def test_ragged_list_with_empty_sublists_and_x_not_found(self):
        """
        Tests a ragged list containing empty sublists where `x` is not found.
        Ensures empty sublists are handled gracefully without errors.
        """
        lst = [[], [1, 2], [], [3, 4, 5], []]
        x = 6
        expected = []
        self.assertListEqual(get_row(lst, x), expected)

    def test_x_at_first_and_last_possible_positions_in_different_rows(self):
        """
        Tests `x` appearing at the very first column of the first row,
        and the very last column of a later row, and a single element row.
        Verifies correct row and column indexing and sorting.
        """
        lst = [
            [100, 2, 3],
            [4, 5, 100],
            [100]
        ]
        x = 100
        # Expected: (0,0) | (1,2) | (2,0)
        expected = [(0, 0), (1, 2), (2, 0)]
        self.assertListEqual(get_row(lst, x), expected)