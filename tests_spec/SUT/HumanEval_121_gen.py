import unittest
from sut.problem_HumanEval_121 import solution

class Test_solution(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[5, 8, 7, 1])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 4 were given')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[3, 3, 3, 3, 3])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 5 were given')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[30, 13, 24, 321])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 4 were given')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[7])
        self.assertEqual(str(cm.exception), "'int' object is not iterable")

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[8])
        self.assertEqual(str(cm.exception), "'int' object is not iterable")

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[2, 4, 6, 8])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 4 were given')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[-1, 2, -3, 4, -5])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 5 were given')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            solution(*[0, 1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), 'solution() takes 1 positional argument but 6 were given')