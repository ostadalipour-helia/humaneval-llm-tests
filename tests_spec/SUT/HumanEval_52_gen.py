import unittest
from sut.problem_HumanEval_52 import below_threshold

class Test_below_threshold(unittest.TestCase):

    def test_case_0(self):
        l = [1, 2, 4, 10]
        t = 100
        expected = True
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_1(self):
        l = [1, 20, 4, 10]
        t = 5
        expected = False
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_2(self):
        l = [-5, 0, 3]
        t = 10
        expected = True
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_3(self):
        l = []
        t = 5
        expected = True
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_4(self):
        l = [5, 5, 5]
        t = 5
        expected = False
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_5(self):
        l = [4.9, 4.99, 4.999]
        t = 5
        expected = True
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_6(self):
        l = [5.0, 5.1, 6]
        t = 5
        expected = False
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_7(self):
        l = [10]
        t = 10
        expected = False
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_8(self):
        l = [9]
        t = 10
        expected = True
        self.assertEqual(below_threshold(l, t), expected)

    def test_case_9(self):
        l = [1, 2, 3]
        t = -1
        expected = False
        self.assertEqual(below_threshold(l, t), expected)