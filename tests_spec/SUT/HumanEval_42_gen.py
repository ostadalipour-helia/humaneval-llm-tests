import unittest
from sut.problem_HumanEval_42 import incr_list

class Test_incr_list(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_case_2(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_case_3(self):
        self.assertEqual(incr_list([0, -1, 100]), [1, 0, 101])

    def test_case_4(self):
        self.assertEqual(incr_list([1.5, 2.0, 3.7]), [2.5, 3.0, 4.7])

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([7]), [8])

    def test_error_string_input(self):
        with self.assertRaises(TypeError):
            incr_list("not_a_list")

    def test_error_integer_input(self):
        with self.assertRaises(TypeError):
            incr_list(123)

    def test_error_none_input(self):
        with self.assertRaises(TypeError):
            incr_list(None)

    def test_error_non_numeric_element(self):
        with self.assertRaises(TypeError):
            incr_list([1, "a", 3])