import unittest
from sut.problem_HumanEval_137 import compare_one

class Test_compare_one(unittest.TestCase):

    # Normal Cases
    def test_normal_float_larger(self):
        a = 1
        b = 2.5
        self.assertEqual(compare_one(a, b), 2.5)

    def test_normal_string_comma_larger(self):
        a = 1
        b = "2,3"
        self.assertEqual(compare_one(a, b), "2,3")

    def test_normal_int_larger(self):
        a = 10
        b = 5
        self.assertEqual(compare_one(a, b), 10)

    def test_normal_string_dot_larger(self):
        a = "10.5"
        b = "9.2"
        self.assertEqual(compare_one(a, b), "10.5")

    # Edge Cases
    def test_edge_equal_string_int(self):
        a = "1"
        b = 1
        self.assertIsNone(compare_one(a, b))

    def test_edge_equal_float_int(self):
        a = 5.0
        b = 5
        self.assertIsNone(compare_one(a, b))

    def test_edge_negative_int_larger(self):
        a = -1
        b = -2
        self.assertEqual(compare_one(a, b), -1)

    def test_edge_negative_string_vs_int(self):
        a = "-1.5"
        b = -1
        self.assertEqual(compare_one(a, b), -1)

    def test_edge_equal_zero_float_int(self):
        a = 0
        b = 0.0
        self.assertIsNone(compare_one(a, b))

    # Error Cases
    def test_error_invalid_string_a(self):
        a = "abc"
        b = 1
        with self.assertRaises(ValueError):
            compare_one(a, b)

    def test_error_invalid_type_b(self):
        a = 1
        b = [2]
        with self.assertRaises(TypeError):
            compare_one(a, b)

    def test_error_invalid_separator_a(self):
        a = "1;2"
        b = 3
        with self.assertRaises(ValueError):
            compare_one(a, b)