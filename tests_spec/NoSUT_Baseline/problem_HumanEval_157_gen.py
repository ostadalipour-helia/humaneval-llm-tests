import unittest
import sut.problem_HumanEval_157 as mod

class TestHybrid(unittest.TestCase):
    def test_example_right_triangle(self):
            # Typical input, exact boundary for a right triangle (3,4,5)
            self.assertEqual(mod.right_angle_triangle(3, 4, 5), True)

    def test_example_not_right_triangle(self):
            # Typical input, degenerate triangle, not right-angled (1,2,3)
            self.assertEqual(mod.right_angle_triangle(1, 2, 3), False)

    def test_permutation_right_triangle(self):
            # Test with sides permuted to check all (a^2+b^2=c^2) conditions
            self.assertEqual(mod.right_angle_triangle(5, 3, 4), True)

    def test_another_pythagorean_triple(self):
            # Another common Pythagorean triple (5,12,13)
            self.assertEqual(mod.right_angle_triangle(5, 12, 13), True)

    def test_off_by_one_hypotenuse_too_small(self):
            # Off-by-one error check: hypotenuse slightly too small
            self.assertEqual(mod.right_angle_triangle(3, 4, 4), False)

    def test_off_by_one_hypotenuse_too_large(self):
            # Off-by-one error check: hypotenuse slightly too large
            self.assertEqual(mod.right_angle_triangle(3, 4, 6), False)

    def test_invalid_sides_zero(self):
            # Edge case: one side is zero (not a valid triangle)
            self.assertEqual(mod.right_angle_triangle(0, 4, 5), False)

    def test_non_triangle_sides(self):
            # Edge case: sides that cannot form any triangle (1,2,10)
            self.assertEqual(mod.right_angle_triangle(1, 2, 10), False)

    def test_large_numbers_right_triangle(self):
            # Extreme input: large numbers forming a right triangle
            self.assertEqual(mod.right_angle_triangle(10000, 24000, 26000), True)

    def test_classic_pythagorean_triple(self):
            # Normal case: Classic Pythagorean triple.
            self.assertTrue(mod.right_angle_triangle(3, 4, 5))

    def test_non_right_triangle(self):
            # Normal case: Sides form a triangle but not a right-angled one.
            self.assertFalse(mod.right_angle_triangle(2, 3, 4))

    def test_degenerate_triangle(self):
            # Normal case: Sides do not form a right triangle (and are degenerate).
            # This case also violates the triangle inequality (1+2 is not > 3),
            # so it should ideally raise an error based on preconditions.
            # However, the spec lists it as a normal case with expected_output: False.
            # If the function handles this by returning False, we test for that.
            # If it raises ValueError, the test would need to be adjusted.
            # Assuming it returns False as per normal_cases description.
            self.assertFalse(mod.right_angle_triangle(1, 2, 3))

    def test_floating_point_right_triangle(self):
            # Edge case: Floating point side lengths forming a right triangle.
            self.assertTrue(mod.right_angle_triangle(0.6, 0.8, 1.0))

    def test_larger_pythagorean_triple(self):
            # Edge case: Larger integer Pythagorean triple.
            self.assertTrue(mod.right_angle_triangle(7, 24, 25))

    def test_permutation_of_sides(self):
            # Edge case: Permutation of a known right triangle.
            self.assertTrue(mod.right_angle_triangle(4, 3, 5))

    def test_near_miss_floating_point(self):
            # Edge case: Sides very close to a right triangle but slightly off.
            # This tests the precision handling of the function.
            self.assertFalse(mod.right_angle_triangle(3.000000000000001, 4, 5))

    def test_non_numeric_input(self):
            # Error case: Non-numeric input for a side length.
            with self.assertRaises(TypeError):
                mod.right_angle_triangle('a', 4, 5)

