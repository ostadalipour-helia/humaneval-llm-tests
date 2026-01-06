import unittest
from sut.problem_HumanEval_42 import incr_list

class Test_incr_list(unittest.TestCase):

    def test_normal_positive_integers(self):
        l = [1, 2, 3]
        expected = [2, 3, 4]
        self.assertEqual(incr_list(l), expected)

    def test_normal_mixed_integers(self):
        l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
        self.assertEqual(incr_list(l), expected)

    def test_normal_zero_negative_integers(self):
        l = [0, -1, 100]
        expected = [1, 0, 101]
        self.assertEqual(incr_list(l), expected)

    def test_normal_float_numbers(self):
        l = [1.5, 2.0, 3.7]
        expected = [2.5, 3.0, 4.7]
        self.assertEqual(incr_list(l), expected)

    def test_edge_empty_list(self):
        l = []
        expected = []
        self.assertEqual(incr_list(l), expected)

    def test_edge_single_element_list(self):
        l = [7]
        expected = [8]
        self.assertEqual(incr_list(l), expected)

    def test_error_non_list_string_input(self):
        l = "not_a_list"
        with self.assertRaises(TypeError):
            incr_list(l)

    def test_error_non_list_integer_input(self):
        l = 123
        with self.assertRaises(TypeError):
            incr_list(l)

    def test_error_non_list_null_input(self):
        l = None
        with self.assertRaises(TypeError):
            incr_list(l)

    def test_error_list_with_non_numeric_string(self):
        l = [1, "a", 3]
        with self.assertRaises(TypeError):
            incr_list(l)

    def test_error_list_with_non_numeric_null(self):
        l = [1, None, 3]
        with self.assertRaises(TypeError):
            incr_list(l)