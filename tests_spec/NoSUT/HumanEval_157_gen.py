import unittest
from sut.problem_HumanEval_157 import right_angle_triangle

class Test_right_angle_triangle(unittest.TestCase):
    def test_classic_pythagorean_triple(self):
        # Normal case: Classic Pythagorean triple.
        self.assertTrue(right_angle_triangle(3, 4, 5))

    def test_another_pythagorean_triple(self):
        # Normal case: Another Pythagorean triple.
        self.assertTrue(right_angle_triangle(5, 12, 13))

    def test_non_right_triangle(self):
        # Normal case: Sides form a triangle but not a right-angled one.
        self.assertFalse(right_angle_triangle(2, 3, 4))

    def test_degenerate_triangle(self):
        # Normal case: Sides do not form a right triangle (and are degenerate).
        # This case also violates the triangle inequality (1+2 is not > 3),
        # so it should ideally raise an error based on preconditions.
        # However, the spec lists it as a normal case with expected_output: False.
        # If the function handles this by returning False, we test for that.
        # If it raises ValueError, the test would need to be adjusted.
        # Assuming it returns False as per normal_cases description.
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_floating_point_right_triangle(self):
        # Edge case: Floating point side lengths forming a right triangle.
        self.assertTrue(right_angle_triangle(0.6, 0.8, 1.0))

    def test_larger_pythagorean_triple(self):
        # Edge case: Larger integer Pythagorean triple.
        self.assertTrue(right_angle_triangle(7, 24, 25))

    def test_permutation_of_sides(self):
        # Edge case: Permutation of a known right triangle.
        self.assertTrue(right_angle_triangle(4, 3, 5))

    def test_near_miss_floating_point(self):
        # Edge case: Sides very close to a right triangle but slightly off.
        # This tests the precision handling of the function.
        self.assertFalse(right_angle_triangle(3.000000000000001, 4, 5))

    def test_non_numeric_input(self):
        # Error case: Non-numeric input for a side length.
        with self.assertRaises(TypeError):
            right_angle_triangle('a', 4, 5)

    def test_negative_side_length(self):
        # Error case: Negative side length (violates precondition).
        # Expected behavior: Undefined behavior or ValueError. We assert ValueError.
        with self.assertRaises(ValueError):
            right_angle_triangle(3, -4, 5)

    def test_zero_side_length(self):
        # Error case: Zero side length (violates precondition).
        # Expected behavior: Undefined behavior or ValueError. We assert ValueError.
        with self.assertRaises(ValueError):
            right_angle_triangle(0, 4, 5)

    def test_violates_triangle_inequality(self):
        # Error case: Sides that cannot form a triangle (violates precondition).
        # Expected behavior: Undefined behavior or ValueError. We assert ValueError.
        with self.assertRaises(ValueError):
            right_angle_triangle(1, 1, 10)