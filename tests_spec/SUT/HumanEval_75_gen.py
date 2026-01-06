import unittest
from sut.problem_HumanEval_75 import is_multiply_prime

class Test_is_multiply_prime(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(is_multiply_prime(30), True)

    def test_case_2(self):
        self.assertEqual(is_multiply_prime(42), True)

    def test_case_3(self):
        self.assertEqual(is_multiply_prime(66), True)

    def test_case_4(self):
        self.assertEqual(is_multiply_prime(70), True)

    def test_case_5(self):
        self.assertEqual(is_multiply_prime(10), False)

    def test_case_6(self):
        self.assertEqual(is_multiply_prime(12), True)

    def test_case_7(self):
        self.assertEqual(is_multiply_prime(60), False)

    def test_case_8(self):
        self.assertEqual(is_multiply_prime(97), False)

    def test_case_9(self):
        self.assertEqual(is_multiply_prime(0), False)

    def test_case_10(self):
        self.assertEqual(is_multiply_prime(1), False)

    def test_case_11(self):
        self.assertEqual(is_multiply_prime(29), False)

    def test_case_12(self):
        self.assertEqual(is_multiply_prime(78), True)

    def test_case_13(self):
        self.assertEqual(is_multiply_prime(79), False)

    def test_case_14(self):
        self.assertEqual(is_multiply_prime(99), True)