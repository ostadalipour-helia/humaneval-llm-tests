import unittest
from sut_llm.problem_HumanEval_157 import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_example_right_triangle(self):
        # Typical input, exact boundary for a right triangle (3,4,5)
        self.assertEqual(right_angle_triangle(3, 4, 5), True)

    def test_example_not_right_triangle(self):
        # Typical input, degenerate triangle, not right-angled (1,2,3)
        self.assertEqual(right_angle_triangle(1, 2, 3), False)

    def test_permutation_right_triangle(self):
        # Test with sides permuted to check all (a^2+b^2=c^2) conditions
        self.assertEqual(right_angle_triangle(5, 3, 4), True)

    def test_another_pythagorean_triple(self):
        # Another common Pythagorean triple (5,12,13)
        self.assertEqual(right_angle_triangle(5, 12, 13), True)

    def test_off_by_one_hypotenuse_too_small(self):
        # Off-by-one error check: hypotenuse slightly too small
        self.assertEqual(right_angle_triangle(3, 4, 4), False)

    def test_off_by_one_hypotenuse_too_large(self):
        # Off-by-one error check: hypotenuse slightly too large
        self.assertEqual(right_angle_triangle(3, 4, 6), False)

    def test_invalid_sides_zero(self):
        # Edge case: one side is zero (not a valid triangle)
        self.assertEqual(right_angle_triangle(0, 4, 5), False)

    def test_invalid_sides_negative(self):
        # Edge case: one side is negative (not a valid triangle)
        self.assertEqual(right_angle_triangle(-3, 4, 5), False)

    def test_non_triangle_sides(self):
        # Edge case: sides that cannot form any triangle (1,2,10)
        self.assertEqual(right_angle_triangle(1, 2, 10), False)

    def test_large_numbers_right_triangle(self):
        # Extreme input: large numbers forming a right triangle
        self.assertEqual(right_angle_triangle(10000, 24000, 26000), True)