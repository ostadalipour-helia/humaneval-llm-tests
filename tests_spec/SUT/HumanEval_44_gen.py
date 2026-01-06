import unittest
from sut.problem_HumanEval_44 import change_base

class Test_change_base(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(change_base(x=8, base=3), '22')

    def test_case_2(self):
        self.assertEqual(change_base(x=8, base=2), '1000')

    def test_case_3(self):
        self.assertEqual(change_base(x=7, base=2), '111')

    def test_case_4(self):
        self.assertEqual(change_base(x=15, base=8), '17')

    def test_case_5(self):
        self.assertEqual(change_base(x=0, base=2), '')

    def test_case_6(self):
        self.assertEqual(change_base(x=0, base=9), '')

    def test_case_7(self):
        self.assertEqual(change_base(x=1, base=2), '1')

    def test_case_8(self):
        self.assertEqual(change_base(x=9, base=9), '10')

    def test_case_9(self):
        self.assertEqual(change_base(x=10, base=9), '11')

    def test_case_10(self):
        self.assertEqual(change_base(x=5, base=7), '5')