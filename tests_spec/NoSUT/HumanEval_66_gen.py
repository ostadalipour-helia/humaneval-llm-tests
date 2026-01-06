import unittest
from sut.problem_HumanEval_66 import digitSum

class Test_digitSum(unittest.TestCase):
    def test_normal_mixed_case_abAB(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test_normal_mixed_case_abcCd(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_normal_mixed_case_aAaaaXa(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

    def test_edge_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_edge_no_uppercase_chars(self):
        self.assertEqual(digitSum("abcdefg"), 0)

    def test_edge_all_uppercase_chars(self):
        self.assertEqual(digitSum("ABCDEFG"), 504)

    def test_edge_non_alphabetic_chars(self):
        self.assertEqual(digitSum("123!@#$"), 0)

    def test_edge_complex_mixed_case(self):
        self.assertEqual(digitSum("MiXeD CaSe 123!"), 455)

    def test_error_input_integer(self):
        with self.assertRaises(TypeError):
            digitSum(123)

    def test_error_input_none(self):
        with self.assertRaises(AttributeError):
            digitSum(None)

    def test_error_input_list(self):
        with self.assertRaises(TypeError):
            digitSum(["a", "B"])