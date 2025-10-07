import unittest
from sut_llm.problem_HumanEval_150 import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_n_is_2(self):
        self.assertEqual(x_or_y(2, 10, 20), 10)

    def test_prime_n_is_3(self):
        self.assertEqual(x_or_y(3, 50, 5), 50)

    def test_prime_n_is_7_from_example(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_prime_n_is_17(self):
        self.assertEqual(x_or_y(17, 100, 1), 100)

    def test_not_prime_n_is_4(self):
        self.assertEqual(x_or_y(4, 10, 20), 20)

    def test_not_prime_n_is_6(self):
        self.assertEqual(x_or_y(6, 50, 5), 5)

    def test_not_prime_n_is_15_from_example(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_not_prime_n_is_1(self):
        self.assertEqual(x_or_y(1, 99, 11), 11)

    def test_not_prime_n_is_0(self):
        self.assertEqual(x_or_y(0, 77, 22), 22)

    def test_not_prime_n_is_25(self):
        self.assertEqual(x_or_y(25, 1000, 100), 100)