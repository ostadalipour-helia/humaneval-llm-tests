import unittest
from sut.problem_HumanEval_54 import same_chars

class Test_same_chars(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(same_chars(s0="eabcdzzzz", s1="dddzzzzzzzddeddabc"), True)

    def test_normal_case_2(self):
        self.assertEqual(same_chars(s0="abcd", s1="dddddddabc"), True)

    def test_normal_case_3(self):
        self.assertEqual(same_chars(s0="dddddddabc", s1="abcd"), True)

    def test_normal_case_4(self):
        self.assertEqual(same_chars(s0="eabcd", s1="dddddddabc"), False)

    def test_normal_case_5(self):
        self.assertEqual(same_chars(s0="abcd", s1="dddddddabce"), False)

    def test_edge_case_empty_strings(self):
        self.assertEqual(same_chars(s0="", s1=""), True)

    def test_edge_case_single_different_chars(self):
        self.assertEqual(same_chars(s0="a", s1="b"), False)

    def test_edge_case_one_empty(self):
        self.assertEqual(same_chars(s0="abc", s1=""), False)

    def test_edge_case_case_sensitive(self):
        self.assertEqual(same_chars(s0="aBc", s1="AbC"), False)

    def test_edge_case_digits(self):
        self.assertEqual(same_chars(s0="123", s1="321"), True)