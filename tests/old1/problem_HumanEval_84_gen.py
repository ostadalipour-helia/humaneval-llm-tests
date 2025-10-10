import unittest
from sut.problem_HumanEval_84 import solve

class TestSolve(unittest.TestCase):

    def test_01_min_constraint(self):
        # N = 0, sum of digits = 0, binary of 0 is "0"
        self.assertEqual(solve(0), "0")

    def test_02_smallest_positive(self):
        # N = 1, sum of digits = 1, binary of 1 is "1"
        self.assertEqual(solve(1), "1")

    def test_03_example_1000(self):
        # N = 1000, sum of digits = 1, binary of 1 is "1"
        self.assertEqual(solve(1000), "1")

    def test_04_example_150(self):
        # N = 150, sum of digits = 6, binary of 6 is "110"
        self.assertEqual(solve(150), "110")

    def test_05_example_147(self):
        # N = 147, sum of digits = 12, binary of 12 is "1100"
        self.assertEqual(solve(147), "1100")

    def test_06_single_digit_max(self):
        # N = 9, sum of digits = 9, binary of 9 is "1001"
        self.assertEqual(solve(9), "1001")

    def test_07_two_digits_simple(self):
        # N = 25, sum of digits = 7, binary of 7 is "111"
        self.assertEqual(solve(25), "111")

    def test_08_two_digits_large_sum(self):
        # N = 99, sum of digits = 18, binary of 18 is "10010"
        self.assertEqual(solve(99), "10010")

    def test_09_three_digits_large_sum(self):
        # N = 999, sum of digits = 27, binary of 27 is "11011"
        self.assertEqual(solve(999), "11011")

    def test_10_max_constraint(self):
        # N = 10000, sum of digits = 1, binary of 1 is "1"
        self.assertEqual(solve(10000), "1")

if __name__ == '__main__':
    unittest.main()