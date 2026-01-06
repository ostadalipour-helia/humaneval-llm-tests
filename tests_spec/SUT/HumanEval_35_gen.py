import unittest
from sut.problem_HumanEval_35 import max_element

class Test_max_element(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_case_1(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_case_2(self):
        self.assertEqual(max_element([-10, -5, -1, -20]), -1)

    def test_case_3(self):
        self.assertEqual(max_element([7, 7, 7, 1, 7]), 7)

    def test_case_4(self):
        self.assertEqual(max_element([42]), 42)

    def test_case_5(self):
        self.assertEqual(max_element([5, 5, 5, 5]), 5)

    def test_case_6(self):
        self.assertEqual(max_element([0, 0, 0]), 0)

    def test_case_7(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_case_8(self):
        self.assertEqual(max_element([42]), 42)

    def test_case_9(self):
        self.assertEqual(max_element([5, 5, 5, 5]), 5)