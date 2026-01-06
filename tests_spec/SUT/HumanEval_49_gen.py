import unittest
from sut.problem_HumanEval_49 import modp

class Test_modp(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(modp(n=3, p=5), 3)

    def test_normal_case_large_exponent(self):
        self.assertEqual(modp(n=1101, p=101), 2)

    def test_normal_case_2(self):
        self.assertEqual(modp(n=3, p=11), 8)

    def test_edge_case_zero_exponent(self):
        self.assertEqual(modp(n=0, p=101), 1)

    def test_edge_case_fermats_little_theorem(self):
        self.assertEqual(modp(n=100, p=101), 1)

    def test_edge_case_mod_by_2(self):
        self.assertEqual(modp(n=5, p=2), 0)

    def test_edge_case_small_values(self):
        self.assertEqual(modp(n=1, p=3), 2)

    def test_edge_case_power_less_than_modulus(self):
        self.assertEqual(modp(n=2, p=5), 4)

    def test_error_modulus_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modp(n=3, p=0)

    def test_error_exponent_not_integer(self):
        with self.assertRaises(TypeError):
            modp(n="abc", p=5)