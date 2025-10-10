import unittest
from sut_llm.problem_HumanEval_71 import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_example_valid_triangle(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.00)

    def test_example_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_equilateral_triangle(self):
        self.assertAlmostEqual(triangle_area(5, 5, 5), 10.83)

    def test_isosceles_triangle(self):
        self.assertAlmostEqual(triangle_area(5, 5, 8), 12.00)

    def test_another_right_angled_triangle(self):
        self.assertAlmostEqual(triangle_area(5, 12, 13), 30.00)

    def test_degenerate_triangle(self):
        self.assertEqual(triangle_area(1, 2, 3), -1)

    def test_invalid_triangle_one_side_too_long(self):
        self.assertEqual(triangle_area(2, 3, 6), -1)

    def test_scalene_triangle(self):
        self.assertAlmostEqual(triangle_area(7, 8, 9), 26.83)

    def test_invalid_triangle_with_zero_side(self):
        self.assertEqual(triangle_area(0, 4, 5), -1)

    def test_invalid_triangle_with_negative_side(self):
        self.assertEqual(triangle_area(-3, 4, 5), -1)