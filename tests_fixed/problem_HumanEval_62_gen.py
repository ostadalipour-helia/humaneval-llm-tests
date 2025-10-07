import unittest
from sut_llm.problem_HumanEval_62 import derivative

class TestDerivative(unittest.TestCase):

    def test_01_docstring_example_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_02_docstring_example_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_03_constant_polynomial(self):
        # Derivative of a constant (e.g., 5) is 0.
        # Based on examples, the output list length is len(input) - 1.
        # So for [5], len=1, output len=0, which is [].
        self.assertEqual(derivative([5]), [])

    def test_04_linear_polynomial(self):
        # Derivative of 2 + 3x is 3.
        self.assertEqual(derivative([2, 3]), [3])

    def test_05_polynomial_with_zero_middle_coefficient(self):
        # Derivative of 1 + 0x + 2x^2 is 0 + 4x, represented as [0, 4].
        self.assertEqual(derivative([1, 0, 2]), [0, 4])

    def test_06_polynomial_with_negative_coefficients(self):
        # Derivative of 1 - 2x + 3x^2 is -2 + 6x.
        self.assertEqual(derivative([1, -2, 3]), [-2, 6])

    def test_07_polynomial_with_fractional_coefficients(self):
        # Derivative of 0.5 + 1.5x + 2.5x^2 is 1.5 + 5.0x.
        self.assertEqual(derivative([0.5, 1.5, 2.5]), [1.5, 5.0])

    def test_08_empty_polynomial(self):
        # An empty list represents a polynomial with no terms (effectively 0).
        # Its derivative should also be represented as an empty list.
        self.assertEqual(derivative([]), [])

    def test_09_polynomial_with_leading_zero_coefficients(self):
        # Derivative of 0 + 0x + 5x^2 is 0 + 10x, represented as [0, 10].
        self.assertEqual(derivative([0, 0, 5]), [0, 10])

    def test_10_polynomial_with_multiple_zero_coefficients(self):
        # Derivative of 1 + 0x + 0x^2 + 4x^3 is 0 + 0x + 12x^2, represented as [0, 0, 12].
        self.assertEqual(derivative([1, 0, 0, 4]), [0, 0, 12])

if __name__ == '__main__':
    unittest.main()