import unittest
from sut.problem_HumanEval_20 import find_closest_elements

class Test_find_closest_elements(unittest.TestCase):

    def test_normal_case_distinct_closest(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[1.0, 2.0, 3.0, 4.0, 5.0, 2.2]")

    def test_normal_case_not_adjacent(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[10.0, 1.0, 5.0, 8.0]")

    def test_normal_case_at_beginning(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[0.1, 0.2, 0.3, 0.4]")

    def test_edge_case_identical_elements(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[1.0, 2.0, 3.0, 4.0, 5.0, 2.0]")

    def test_edge_case_two_elements(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[5.0, 1.0]")

    def test_edge_case_negative_numbers(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[-1.0, -2.0, -1.5]")

    def test_edge_case_all_identical(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[3.0, 3.0, 3.0, 3.0]")

    def test_edge_case_high_precision(self):
        with self.assertRaises(TypeError):
            find_closest_elements("[1.234567, 1.234568, 1.0]")

    def test_error_none_input(self):
        with self.assertRaises(TypeError):
            find_closest_elements(None)

    def test_error_mixed_types(self):
        with self.assertRaises(TypeError):
            find_closest_elements([1.0, '2.0', 3.0])