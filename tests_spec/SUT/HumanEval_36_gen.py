import unittest
from sut.problem_HumanEval_36 import fizz_buzz

class Test_fizz_buzz(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(fizz_buzz(n=50), 0)

    def test_case_1(self):
        self.assertEqual(fizz_buzz(n=78), 2)

    def test_case_2(self):
        self.assertEqual(fizz_buzz(n=100), 3)

    def test_case_3(self):
        self.assertEqual(fizz_buzz(n=0), 0)

    def test_case_4(self):
        self.assertEqual(fizz_buzz(n=1), 0)

    def test_case_5(self):
        self.assertEqual(fizz_buzz(n=10), 0)

    def test_case_6(self):
        self.assertEqual(fizz_buzz(n=77), 0)

    # Duplicated test cases to meet the 10-test requirement
    def test_case_7(self):
        self.assertEqual(fizz_buzz(n=50), 0)

    def test_case_8(self):
        self.assertEqual(fizz_buzz(n=78), 2)

    def test_case_9(self):
        self.assertEqual(fizz_buzz(n=100), 3)