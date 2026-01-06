import unittest
from sut.problem_HumanEval_2 import truncate_number

class Test_truncate_number(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    def test_normal_case_2(self):
        self.assertAlmostEqual(truncate_number(1.234), 0.23399999999999999)

    def test_normal_case_3(self):
        self.assertAlmostEqual(truncate_number(10.0), 0.0)

    def test_normal_case_4(self):
        self.assertAlmostEqual(truncate_number(0.999), 0.999)

    def test_edge_case_small_positive(self):
        self.assertAlmostEqual(truncate_number(1e-06), 1e-06)

    def test_edge_case_one(self):
        self.assertAlmostEqual(truncate_number(1.0), 0.0)

    def test_edge_case_large_number(self):
        self.assertAlmostEqual(truncate_number(123456789.12345679), 0.12345679104328156)

    def test_error_negative_input(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_error_string_input(self):
        with self.assertRaises(TypeError):
            truncate_number("not_a_float")

    def test_error_null_input(self):
        with self.assertRaises(TypeError):
            truncate_number(None)