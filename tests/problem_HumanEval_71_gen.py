import unittest
import math
from sut.problem_HumanEval_71 import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_01_typical_valid_triangle(self):
        # Example from docstring: a standard right-angled triangle
        # Covers: Typical input, exact output.
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_02_typical_invalid_triangle(self):
        # Example from docstring: sides do not form a valid triangle
        # Covers: Typical invalid input, exact output, logic mutation (all conditions fail).
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_03_boundary_equilateral_triangle(self):
        # All sides equal, just barely valid (all a+b > c conditions are true)
        # Covers: Boundary condition, exact output, typical valid.
        # s = (2+2+2)/2 = 3; Area = sqrt(3 * 1 * 1 * 1) = sqrt(3) approx 1.73205
        self.assertEqual(triangle_area(2, 2, 2), 1.73)

    def test_04_boundary_degenerate_triangle(self):
        # Sum of two sides equals the third (a+b == c), should be invalid.
        # Covers: Boundary condition (equality), off-by-one error (checking > vs >=), exact output.
        self.assertEqual(triangle_area(1, 2, 3), -1)
        self.assertEqual(triangle_area(5, 5, 10), -1) # Another degenerate case

    def test_05_boundary_almost_degenerate_valid_triangle(self):
        # Sum of two sides is just slightly greater than the third.
        # Covers: Boundary condition, off-by-one error, extreme input (small difference), exact output.
        # s = (5+5+0.01)/2 = 5.005
        # Area = sqrt(5.005 * (0.005) * (0.005) * (4.995)) approx 0.024987
        self.assertEqual(triangle_area(5, 5, 0.01), 0.02)

    def test_06_edge_case_zero_side_length(self):
        # One side is zero, which is invalid.
        # Covers: Edge case (zero input), sign/zero testing, return value.
        self.assertEqual(triangle_area(0, 4, 5), -1)

    def test_07_edge_case_negative_side_length(self):
        # One side is negative, which is invalid.
        # Covers: Edge case (negative input), sign/zero testing, return value.
        self.assertEqual(triangle_area(-3, 4, 5), -1)

    def test_08_logic_mutation_one_condition_fails(self):
        # Only one of the three triangle inequality conditions fails.
        # This specifically tests the 'AND' logic for validity.
        # (2+3 > 10) is False, (2+10 > 3) is True, (3+10 > 2) is True.
        # Covers: Logic mutation, return value testing.
        self.assertEqual(triangle_area(2, 3, 10), -1)

    def test_09_extreme_input_large_numbers(self):
        # Test with very large side lengths for a valid triangle.
        # Covers: Extreme input, exact output.
        # Using a large isosceles triangle: (100000, 100000, 1)
        # s = (200001)/2 = 100000.5
        # Area = sqrt(100000.5 * 0.5 * 0.5 * 99999.5) approx 49999.875
        self.assertEqual(triangle_area(100000, 100000, 1), 50000.00)

    def test_10_extreme_input_very_small_numbers(self):
        # Test with very small side lengths for a valid triangle.
        # Covers: Extreme input, floating point precision, boundary, exact output.
        # s = (0.01+0.01+0.01)/2 = 0.015
        # Area = sqrt(0.015 * 0.005 * 0.005 * 0.005) approx 0.0000433
        self.assertEqual(triangle_area(0.01, 0.01, 0.01), 0.00)