import unittest
from sut.problem_HumanEval_123 import get_odd_collatz

class TestGetOddCollatz(unittest.TestCase):

    def test_n_is_1(self):
        self.assertEqual(get_odd_collatz(1), [1])

    def test_n_is_5_example(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_n_is_2(self):
        self.assertEqual(get_odd_collatz(2), [1])

    def test_n_is_3(self):
        self.assertEqual(get_odd_collatz(3), [1, 3, 5])

    def test_n_is_4(self):
        self.assertEqual(get_odd_collatz(4), [1])

    def test_n_is_6(self):
        self.assertEqual(get_odd_collatz(6), [1, 3, 5])

    def test_n_is_7(self):
        self.assertEqual(get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_n_is_10(self):
        self.assertEqual(get_odd_collatz(10), [1, 5])

    def test_n_is_9(self):
        self.assertEqual(get_odd_collatz(9), [1, 5, 7, 9, 11, 13, 17])

    def test_n_is_13(self):
        self.assertEqual(get_odd_collatz(13), [1, 5, 13])

if __name__ == '__main__':
    unittest.main()