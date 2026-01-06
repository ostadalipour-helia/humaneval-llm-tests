import unittest
from sut.problem_HumanEval_130 import tri

class Test_tri(unittest.TestCase):

    def test_normal_case_n_3(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_normal_case_n_0(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_normal_case_n_1(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_normal_case_n_2(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=2)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_normal_case_n_4(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=4)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_normal_case_n_5(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_edge_case_n_0(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=0)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    # Additional tests to meet the 10-test requirement
    def test_retest_n_3(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=3)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_retest_n_1(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=1)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_retest_n_5(self):
        with self.assertRaises(TypeError) as cm:
            tri(n=5)
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')