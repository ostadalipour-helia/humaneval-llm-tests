import unittest
from sut.problem_HumanEval_103 import rounded_avg

class Test_rounded_avg(unittest.TestCase):

    def test_normal_case_1_5(self):
        self.assertEqual(rounded_avg(n=1, m=5), '0b11')

    def test_normal_case_10_20(self):
        self.assertEqual(rounded_avg(n=10, m=20), '0b1111')

    def test_normal_case_20_33(self):
        self.assertEqual(rounded_avg(n=20, m=33), '0b11010')

    def test_n_greater_than_m(self):
        self.assertEqual(rounded_avg(n=7, m=5), -1)

    def test_n_equals_m_single_element(self):
        self.assertEqual(rounded_avg(n=1, m=1), '0b1')

    def test_rounding_half_to_even_2_3(self):
        self.assertEqual(rounded_avg(n=2, m=3), '0b10')

    def test_n_equals_m_another_case(self):
        self.assertEqual(rounded_avg(n=2, m=2), '0b10')

    def test_rounding_half_to_even_1_2(self):
        self.assertEqual(rounded_avg(n=1, m=2), '0b10')

    def test_rounding_half_to_even_3_4(self):
        self.assertEqual(rounded_avg(n=3, m=4), '0b100')

    def test_normal_case_3_5(self):
        self.assertEqual(rounded_avg(n=3, m=5), '0b100')