import unittest
from sut.problem_HumanEval_71 import triangle_area

class Test_triangle_area(unittest.TestCase):
    def test_normal_right_angled_integer_sides(self):
        # A standard right-angled triangle.
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0, places=2)

    def test_normal_right_angled_float_sides(self):
        # Another right-angled triangle with float inputs.
        self.assertAlmostEqual(triangle_area(5.0, 12.0, 13.0), 30.0, places=2)

    def test_normal_scalene_triangle(self):
        # A scalene triangle with non-integer area, rounded to two decimal places.
        self.assertAlmostEqual(triangle_area(7, 8, 9), 26.83, places=2)

    def test_normal_equilateral_triangle(self):
        # An equilateral triangle, area rounded.
        self.assertAlmostEqual(triangle_area(5, 5, 5), 10.83, places=2)

    def test_edge_invalid_triangle_sum_less(self):
        # Invalid triangle: sum of two sides is less than the third (1+2 < 10).
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_edge_degenerate_triangle_sum_equal(self):
        # Degenerate triangle: sum of two sides equals the third (1+2 = 3), not strictly greater.
        self.assertEqual(triangle_area(1, 2, 3), -1)

    def test_edge_very_small_equilateral_triangle(self):
        # Very small valid equilateral triangle, area rounds to 0.00.
        self.assertAlmostEqual(triangle_area(0.1, 0.1, 0.1), 0.0, places=2)

    def test_edge_isosceles_triangle(self):
        # An isosceles triangle.
        self.assertAlmostEqual(triangle_area(5, 5, 6), 12.0, places=2)

    def test_error_non_numeric_input(self):
        # Non-numeric input for a side length.
        with self.assertRaises(TypeError):
            triangle_area("a", 4, 5)

    def test_invalid_negative_side_length(self):
        # Negative side length. This violates the positivity precondition, making it an invalid triangle, thus returning -1.
        self.assertEqual(triangle_area(-3, 4, 5), -1)

    def test_invalid_zero_side_length(self):
        # Zero side length. This violates the positivity precondition, making it an invalid triangle, thus returning -1.
        self.assertEqual(triangle_area(0, 4, 5), -1)