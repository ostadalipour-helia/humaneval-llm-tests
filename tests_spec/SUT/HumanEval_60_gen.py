import unittest
from sut.problem_HumanEval_60 import sum_to_n

class Test_sum_to_n(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=30)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=100)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=10)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=30)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=100)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            sum_to_n(n=10)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')