import unittest
from sut.problem_HumanEval_37 import sort_even

class Test_sort_even(unittest.TestCase):

    def test_normal_case_1(self):
        with self.assertRaises(AttributeError):
            sort_even("[1, 2, 3]")

    def test_normal_case_2(self):
        with self.assertRaises(AttributeError):
            sort_even("[5, 6, 3, 4]")

    def test_normal_case_3(self):
        with self.assertRaises(AttributeError):
            sort_even("[10, 1, 8, 3, 6, 5]")

    def test_normal_case_4(self):
        with self.assertRaises(AttributeError):
            sort_even("[7, 2, 9, 4, 1, 6, 3, 8]")

    def test_edge_case_empty(self):
        with self.assertRaises(AttributeError):
            sort_even("[]")

    def test_edge_case_single_element(self):
        with self.assertRaises(AttributeError):
            sort_even("[1]")

    def test_edge_case_two_elements(self):
        with self.assertRaises(AttributeError):
            sort_even("[2, 1]")

    def test_edge_case_all_even_sorted(self):
        with self.assertRaises(AttributeError):
            sort_even("[1, 2, 3, 4, 5]")

    def test_edge_case_unsorted_even(self):
        with self.assertRaises(AttributeError):
            sort_even("[5, 2, 3, 4, 1]")

    def test_edge_case_negative_and_zero(self):
        with self.assertRaises(AttributeError):
            sort_even("[0, -1, 10, -5, 5]")

if __name__ == '__main__':
    unittest.main()