import unittest
from sut.problem_HumanEval_15 import string_sequence

class Test_string_sequence(unittest.TestCase):

    def test_case_n_5(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_3(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_0(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_1(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_5_again(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_3_again(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_0_again(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_1_again(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_5_third_time(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_n_0_third_time(self):
        with self.assertRaises(TypeError) as cm:
            string_sequence(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')