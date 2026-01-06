import unittest
import sut.problem_HumanEval_45 as mod

class TestHybrid(unittest.TestCase):
    def test_01_docstring_example(self):
            # Test with the example provided in the docstring
            self.assertEqual(mod.triangle_area(5, 3), 7.5)

    def test_02_zero_base(self):
            # Boundary test: base is zero
            self.assertEqual(mod.triangle_area(0, 10), 0.0)

    def test_03_zero_height(self):
            # Boundary test: height is zero
            self.assertEqual(mod.triangle_area(10, 0), 0.0)

    def test_04_both_zero(self):
            # Edge case: both base and height are zero
            self.assertEqual(mod.triangle_area(0, 0), 0.0)

    def test_05_small_positive_integers(self):
            # Typical input: small positive integers
            self.assertEqual(mod.triangle_area(1, 1), 0.5)

    def test_06_floating_point_inputs(self):
            # Test with floating point numbers for base and height
            self.assertEqual(mod.triangle_area(2.5, 4.0), 5.0)

    def test_07_large_numbers(self):
            # Extreme input: large numbers for base and height
            self.assertEqual(mod.triangle_area(1000, 2000), 1_000_000.0)

    def test_09_negative_base(self):
            # Unusual input: negative base (assuming direct mathematical calculation)
            self.assertEqual(mod.triangle_area(-5, 3), -7.5)

    def test_10_negative_height(self):
            # Unusual input: negative height (assuming direct mathematical calculation)
            self.assertEqual(mod.triangle_area(5, -3), -7.5)

    def test_normal_integer_inputs(self):
            # Example from docstring with integer inputs.
            a = 5
            h = 3
            expected_output = 7.5
            result = mod.triangle_area(a, h)
            self.assertEqual(result, expected_output)
            self.assertIsInstance(result, float)

    def test_normal_float_inputs(self):
            # Inputs are floats.
            a = 10.0
            h = 4.0
            expected_output = 20.0
            result = mod.triangle_area(a, h)
            self.assertEqual(result, expected_output)
            self.assertIsInstance(result, float)

    def test_normal_mixed_inputs(self):
            # Mixed integer and float inputs.
            a = 7
            h = 2.5
            expected_output = 8.75
            result = mod.triangle_area(a, h)
            self.assertEqual(result, expected_output)
            self.assertIsInstance(result, float)

    def test_edge_smallest_positive_integers(self):
            # Smallest positive integer inputs.
            a = 1
            h = 1
            expected_output = 0.5
            result = mod.triangle_area(a, h)
            self.assertEqual(result, expected_output)
            self.assertIsInstance(result, float)

    def test_edge_smallest_positive_floats(self):
            # Smallest positive float inputs.
            a = 0.1
            h = 0.1
            expected_output = 0.005
            result = mod.triangle_area(a, h)
            self.assertAlmostEqual(result, expected_output) # Use assertAlmostEqual for small floats
            self.assertIsInstance(result, float)

    def test_edge_large_inputs(self):
            # Large integer inputs.
            a = 1000000
            h = 1000000
            expected_output = 500000000000.0
            result = mod.triangle_area(a, h)
            self.assertEqual(result, expected_output)
            self.assertIsInstance(result, float)

    def test_error_non_numeric_side(self):
            # Side length is not a number. Precondition: a is a number.
            with self.assertRaises(TypeError):
                mod.triangle_area('abc', 3)

    def test_error_none_side(self):
            # Side length is None. Precondition: a is a number.
            with self.assertRaises(TypeError):
                mod.triangle_area(None, 3)

