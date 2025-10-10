import unittest
from sut.problem_HumanEval_130 import tri

class TestTri(unittest.TestCase):

    def test_0_n_equals_zero_edge_case(self):
        # Edge case: n=0, should return the first 0+1 = 1 number.
        # Based on tri(3) = [1, 3, 2, 8], the 0-th term is 1.
        self.assertListEqual(tri(0), [1])

    def test_1_n_equals_one_base_case(self):
        # Edge case: n=1, should return the first 1+1 = 2 numbers.
        # T_0 = 1, T_1 = 3 (given tri(1)=3)
        self.assertListEqual(tri(1), [1, 3])

    def test_2_n_equals_two_even_rule(self):
        # Boundary/Typical: n=2, uses even rule T_2 = 1 + 2/2 = 2.
        # T_0 = 1, T_1 = 3, T_2 = 2
        self.assertListEqual(tri(2), [1, 3, 2])

    def test_3_n_equals_three_odd_rule_example(self):
        # Boundary/Typical: n=3, uses odd rule T_3 = T_2 + T_1 + T_4.
        # T_0 = 1, T_1 = 3, T_2 = 2, T_3 = 8 (given example)
        self.assertListEqual(tri(3), [1, 3, 2, 8])

    def test_4_n_equals_four_even_rule_example(self):
        # Boundary/Typical: n=4, uses even rule T_4 = 3 (given example).
        # T_0 = 1, T_1 = 3, T_2 = 2, T_3 = 8, T_4 = 3
        self.assertListEqual(tri(4), [1, 3, 2, 8, 3])

    def test_5_n_equals_five_odd_rule_deeper(self):
        # Logic mutation: n=5, odd rule T_5 = T_4 + T_3 + T_6.
        # T_6 = 1 + 6/2 = 4. So T_5 = 3 + 8 + 4 = 15.
        # Sequence: [1, 3, 2, 8, 3, 15]
        self.assertListEqual(tri(5), [1, 3, 2, 8, 3, 15])

    def test_6_n_equals_six_even_rule_deeper(self):
        # Logic mutation: n=6, even rule T_6 = 1 + 6/2 = 4.
        # Sequence: [1, 3, 2, 8, 3, 15, 4]
        self.assertListEqual(tri(6), [1, 3, 2, 8, 3, 15, 4])

    def test_7_n_equals_seven_extreme_odd(self):
        # Extreme input: n=7, odd rule T_7 = T_6 + T_5 + T_8.
        # T_8 = 1 + 8/2 = 5. So T_7 = 4 + 15 + 5 = 24.
        # Sequence: [1, 3, 2, 8, 3, 15, 4, 24]
        self.assertListEqual(tri(7), [1, 3, 2, 8, 3, 15, 4, 24])

    def test_8_n_equals_eight_extreme_even(self):
        # Extreme input: n=8, even rule T_8 = 1 + 8/2 = 5.
        # Sequence: [1, 3, 2, 8, 3, 15, 4, 24, 5]
        self.assertListEqual(tri(8), [1, 3, 2, 8, 3, 15, 4, 24, 5])

    def test_9_n_equals_nine_extreme_odd_further(self):
        # Extreme input: n=9, odd rule T_9 = T_8 + T_7 + T_10.
        # T_10 = 1 + 10/2 = 6. So T_9 = 5 + 24 + 6 = 35.
        # Sequence: [1, 3, 2, 8, 3, 15, 4, 24, 5, 35]
        self.assertListEqual(tri(9), [1, 3, 2, 8, 3, 15, 4, 24, 5, 35])