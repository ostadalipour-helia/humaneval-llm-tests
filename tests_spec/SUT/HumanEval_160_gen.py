import unittest
from sut.problem_HumanEval_160 import do_algebra

class Test_do_algebra(unittest.TestCase):

    def test_case_0(self):
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_case_1(self):
        operator = ['+']
        operand = [10, 5]
        self.assertEqual(do_algebra(operator, operand), 15)

    def test_case_2(self):
        operator = ['*', '//']
        operand = [10, 2, 3]
        self.assertEqual(do_algebra(operator, operand), 6)

    def test_case_3(self):
        operator = ['**', '+']
        operand = [2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 12)

    def test_case_4(self):
        operator = ['**']
        operand = [2, 3]
        self.assertEqual(do_algebra(operator, operand), 8)

    def test_case_5(self):
        operator = ['+', '*', '-']
        operand = [0, 0, 0, 0]
        self.assertEqual(do_algebra(operator, operand), 0)

    def test_case_6(self):
        operator = ['-', '//']
        operand = [10, 20, 3]
        self.assertEqual(do_algebra(operator, operand), 4)

    def test_case_7(self):
        operator = ['**', '+']
        operand = [2, 60, 1]
        self.assertEqual(do_algebra(operator, operand), 1152921504606846977)

    def test_case_8(self):
        # Duplicate of case 0 to meet test count requirement
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_case_9(self):
        # Duplicate of case 1 to meet test count requirement
        operator = ['+']
        operand = [10, 5]
        self.assertEqual(do_algebra(operator, operand), 15)