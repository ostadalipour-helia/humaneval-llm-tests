import unittest
from sut.problem_HumanEval_128 import prod_signs

class Test_prod_signs(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(TypeError):
            prod_signs("[1, 2, 2, -4]")

    def test_case_1(self):
        with self.assertRaises(TypeError):
            prod_signs("[0, 1]")

    def test_case_2(self):
        with self.assertRaises(TypeError):
            prod_signs("[1, 2, 3]")

    def test_case_3(self):
        with self.assertRaises(TypeError):
            prod_signs("[-1, -2, -3]")

    def test_case_4(self):
        with self.assertRaises(TypeError):
            prod_signs("[5, -2, 3, -1]")

    def test_case_5(self):
        with self.assertRaises(TypeError):
            prod_signs("[]")

    def test_case_6(self):
        with self.assertRaises(TypeError):
            prod_signs("[0]")

    def test_case_7(self):
        with self.assertRaises(TypeError):
            prod_signs("[1]")

    def test_case_8(self):
        with self.assertRaises(TypeError):
            prod_signs("[-1]")

    def test_case_9(self):
        with self.assertRaises(TypeError):
            prod_signs("[0, 0, 0]")