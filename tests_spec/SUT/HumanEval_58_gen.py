import unittest
from sut.problem_HumanEval_58 import common

class Test_common(unittest.TestCase):

    def test_case_0(self):
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        expected = [1, 5, 653]
        self.assertEqual(common(l1, l2), expected)

    def test_case_1(self):
        l1 = [5, 3, 2, 8]
        l2 = [3, 2]
        expected = [2, 3]
        self.assertEqual(common(l1, l2), expected)

    def test_case_2(self):
        l1 = [10, 20, 30]
        l2 = [20, 40, 10]
        expected = [10, 20]
        self.assertEqual(common(l1, l2), expected)

    def test_case_3(self):
        l1 = []
        l2 = [1, 2, 3]
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_case_4(self):
        l1 = [1, 2, 3]
        l2 = []
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_case_5(self):
        l1 = []
        l2 = []
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_case_6(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        expected = []
        self.assertEqual(common(l1, l2), expected)

    def test_case_7(self):
        l1 = [1, 1, 2, 2, 3]
        l2 = [1, 2, 2, 4]
        expected = [1, 2]
        self.assertEqual(common(l1, l2), expected)

    def test_case_8(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(common(l1, l2), expected)

    def test_case_9(self):
        l1 = ['a', 'b', 'c']
        l2 = ['c', 'a', 'd']
        expected = ['a', 'c']
        self.assertEqual(common(l1, l2), expected)