import unittest
from sut.problem_HumanEval_32 import find_zero

class Test_find_zero(unittest.TestCase):

    def test_normal_linear_polynomial(self):
        # f(x) = 1 + 2x. The unique root is -0.5.
        xs = [1, 2]
        expected_output = -0.5
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_normal_cubic_polynomial(self):
        # f(x) = -6 + 11x - 6x^2 + x^3. Roots are 1.0, 2.0, 3.0.
        # The function returns one of them, specifically 1.0 in the example.
        xs = [-6, 11, -6, 1]
        expected_output = 1.0
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_edge_linear_zero_constant(self):
        # f(x) = x. The unique root is 0.0.
        xs = [0.0, 1.0]
        expected_output = 0.0
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_edge_high_degree_only_highest_term(self):
        # f(x) = x^5. The unique real root is 0.0.
        xs = [0, 0, 0, 0, 0, 1]
        expected_output = 0.0
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_edge_cubic_negative_root(self):
        # f(x) = 1 + x^3. The unique real root is -1.0.
        xs = [1, 0, 0, 1]
        expected_output = -1.0
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_edge_small_coefficients(self):
        # Linear polynomial with very small coefficients: f(x) = 1e-9 + 1e-9x.
        # The unique root is -1.0.
        xs = [1e-09, 1e-09]
        expected_output = -1.0
        result = find_zero(xs)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, expected_output, delta=1e-6)

    def test_error_xs_not_list(self):
        # `xs` is not a list.
        xs = "not a list"
        with self.assertRaises(TypeError):
            find_zero(xs)

    def test_error_xs_non_numeric_elements(self):
        # `xs` contains non-numeric elements.
        xs = [1, "a"]
        with self.assertRaises(TypeError):
            find_zero(xs)

    def test_error_xs_empty(self):
        # `xs` is empty, violating the minimum length and even length requirements.
        xs = []
        with self.assertRaises(ValueError):
            find_zero(xs)

    def test_error_xs_odd_length(self):
        # `xs` has an odd number of coefficients (length 1), violating the even length requirement.
        xs = [1]
        with self.assertRaises(ValueError):
            find_zero(xs)

    def test_error_xs_highest_coeff_zero_linear(self):
        # The highest degree coefficient (`xs[1]`) is zero, violating the precondition.
        xs = [0, 0]
        with self.assertRaises(ValueError):
            find_zero(xs)

    def test_error_xs_highest_coeff_zero_higher_degree(self):
        # The highest degree coefficient (`xs[3]`) is zero, violating the precondition.
        xs = [1, 2, 0, 0]
        with self.assertRaises(ValueError):
            find_zero(xs)