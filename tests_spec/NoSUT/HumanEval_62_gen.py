import unittest
from sut.problem_HumanEval_62 import derivative

class Test_derivative(unittest.TestCase):
    def test_normal_case_1(self):
        # Polynomial 3 + x + 2x^2 + 4x^3 + 5x^4, derivative is 1 + 4x + 12x^2 + 20x^3.
        xs = [3, 1, 2, 4, 5]
        expected_output = [1, 4, 12, 20]
        self.assertEqual(derivative(xs), expected_output)

    def test_normal_case_2(self):
        # Polynomial 1 + 2x + 3x^2, derivative is 2 + 6x.
        xs = [1, 2, 3]
        expected_output = [2, 6]
        self.assertEqual(derivative(xs), expected_output)

    def test_normal_case_zero_polynomial(self):
        # Derivative of the zero polynomial (up to x^3) is the zero polynomial (up to x^2).
        xs = [0, 0, 0, 0]
        expected_output = [0, 0, 0]
        self.assertEqual(derivative(xs), expected_output)

    def test_normal_case_float_coefficients(self):
        # Polynomial with float coefficients.
        xs = [1.0, 2.5, 3.0, 0.5]
        expected_output = [2.5, 6.0, 1.5]
        self.assertEqual(derivative(xs), expected_output)

    def test_edge_case_constant_polynomial(self):
        # Derivative of a constant polynomial (e.g., 5) is 0, represented by an empty list.
        xs = [5]
        expected_output = []
        self.assertEqual(derivative(xs), expected_output)

    def test_edge_case_zero_constant_polynomial(self):
        # Derivative of the zero constant polynomial (0) is 0, represented by an empty list.
        xs = [0]
        expected_output = []
        self.assertEqual(derivative(xs), expected_output)

    def test_edge_case_empty_list(self):
        # Derivative of an empty list (representing the zero polynomial) is an empty list.
        xs = []
        expected_output = []
        self.assertEqual(derivative(xs), expected_output)

    def test_edge_case_trailing_zeros(self):
        # Polynomial 1 + 0x + 0x^2, derivative is 0 + 0x.
        xs = [1, 0, 0]
        expected_output = [0, 0]
        self.assertEqual(derivative(xs), expected_output)

    def test_error_case_input_none(self):
        # Input `xs` is not a list.
        with self.assertRaises(TypeError):
            derivative(None)

    def test_error_case_input_not_list(self):
        # Input `xs` is an integer, not a list.
        with self.assertRaises(TypeError):
            derivative(123)

    def test_error_case_non_numeric_element_string(self):
        # Input list `xs` contains non-numeric elements.
        with self.assertRaises(TypeError):
            derivative([1, 'a', 3])

    def test_error_case_non_numeric_element_none(self):
        # Input list `xs` contains non-numeric elements (None).
        with self.assertRaises(TypeError):
            derivative([1, None, 3])