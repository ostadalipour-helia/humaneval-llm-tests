import unittest
from sut.problem_HumanEval_132 import is_nested

class Test_is_nested(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(is_nested('[[]]'), True)

    def test_case_2(self):
        self.assertEqual(is_nested('[[][]]'), True)

    def test_case_3(self):
        self.assertEqual(is_nested('[[]][['), True)

    def test_case_4(self):
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), True)

    def test_case_5(self):
        self.assertEqual(is_nested('[][]'), True)

    def test_case_6(self):
        self.assertEqual(is_nested(''), False)

    def test_case_7(self):
        self.assertEqual(is_nested('['), False)

    def test_case_8(self):
        self.assertEqual(is_nested(']'), False)

    def test_case_9(self):
        self.assertEqual(is_nested('[[['), False)

    def test_case_10(self):
        self.assertEqual(is_nested(']]'), False)