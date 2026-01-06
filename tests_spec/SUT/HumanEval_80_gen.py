import unittest
from sut.problem_HumanEval_80 import is_happy

class Test_is_happy(unittest.TestCase):

    def test_normal_case_abcd(self):
        self.assertEqual(is_happy("abcd"), True)

    def test_normal_case_adb(self):
        self.assertEqual(is_happy("adb"), True)

    def test_normal_case_abcde(self):
        self.assertEqual(is_happy("abcde"), True)

    def test_normal_case_xyzabc(self):
        self.assertEqual(is_happy("xyzabc"), True)

    def test_edge_case_short_a(self):
        self.assertEqual(is_happy("a"), False)

    def test_edge_case_short_aa(self):
        self.assertEqual(is_happy("aa"), False)

    def test_edge_case_empty(self):
        self.assertEqual(is_happy(""), False)

    def test_edge_case_repeating_aabb(self):
        self.assertEqual(is_happy("aabb"), False)

    def test_edge_case_repeating_xyy(self):
        self.assertEqual(is_happy("xyy"), False)

    def test_edge_case_repeating_aaa(self):
        self.assertEqual(is_happy("aaa"), False)