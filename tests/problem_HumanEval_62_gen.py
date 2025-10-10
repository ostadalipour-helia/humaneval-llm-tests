import unittest
from sut.problem_HumanEval_62 import derivative

class TestDerivative(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical case from docstring, verifies general functionality
        self.assertListEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_docstring_example_2(self):
        # Another typical case from docstring, verifies general functionality
        self.assertListEqual(derivative([1, 2, 3]), [2, 6])

    def test_edge_case_empty_list(self):
        # Boundary condition: Empty polynomial (no coefficients)
        self.assertListEqual(derivative([]), [])

    def test_edge_case_single_element_list(self):
        # Boundary condition: Constant polynomial (e.g., P(x) = 7), derivative is 0
        self.assertListEqual(derivative([7]), [])

    def test_boundary_two_elements_linear_polynomial(self):
        # Boundary condition: Linear polynomial (e.g., P(x) = 10 - 3x)
        # Tests the smallest input that yields a non-empty derivative
        self.assertListEqual(derivative([10, -3]), [-3])

    def test_negative_coefficients(self):
        # Sign testing: Polynomial with all negative coefficients
        self.assertListEqual(derivative([-1, -2, -3, -4]), [-2, -6, -12])

    def test_zero_coefficients(self):
        # Sign testing: Polynomial with some zero coefficients, including the constant term
        # Catches issues with multiplication by zero or incorrect index handling
        self.assertListEqual(derivative([5, 0, 3, 0, 1]), [0, 6, 0, 4])

    def test_large_coefficients(self):
        # Extreme input: Polynomial with large coefficients
        # Verifies correct arithmetic with larger numbers
        self.assertListEqual(derivative([1000, 2000, 3000]), [2000, 6000])

    def test_mixed_coefficients(self):
        # Logic mutation: Polynomial with a mix of positive, negative, and zero coefficients
        # Ensures the derivative logic handles all types of coefficients correctly
        self.assertListEqual(derivative([1, -2, 0, 4, -5]), [-2, 0, 12, -20])

    def test_all_same_non_zero_coefficients(self):
        # Edge case: All coefficients are the same non-zero value (e.g., P(x) = 7 + 7x + 7x^2 + 7x^3)
        # Checks if the multiplication by index (k) is correctly applied for each term
        self.assertListEqual(derivative([7, 7, 7, 7]), [7, 14, 21])