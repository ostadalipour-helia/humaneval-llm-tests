import unittest
from sut.problem_HumanEval_59 import largest_prime_factor

class Test_largest_prime_factor(unittest.TestCase):

    def test_case_13195(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(13195)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2048(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(2048)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_100(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(100)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_60(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(60)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_81(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(81)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_210(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(210)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_999999(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(999999)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_13195_duplicate(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(13195)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2048_duplicate(self):
        with self.assertRaises(TypeError) as cm:
            largest_prime_factor(2048)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')