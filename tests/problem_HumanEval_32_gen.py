import unittest
import math
from sut.problem_HumanEval_32 import find_zero

class TestFindZero(unittest.TestCase):

    def test_example_1_linear(self):
        # Test case from docstring: f(x) = 1 + 2x, expected root = -0.5
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=7)

    def test_example_2_cubic(self):
        # Test case from docstring: f(x) = (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
        # Roots are 1, 2, 3. Docstring indicates 1.0 (the smallest root) is returned.
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=7)

    def test_smallest_even_length(self):
        # Boundary test: Smallest valid list length (2 coefficients), f(x) = 1 + x, expected root = -1.0
        self.assertAlmostEqual(find_zero([1, 1]), -1.0, places=7)

    def test_zero_root(self):
        # Boundary test: Polynomial with a root at zero, f(x) = 0 + x = x, expected root = 0.0
        self.assertAlmostEqual(find_zero([0, 1]), 0.0, places=7)

    def test_all_negative_coefficients(self):
        # Sign test: All coefficients are negative, f(x) = -1 - x, expected root = -1.0
        self.assertAlmostEqual(find_zero([-1, -1]), -1.0, places=7)

    def test_larger_even_length_single_root(self):
        # Extreme input: Higher degree polynomial (length 6, degree 5), f(x) = 1 + x^5, expected root = -1.0
        self.assertAlmostEqual(find_zero([1, 0, 0, 0, 0, 1]), -1.0, places=7)

    def test_large_constant_term(self):
        # Extreme input: Polynomial with a large constant term, f(x) = 1000 + x, expected root = -1000.0
        self.assertAlmostEqual(find_zero([1000, 1]), -1000.0, places=7)

    def test_multiple_negative_roots(self):
        # Logic mutation test: Polynomial with multiple negative roots, f(x) = (x+1)(x+2)(x+3) = 6 + 11x + 6x^2 + x^3
        # Roots are -1, -2, -3. Expecting the smallest root, -3.0, based on docstring example behavior.
        self.assertAlmostEqual(find_zero([6, 11, 6, 1]), -3.0, places=7)

    def test_zero_coefficients_in_middle(self):
        # Edge case: Polynomial with zero coefficients for intermediate powers, f(x) = 1 + 2x^3, expected root = (-0.5)^(1/3)
        self.assertAlmostEqual(find_zero([1, 0, 0, 2]), math.pow(-0.5, 1/3), places=7)

    def test_very_small_coefficients(self):
        # Extreme input: Polynomial with a very small coefficient, f(x) = 0.001 + x, expected root = -0.001
        self.assertAlmostEqual(find_zero([0.001, 1]), -0.001, places=7)