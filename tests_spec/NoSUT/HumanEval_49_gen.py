import unittest
from sut.problem_HumanEval_49 import modp

class Test_modp(unittest.TestCase):
    def test_normal_case_2_pow_3_mod_5(self):
        # 2^3 mod 5 = 8 mod 5 = 3
        self.assertEqual(modp(3, 5), 3)

    def test_normal_case_large_exponent(self):
        # 2^1101 mod 101 = 2 (large exponent)
        self.assertEqual(modp(1101, 101), 2)

    def test_normal_case_2_pow_3_mod_11(self):
        # 2^3 mod 11 = 8 mod 11 = 8
        self.assertEqual(modp(3, 11), 8)

    def test_edge_case_exponent_is_zero(self):
        # Exponent is zero: 2^0 mod 101 = 1 mod 101 = 1
        self.assertEqual(modp(0, 101), 1)

    def test_edge_case_fermat_little_theorem(self):
        # Fermat's Little Theorem case: 2^(p-1) mod p = 1 for prime p (101 is prime)
        self.assertEqual(modp(100, 101), 1)

    def test_edge_case_modulo_by_2(self):
        # Modulo by 2: 2^5 mod 2 = 32 mod 2 = 0
        self.assertEqual(modp(5, 2), 0)

    def test_edge_case_2_pow_n_less_than_p(self):
        # 2^n < p
        self.assertEqual(modp(2, 5), 4)

    def test_error_n_is_negative(self):
        # n must be non-negative. Negative exponents are not supported for this modular exponentiation.
        with self.assertRaises(ValueError):
            modp(-1, 5)

    def test_error_p_is_zero(self):
        # p must be greater than 1. Modulo by zero is undefined.
        with self.assertRaises(ZeroDivisionError):
            modp(3, 0)

    def test_error_p_is_one(self):
        # p must be greater than 1. Modulo by 1 always yields 0, but is typically excluded from standard modular exponentiation definitions.
        with self.assertRaises(ValueError):
            modp(3, 1)

    def test_error_n_is_not_integer(self):
        # n must be an integer.
        with self.assertRaises(TypeError):
            modp("abc", 5)

    def test_error_p_is_not_integer(self):
        # p must be an integer.
        with self.assertRaises(TypeError):
            modp(3, "xyz")