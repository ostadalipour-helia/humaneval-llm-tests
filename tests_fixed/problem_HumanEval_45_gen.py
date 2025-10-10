import unittest
from sut_llm.problem_HumanEval_45 import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_01_docstring_example(self):
        # Test with the example provided in the docstring
        self.assertEqual(triangle_area(5, 3), 7.5)

    def test_02_zero_base(self):
        # Boundary test: base is zero
        self.assertEqual(triangle_area(0, 10), 0.0)

    def test_03_zero_height(self):
        # Boundary test: height is zero
        self.assertEqual(triangle_area(10, 0), 0.0)

    def test_04_both_zero(self):
        # Edge case: both base and height are zero
        self.assertEqual(triangle_area(0, 0), 0.0)

    def test_05_small_positive_integers(self):
        # Typical input: small positive integers
        self.assertEqual(triangle_area(1, 1), 0.5)

    def test_06_floating_point_inputs(self):
        # Test with floating point numbers for base and height
        self.assertEqual(triangle_area(2.5, 4.0), 5.0)

    def test_07_large_numbers(self):
        # Extreme input: large numbers for base and height
        self.assertEqual(triangle_area(1000, 2000), 1_000_000.0)

    def test_08_very_small_positive_numbers(self):
        # Extreme input: very small positive numbers, close to zero
        self.assertAlmostEqual(triangle_area(0.1, 0.1), 0.005)

    def test_09_negative_base(self):
        # Unusual input: negative base (assuming direct mathematical calculation)
        self.assertEqual(triangle_area(-5, 3), -7.5)

    def test_10_negative_height(self):
        # Unusual input: negative height (assuming direct mathematical calculation)
        self.assertEqual(triangle_area(5, -3), -7.5)