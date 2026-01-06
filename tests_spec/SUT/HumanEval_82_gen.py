import unittest
from sut.problem_HumanEval_82 import prime_length

class Test_prime_length(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(prime_length('Hello'), True)

    def test_case_2(self):
        self.assertEqual(prime_length('abcdcba'), False)

    def test_case_3(self):
        self.assertEqual(prime_length('kittens'), False)

    def test_case_4(self):
        self.assertEqual(prime_length('orange'), False)

    def test_case_5(self):
        self.assertEqual(prime_length('python'), False)

    def test_case_6(self):
        self.assertEqual(prime_length('abc'), True)

    def test_case_7(self):
        self.assertEqual(prime_length(''), True)

    def test_case_8(self):
        self.assertEqual(prime_length('a'), True)

    def test_case_9(self):
        self.assertEqual(prime_length('ab'), False)

    def test_case_10(self):
        self.assertEqual(prime_length('abcdefghijklm'), False)