import unittest
from sut.problem_HumanEval_66 import digitSum

class Test_digitSum(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test_normal_case_2(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_normal_case_3(self):
        self.assertEqual(digitSum("helloE"), 69)

    def test_normal_case_4(self):
        self.assertEqual(digitSum("woArBld"), 131)

    def test_normal_case_5(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

    def test_edge_case_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_edge_case_no_uppercase(self):
        self.assertEqual(digitSum("abcdefg"), 0)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(digitSum("ABCDEFG"), 476)

    def test_edge_case_non_alphabetic(self):
        self.assertEqual(digitSum("123!@#$"), 0)

    def test_edge_case_mixed_string(self):
        self.assertEqual(digitSum("MiXeD CaSe 123!"), 383)