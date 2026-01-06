import unittest
from sut.problem_HumanEval_71 import triangle_area

class Test_triangle_area(unittest.TestCase):

    def test_normal_right_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.0)

    def test_normal_right_triangle_with_floats(self):
        self.assertEqual(triangle_area(5.0, 12.0, 13.0), 30.0)

    def test_normal_scalene_triangle(self):
        self.assertEqual(triangle_area(7, 8, 9), 26.83)

    def test_normal_equilateral_triangle(self):
        self.assertEqual(triangle_area(5, 5, 5), 10.83)

    def test_edge_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_edge_degenerate_triangle(self):
        self.assertEqual(triangle_area(1, 2, 3), -1)

    def test_edge_small_valid_triangle(self):
        self.assertEqual(triangle_area(0.1, 0.1, 0.1), 0.0)

    def test_edge_isosceles_triangle(self):
        self.assertEqual(triangle_area(5, 5, 6), 12.0)

    def test_duplicate_case_1(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.0)

    def test_duplicate_case_2(self):
        self.assertEqual(triangle_area(5.0, 12.0, 13.0), 30.0)