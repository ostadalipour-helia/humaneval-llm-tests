import unittest
import math
from sut_llm.problem_HumanEval_32 import find_zero

class TestFindZero(unittest.TestCase):

    def test_example_1_linear(self):
        # Test case from docstring: f(x) = 1 + 2x, expected root = -0.5
        # The find_zero function uses a tolerance of 1e-6.
        # For f(x) = 1 + 2x, the derivative f'(x) = 2.
        # When the bisection method finds a mid-point `m` such that `abs(poly(xs, m)) < tolerance`,
        # the error in `m` relative to the true root `x_0` can be approximated by `|m - x_0| approx |poly(xs, m) / f'(x_0)|`.
        # In this case, `|m - (-0.5)| < 1e-6 / 2 = 0.5e-6`.
        # This means the result is guaranteed to be accurate to at least 6 decimal places (i.e., the error is less than 0.0000005).
        # Therefore, `places=6` is the appropriate precision for the assertion.
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=6)

    def test_example_2_cubic(self):
        # Test case from docstring: f(x) = (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
        # Roots are 1, 2, 3. Docstring indicates 1.0 (the smallest root) is returned.
        # The find_zero function uses a tolerance of 1e-6, which implies an accuracy of approximately 0.5e-6.
        # Therefore, asserting up to 6 decimal places is appropriate.
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=6)

    def test_smallest_even_length(self):
        # Boundary test: Smallest valid list length (2 coefficients), f(x) = 1 + x, expected root = -1.0
        # The find_zero function uses an internal tolerance of 1e-6.
        # For f(x) = 1 + x, f'(x) = 1. If |f(x)| < 1e-6, then |x - x_true| is approximately |f(x)/f'(x_true)| < 1e-6.
        # Therefore, asserting to 6 decimal places (tolerance 0.5e-6) is appropriate.
        self.assertAlmostEqual(find_zero([1, 1]), -1.0, places=6)

    def test_zero_root(self):
        # Boundary test: Polynomial with a root at zero, f(x) = 0 + x = x, expected root = 0.0
        self.assertAlmostEqual(find_zero([0, 1]), 0.0, places=7)

    def test_all_negative_coefficients(self):
        # Sign test: All coefficients are negative, f(x) = -1 - x, expected root = -1.0
        # The find_zero function uses a tolerance of 1e-6.
        # The bisection method guarantees the root is within (high - low)/2, which is tolerance/2 = 5e-7.
        # assertAlmostEqual(..., places=6) checks for a difference less than 0.5 * 10^-6 = 5e-7.
        # This matches the precision of the find_zero function.
        self.assertAlmostEqual(find_zero([-1, -1]), -1.0, places=6)

    def test_larger_even_length_single_root(self):
        # Extreme input: Higher degree polynomial (length 6, degree 5), f(x) = 1 + x^5, expected root = -1.0
        self.assertAlmostEqual(find_zero([1, 0, 0, 0, 0, 1]), -1.0, places=7)

    def test_large_constant_term(self):
        # Extreme input: Polynomial with a large constant term, f(x) = 1000 + x, expected root = -1000.0
        # The find_zero function uses an internal tolerance of 1e-6.
        # assertAlmostEqual(a, b, places=N) checks if abs(a - b) < 0.5 * (10**-N).
        # For a function with 1e-6 tolerance, the result can be off by up to 1e-6.
        # To pass, we need 0.5 * (10**-N) to be greater than or equal to the expected error (e.g., 1e-6).
        # If N=5, 0.5 * (10**-5) = 5e-6, which is sufficient to cover a 1e-6 error.
        # The original 'places=7' implied a tolerance of 0.5 * 10**-7 = 5e-8, which was too strict.
        self.assertAlmostEqual(find_zero([1000, 1]), -1000.0, places=5)


    def test_zero_coefficients_in_middle(self):
        # Edge case: Polynomial with zero coefficients for intermediate powers, f(x) = 1 + 2x^3, expected root = (-0.5)^(1/3)
        # The find_zero function uses a tolerance of 1e-6, which means it's accurate to about 6 decimal places.
        # Therefore, the assertion should check for equality up to 6 decimal places.
        self.assertAlmostEqual(find_zero([1, 0, 0, 2]), -math.pow(0.5, 1/3), places=6)

    def test_very_small_coefficients(self):
        # Extreme input: Polynomial with a very small coefficient, f(x) = 0.001 + x, expected root = -0.001
        # The find_zero function uses a tolerance of 1e-6.
        # This means the result can be expected to be accurate to roughly 0.5 * 1e-6 = 5e-7.
        # assertAlmostEqual(..., places=6) checks for a difference less than 0.5 * 10^-6 = 5e-7.
        # This aligns with the algorithm's internal tolerance.
        self.assertAlmostEqual(find_zero([0.001, 1]), -0.001, places=6)