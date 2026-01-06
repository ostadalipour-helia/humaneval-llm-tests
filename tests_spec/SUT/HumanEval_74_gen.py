import unittest
from sut.problem_HumanEval_74 import total_match

class Test_total_match(unittest.TestCase):

    def test_case_1(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hI', 'Hi']
        expected = ['hI', 'Hi']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_2(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hi', 'hi', 'admin', 'project']
        expected = ['hi', 'admin']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_3(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hI', 'hi', 'hi']
        expected = ['hI', 'hi', 'hi']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_4(self):
        lst1 = ['4']
        lst2 = ['1', '2', '3', '4', '5']
        expected = ['4']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_5(self):
        lst1 = []
        lst2 = []
        expected = []
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_6(self):
        lst1 = ['a']
        lst2 = ['b']
        expected = ['a']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_7(self):
        lst1 = ['longstring']
        lst2 = ['short']
        expected = ['short']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_8(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hI', 'Hi']
        expected = ['hI', 'Hi']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_9(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hi', 'hi', 'admin', 'project']
        expected = ['hi', 'admin']
        self.assertEqual(total_match(lst1, lst2), expected)

    def test_case_10(self):
        lst1 = ['hi', 'admin']
        lst2 = ['hI', 'hi', 'hi']
        expected = ['hI', 'hi', 'hi']
        self.assertEqual(total_match(lst1, lst2), expected)