import unittest
import sut.problem_HumanEval_62 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Typical case from docstring, verifies general functionality
            self.assertListEqual(mod.derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_docstring_example_2(self):
            # Another typical case from docstring, verifies general functionality
            self.assertListEqual(mod.derivative([1, 2, 3]), [2, 6])

    def test_edge_case_empty_list(self):
            # Boundary condition: Empty polynomial (no coefficients)
            self.assertListEqual(mod.derivative([]), [])

    def test_edge_case_single_element_list(self):
            # Boundary condition: Constant polynomial (e.g., P(x) = 7), derivative is 0
            self.assertListEqual(mod.derivative([7]), [])

    def test_boundary_two_elements_linear_polynomial(self):
            # Boundary condition: Linear polynomial (e.g., P(x) = 10 - 3x)
            # Tests the smallest input that yields a non-empty derivative
            self.assertListEqual(mod.derivative([10, -3]), [-3])

    def test_negative_coefficients(self):
            # Sign testing: Polynomial with all negative coefficients
            self.assertListEqual(mod.derivative([-1, -2, -3, -4]), [-2, -6, -12])

    def test_zero_coefficients(self):
            # Sign testing: Polynomial with some zero coefficients, including the constant term
            # Catches issues with multiplication by zero or incorrect index handling
            self.assertListEqual(mod.derivative([5, 0, 3, 0, 1]), [0, 6, 0, 4])

    def test_large_coefficients(self):
            # Extreme input: Polynomial with large coefficients
            # Verifies correct arithmetic with larger numbers
            self.assertListEqual(mod.derivative([1000, 2000, 3000]), [2000, 6000])

    def test_mixed_coefficients(self):
            # Logic mutation: Polynomial with a mix of positive, negative, and zero coefficients
            # Ensures the derivative logic handles all types of coefficients correctly
            self.assertListEqual(mod.derivative([1, -2, 0, 4, -5]), [-2, 0, 12, -20])

    def test_all_same_non_zero_coefficients(self):
            # Edge case: All coefficients are the same non-zero value (e.g., P(x) = 7 + 7x + 7x^2 + 7x^3)
            # Checks if the multiplication by index (k) is correctly applied for each term
            self.assertListEqual(mod.derivative([7, 7, 7, 7]), [7, 14, 21])

    def test_normal_case_1(self):
            # Polynomial 3 + x + 2x^2 + 4x^3 + 5x^4, derivative is 1 + 4x + 12x^2 + 20x^3.
            xs = [3, 1, 2, 4, 5]
            expected_output = [1, 4, 12, 20]
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_normal_case_2(self):
            # Polynomial 1 + 2x + 3x^2, derivative is 2 + 6x.
            xs = [1, 2, 3]
            expected_output = [2, 6]
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_normal_case_zero_polynomial(self):
            # Derivative of the zero polynomial (up to x^3) is the zero polynomial (up to x^2).
            xs = [0, 0, 0, 0]
            expected_output = [0, 0, 0]
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_normal_case_float_coefficients(self):
            # Polynomial with float coefficients.
            xs = [1.0, 2.5, 3.0, 0.5]
            expected_output = [2.5, 6.0, 1.5]
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_edge_case_constant_polynomial(self):
            # Derivative of a constant polynomial (e.g., 5) is 0, represented by an empty list.
            xs = [5]
            expected_output = []
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_edge_case_zero_constant_polynomial(self):
            # Derivative of the zero constant polynomial (0) is 0, represented by an empty list.
            xs = [0]
            expected_output = []
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_edge_case_trailing_zeros(self):
            # Polynomial 1 + 0x + 0x^2, derivative is 0 + 0x.
            xs = [1, 0, 0]
            expected_output = [0, 0]
            self.assertEqual(mod.derivative(xs), expected_output)

    def test_error_case_input_none(self):
            # Input `xs` is not a list.
            with self.assertRaises(TypeError):
                mod.derivative(None)

    def test_error_case_input_not_list(self):
            # Input `xs` is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.derivative(123)

    def test_error_case_non_numeric_element_none(self):
            # Input list `xs` contains non-numeric elements (None).
            with self.assertRaises(TypeError):
                mod.derivative([1, None, 3])

