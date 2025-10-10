import unittest
from sut_llm.problem_HumanEval_157 import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_classic_pythagorean_triple(self):
        self.assertEqual(right_angle_triangle(3, 4, 5), True)

    def test_another_pythagorean_triple(self):
        self.assertEqual(right_angle_triangle(5, 12, 13), True)

    def test_permutation_of_sides(self):
        self.assertEqual(right_angle_triangle(4, 5, 3), True)

    def test_scaled_pythagorean_triple(self):
        self.assertEqual(right_angle_triangle(6, 8, 10), True)

    def test_large_pythagorean_triple(self):
        self.assertEqual(right_angle_triangle(8, 15, 17), True)

    def test_not_a_triangle_from_docstring(self):
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

    def test_acute_triangle(self):
        self.assertEqual(right_angle_triangle(2, 3, 4), False)

    def test_equilateral_triangle(self):
        self.assertEqual(right_angle_triangle(7, 7, 7), False)

    def test_obtuse_triangle(self):
        self.assertEqual(right_angle_triangle(3, 5, 6), False)

    def test_another_non_right_triangle(self):
        self.assertEqual(right_angle_triangle(10, 11, 12), False)