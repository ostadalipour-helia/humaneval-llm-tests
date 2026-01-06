import unittest
from sut.problem_HumanEval_158 import find_max

class Test_find_max(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(find_max(["name", "of", "string"]), ' ')

    def test_case_1(self):
        self.assertEqual(find_max(["name", "enam", "game"]), ' ')

    def test_case_2(self):
        self.assertEqual(find_max([]), ' ')

    def test_case_3(self):
        self.assertEqual(find_max(["hello"]), ' ')

    def test_case_4(self):
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), ' ')

    def test_case_5(self):
        self.assertEqual(find_max(["abc", "bca", "cab"]), ' ')

    def test_case_6(self):
        self.assertEqual(find_max(["apple", "banana", "apricot"]), ' ')

    def test_case_7(self):
        self.assertEqual(find_max(["Aa", "aA"]), ' ')

    def test_case_8(self):
        self.assertEqual(find_max(["apple", "banana", "apricot"]), ' ')

    def test_case_9(self):
        self.assertEqual(find_max(["Aa", "aA"]), ' ')