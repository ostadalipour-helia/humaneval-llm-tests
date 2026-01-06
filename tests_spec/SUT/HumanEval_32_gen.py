import unittest
from sut.problem_HumanEval_32 import find_zero

class Test_find_zero(unittest.TestCase):

    def test_normal_linear_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5000000000582077, delta=1e-9)

    def test_normal_cubic_polynomial(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 0.9999999999417923, delta=1e-9)

    def test_edge_linear_different_coeffs(self):
        self.assertAlmostEqual(find_zero([2, 1]), -2.0, delta=1e-9)

    def test_edge_zero_constant_term(self):
        self.assertAlmostEqual(find_zero([0.0, 1.0]), -5.820766091346741e-11, delta=1e-9)

    def test_edge_highest_degree_only(self):
        self.assertAlmostEqual(find_zero([0, 0, 0, 0, 0, 1]), -5.820766091346741e-11, delta=1e-9)

    def test_edge_cubic_with_negative_root(self):
        self.assertAlmostEqual(find_zero([1, 0, 0, 1]), -1.0, delta=1e-9)

    def test_edge_small_coefficients(self):
        self.assertAlmostEqual(find_zero([1e-09, 1e-09]), -1.0, delta=1e-9)