import unittest
from sut.problem_HumanEval_45 import triangle_area

class Test_triangle_area(unittest.TestCase):

    def test_normal_integer_inputs(self):
        # Example from docstring with integer inputs.
        a = 5
        h = 3
        expected_output = 7.5
        result = triangle_area(a, h)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

    def test_normal_float_inputs(self):
        # Inputs are floats.
        a = 10.0
        h = 4.0
        expected_output = 20.0
        result = triangle_area(a, h)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

    def test_normal_mixed_inputs(self):
        # Mixed integer and float inputs.
        a = 7
        h = 2.5
        expected_output = 8.75
        result = triangle_area(a, h)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

    def test_edge_smallest_positive_integers(self):
        # Smallest positive integer inputs.
        a = 1
        h = 1
        expected_output = 0.5
        result = triangle_area(a, h)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

    def test_edge_smallest_positive_floats(self):
        # Smallest positive float inputs.
        a = 0.1
        h = 0.1
        expected_output = 0.005
        result = triangle_area(a, h)
        self.assertAlmostEqual(result, expected_output) # Use assertAlmostEqual for small floats
        self.assertIsInstance(result, float)

    def test_edge_large_inputs(self):
        # Large integer inputs.
        a = 1000000
        h = 1000000
        expected_output = 500000000000.0
        result = triangle_area(a, h)
        self.assertEqual(result, expected_output)
        self.assertIsInstance(result, float)

    def test_error_zero_side(self):
        # Side length is zero. Precondition: a > 0.
        with self.assertRaises(ValueError):
            triangle_area(0, 5)

    def test_error_zero_height(self):
        # Height is zero. Precondition: h > 0.
        with self.assertRaises(ValueError):
            triangle_area(5, 0)

    def test_error_negative_side(self):
        # Side length is negative. Precondition: a > 0.
        with self.assertRaises(ValueError):
            triangle_area(-5, 3)

    def test_error_negative_height(self):
        # Height is negative. Precondition: h > 0.
        with self.assertRaises(ValueError):
            triangle_area(5, -3)

    def test_error_non_numeric_side(self):
        # Side length is not a number. Precondition: a is a number.
        with self.assertRaises(TypeError):
            triangle_area('abc', 3)

    def test_error_none_side(self):
        # Side length is None. Precondition: a is a number.
        with self.assertRaises(TypeError):
            triangle_area(None, 3)