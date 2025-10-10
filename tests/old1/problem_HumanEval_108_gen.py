import unittest
from sut.problem_HumanEval_108 import count_nums

class TestCountNums(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_all_positive_sums_greater_than_zero(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_mixed_positive_negative_some_sums_greater_than_zero(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_all_negative_some_sums_greater_than_zero(self):
        # -123: -1+2+3 = 4 (>0)
        # -10: -1+0 = -1 (not >0)
        # -5: -5 (not >0)
        # -99: -9+9 = 0 (not >0)
        self.assertEqual(count_nums([-123, -10, -5, -99]), 1)

    def test_numbers_with_zero_sum_of_digits(self):
        # 10: 1+0 = 1 (>0)
        # -11: -1+1 = 0 (not >0)
        # 0: 0 (not >0)
        # 20: 2+0 = 2 (>0)
        self.assertEqual(count_nums([10, -11, 0, 20]), 2)

    def test_single_digit_numbers_positive_and_negative(self):
        # 5: 5 (>0)
        # -5: -5 (not >0)
        # 0: 0 (not >0)
        # 9: 9 (>0)
        # -9: -9 (not >0)
        self.assertEqual(count_nums([5, -5, 0, 9, -9]), 2)

    def test_large_numbers_mixed_signs(self):
        # 999: 9+9+9 = 27 (>0)
        # -999: -9+9+9 = 9 (>0)
        # 1000: 1+0+0+0 = 1 (>0)
        # -1000: -1+0+0+0 = -1 (not >0)
        self.assertEqual(count_nums([999, -999, 1000, -1000]), 3)

    def test_all_numbers_with_sum_less_than_or_equal_to_zero(self):
        # -1: -1 (not >0)
        # -2: -2 (not >0)
        # -10: -1+0 = -1 (not >0)
        # 0: 0 (not >0)
        # -11: -1+1 = 0 (not >0)
        self.assertEqual(count_nums([-1, -2, -10, 0, -11]), 0)

    def test_array_with_only_zero(self):
        self.assertEqual(count_nums([0]), 0)

    def test_multiple_digit_numbers_all_sums_greater_than_zero(self):
        # 12: 1+2 = 3 (>0)
        # -34: -3+4 = 1 (>0)
        # 56: 5+6 = 11 (>0)
        # -78: -7+8 = 1 (>0)
        # 90: 9+0 = 9 (>0)
        self.assertEqual(count_nums([12, -34, 56, -78, 90]), 5)

if __name__ == '__main__':
    unittest.main()