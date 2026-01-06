import unittest
from sut.problem_HumanEval_87 import get_row

class Test_get_row(unittest.TestCase):

    def test_multiple_occurrences_sorted(self):
        """
        Normal case: Multiple occurrences of x across different rows and columns,
        requiring both sorting criteria (row ascending, column descending).
        """
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        x = 1
        # Expected output based on sorting: (0,0), (1,4), (1,0), (2,5), (2,0)
        expected_output = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, x), expected_output)

    def test_single_occurrence_middle(self):
        """
        Normal case: x appears exactly once in the middle of the matrix.
        """
        lst = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        x = 50
        expected_output = [(1, 1)]
        self.assertEqual(get_row(lst, x), expected_output)

    def test_x_not_present(self):
        """
        Normal case: x is not present in the list.
        """
        lst = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        x = 0
        expected_output = []
        self.assertEqual(get_row(lst, x), expected_output)

    def test_empty_lst(self):
        """
        Edge case: Empty input list `lst`.
        """
        lst = []
        x = 1
        expected_output = []
        self.assertEqual(get_row(lst, x), expected_output)

    def test_lst_with_empty_rows(self):
        """
        Edge case: Input list `lst` contains empty rows and `x` is found in a non-empty row.
        """
        lst = [
            [],
            [1],
            [1, 2, 3]
        ]
        x = 3
        expected_output = [(2, 2)]
        self.assertEqual(get_row(lst, x), expected_output)

    def test_all_elements_are_x(self):
        """
        Edge case: All elements in `lst` are `x`, testing comprehensive sorting.
        """
        lst = [
            [7, 7, 7],
            [7, 7, 7]
        ]
        x = 7
        # Expected output based on sorting: (0,2), (0,1), (0,0), (1,2), (1,1), (1,0)
        expected_output = [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]
        self.assertEqual(get_row(lst, x), expected_output)

    def test_lst_not_a_list_type_error(self):
        """
        Error case: `lst` is not a list.
        """
        lst = "not a list"
        x = 1
        with self.assertRaises(TypeError):
            get_row(lst, x)

    def test_inner_element_not_list_type_error(self):
        """
        Error case: An element of `lst` is not a list.
        """
        lst = [
            [1, 2],
            "not a list",
            [3, 4]
        ]
        x = 1
        with self.assertRaises(TypeError):
            get_row(lst, x)

    def test_innermost_element_not_int_type_error(self):
        """
        Error case: An element within an inner list is not an integer.
        """
        lst = [
            [1, 2],
            [3, "a"]
        ]
        x = 1
        with self.assertRaises(TypeError):
            get_row(lst, x)

    def test_x_not_an_int_type_error(self):
        """
        Error case: `x` is not an integer.
        """
        lst = [
            [1, 2],
            [3, 4]
        ]
        x = "not an int"
        with self.assertRaises(TypeError):
            get_row(lst, x)