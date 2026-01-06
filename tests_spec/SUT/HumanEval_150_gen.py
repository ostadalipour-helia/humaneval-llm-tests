import unittest
from sut.problem_HumanEval_150 import x_or_y

class Test_x_or_y(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(x_or_y(n=7, x=34, y=12), 34)

    def test_case_1(self):
        self.assertEqual(x_or_y(n=15, x=8, y=5), 5)

    def test_case_2(self):
        self.assertEqual(x_or_y(n=13, x="hello", y="world"), "hello")

    def test_case_3(self):
        self.assertEqual(x_or_y(n=9, x=True, y=False), False)

    def test_case_4(self):
        self.assertEqual(x_or_y(n=1, x=100, y=200), 200)

    def test_case_5(self):
        self.assertEqual(x_or_y(n=2, x=10, y=20), 10)

    def test_case_6(self):
        self.assertEqual(x_or_y(n=4, x=10, y=20), 20)

    def test_case_7(self):
        self.assertEqual(x_or_y(n=29, x=5.5, y=10.1), 5.5)

    def test_case_8(self):
        self.assertEqual(x_or_y(n=30, x=5.5, y=10.1), 10.1)

    def test_case_9(self):
        self.assertEqual(x_or_y(n=17, x=5, y=5), 5)