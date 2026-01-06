import unittest
from sut.problem_HumanEval_76 import is_simple_power

class Test_is_simple_power(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(is_simple_power(x=1, n=4), True)

    def test_case_2(self):
        self.assertEqual(is_simple_power(x=2, n=2), True)

    def test_case_3(self):
        self.assertEqual(is_simple_power(x=8, n=2), True)

    def test_case_4(self):
        self.assertEqual(is_simple_power(x=3, n=2), False)

    def test_case_5(self):
        self.assertEqual(is_simple_power(x=5, n=3), False)

    def test_case_6(self):
        self.assertEqual(is_simple_power(x=27, n=3), True)

    def test_case_7(self):
        self.assertEqual(is_simple_power(x=100, n=10), True)

    def test_case_8(self):
        self.assertEqual(is_simple_power(x=1, n=1), True)

    def test_case_9(self):
        self.assertEqual(is_simple_power(x=3, n=1), False)

    def test_case_10(self):
        self.assertEqual(is_simple_power(x=7, n=7), True)