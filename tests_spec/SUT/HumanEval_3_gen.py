import unittest
from sut.problem_HumanEval_3 import below_zero

class Test_below_zero(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(below_zero(operations=[1, 2, 3]), False)

    def test_case_1(self):
        self.assertEqual(below_zero(operations=[1, 2, -4, 5]), True)

    def test_case_2(self):
        self.assertEqual(below_zero(operations=[10, -5, -3, 2]), False)

    def test_case_3(self):
        self.assertEqual(below_zero(operations=[-1, 5, -3]), True)

    def test_case_4(self):
        self.assertEqual(below_zero(operations=[]), False)

    def test_case_5(self):
        self.assertEqual(below_zero(operations=[0]), False)

    def test_case_6(self):
        self.assertEqual(below_zero(operations=[-1]), True)

    def test_case_7(self):
        self.assertEqual(below_zero(operations=[10, -10]), False)

    def test_case_8(self):
        self.assertEqual(below_zero(operations=[10, -10, -1]), True)

    def test_case_9(self):
        self.assertEqual(below_zero(operations=[5, 0, -3, -3]), True)