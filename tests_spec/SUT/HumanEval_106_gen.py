import unittest
from sut.problem_HumanEval_106 import f

class Test_f(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            f(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            f(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            f(n=2)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            f(n=4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            f(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            f(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            f(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            f(n=2)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            f(n=4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            f(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')