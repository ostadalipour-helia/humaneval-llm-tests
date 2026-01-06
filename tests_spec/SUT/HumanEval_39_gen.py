import unittest
from sut.problem_HumanEval_39 import prime_fib

class Test_prime_fib(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(prime_fib(n=1), 2)

    def test_case_2(self):
        self.assertEqual(prime_fib(n=2), 3)

    def test_case_3(self):
        self.assertEqual(prime_fib(n=3), 5)

    def test_case_4(self):
        self.assertEqual(prime_fib(n=4), 13)

    def test_case_5(self):
        self.assertEqual(prime_fib(n=5), 89)

    def test_case_6(self):
        self.assertEqual(prime_fib(n=1), 2)

    def test_case_7(self):
        self.assertEqual(prime_fib(n=1), 2)

    def test_case_8(self):
        self.assertEqual(prime_fib(n=2), 3)

    def test_case_9(self):
        self.assertEqual(prime_fib(n=3), 5)

    def test_case_10(self):
        self.assertEqual(prime_fib(n=4), 13)