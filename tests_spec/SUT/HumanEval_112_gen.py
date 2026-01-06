import unittest
from sut.problem_HumanEval_112 import reverse_delete

class Test_reverse_delete(unittest.TestCase):

    def test_case_1(self):
        s = "abcde"
        c = "ae"
        expected = ('bcd', False)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_2(self):
        s = "abcdef"
        c = "b"
        expected = ('acdef', False)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_3(self):
        s = "abcdedcba"
        c = "ab"
        expected = ('cdedc', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_4(self):
        s = "hello world"
        c = "o"
        expected = ('hell wrld', False)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_5(self):
        s = ""
        c = "abc"
        expected = ('', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_6(self):
        s = "abc"
        c = ""
        expected = ('abc', False)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_7(self):
        s = "racecar"
        c = "r"
        expected = ('aceca', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_8(self):
        s = "racecar"
        c = "e"
        expected = ('raccar', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_9(self):
        s = "abc"
        c = "abc"
        expected = ('', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_case_10(self):
        s = "abacaba"
        c = "b"
        expected = ('aacaa', True)
        self.assertEqual(reverse_delete(s, c), expected)