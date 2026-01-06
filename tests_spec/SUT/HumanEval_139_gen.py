import unittest
from sut.problem_HumanEval_139 import special_factorial

class Test_special_factorial(unittest.TestCase):

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_10(self):
        with self.assertRaises(TypeError) as cm:
            special_factorial(5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')