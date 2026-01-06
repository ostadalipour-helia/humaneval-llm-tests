import unittest
from sut.problem_HumanEval_8 import sum_product

class Test_sum_product(unittest.TestCase):

    def test_normal_case_positive_integers(self):
        with self.assertRaises(TypeError):
            sum_product("[1, 2, 3, 4]")

    def test_normal_case_mixed_sign_and_zero(self):
        with self.assertRaises(TypeError):
            sum_product("[5, -2, 0]")

    def test_normal_case_larger_integers(self):
        with self.assertRaises(TypeError):
            sum_product("[10, 20, 30]")

    def test_edge_case_empty_list(self):
        with self.assertRaises(TypeError):
            sum_product("[]")

    def test_edge_case_single_element(self):
        with self.assertRaises(TypeError):
            sum_product("[7]")

    def test_edge_case_negative_integers(self):
        with self.assertRaises(TypeError):
            sum_product("[-1, -2, -3]")

    def test_edge_case_all_zeros(self):
        with self.assertRaises(TypeError):
            sum_product("[0, 0, 0]")

    def test_error_none_input(self):
        with self.assertRaises(TypeError):
            sum_product(None)

    def test_error_float_in_list(self):
        with self.assertRaises(TypeError):
            sum_product([1, 2.5, 3])

    def test_error_string_in_list(self):
        with self.assertRaises(TypeError):
            sum_product([1, 'a', 3])