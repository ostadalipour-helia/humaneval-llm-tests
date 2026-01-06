import unittest
from sut.problem_HumanEval_69 import search

class Test_search(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError) as cm:
            search([4, 1, 2, 2, 3, 1])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_1(self):
        with self.assertRaises(TypeError) as cm:
            search([1, 2, 2, 3, 3, 3, 4, 4, 4])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_2(self):
        with self.assertRaises(TypeError) as cm:
            search([1, 1, 1, 1, 1])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_3(self):
        with self.assertRaises(TypeError) as cm:
            search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_4(self):
        with self.assertRaises(TypeError) as cm:
            search([1])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_5(self):
        with self.assertRaises(TypeError) as cm:
            search([2])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_6(self):
        with self.assertRaises(TypeError) as cm:
            search([5, 5, 4, 4, 4])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_7(self):
        with self.assertRaises(TypeError) as cm:
            search([1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_8(self):
        with self.assertRaises(TypeError) as cm:
            search([1, 1, 2, 2, 3, 3])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')

    def test_case_9(self):
        with self.assertRaises(TypeError) as cm:
            search([4, 1, 2, 2, 3, 1])
        self.assertEqual(str(cm.exception), 'can only concatenate str (not "int") to str')