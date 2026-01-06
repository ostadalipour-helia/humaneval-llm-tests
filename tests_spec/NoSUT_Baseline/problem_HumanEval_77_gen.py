import unittest
import sut.problem_HumanEval_77 as mod

class TestHybrid(unittest.TestCase):
    def test_zero_is_cube(self):
            """Test that 0 is considered a cube (0^3 = 0)."""
            self.assertEqual(mod.iscube(0), True)

    def test_one_is_cube(self):
            """Test that 1 is considered a cube (1^3 = 1)."""
            self.assertEqual(mod.iscube(1), True)

    def test_negative_one_is_cube(self):
            """Test that -1 is considered a cube ((-1)^3 = -1)."""
            self.assertEqual(mod.iscube(-1), True)

    def test_positive_perfect_cube(self):
            """Test a typical positive perfect cube (2^3 = 8)."""
            self.assertEqual(mod.iscube(8), True)

    def test_negative_perfect_cube(self):
            """Test a typical negative perfect cube ((-2)^3 = -8)."""
            self.assertEqual(mod.iscube(-8), True)

    def test_positive_not_cube_below_boundary(self):
            """Test a positive number just below a perfect cube (7, below 8)."""
            self.assertEqual(mod.iscube(7), False)

    def test_positive_not_cube_above_boundary(self):
            """Test a positive number just above a perfect cube (9, above 8)."""
            self.assertEqual(mod.iscube(9), False)

    def test_negative_not_cube_below_boundary(self):
            """Test a negative number just below a perfect cube (-9, below -8)."""
            self.assertEqual(mod.iscube(-9), False)

    def test_large_positive_perfect_cube(self):
            """Test a large positive perfect cube (100^3 = 1,000,000)."""
            self.assertEqual(mod.iscube(1000000), True)

    def test_large_positive_not_cube_above_boundary(self):
            """Test a large positive number just above a perfect cube (1,000,001, above 100^3)."""
            self.assertEqual(mod.iscube(1000001), False)

    def test_normal_positive_cube(self):
            # Normal case: Positive integer that is a perfect cube (4*4*4).
            self.assertTrue(mod.iscube(64))

    def test_normal_negative_cube(self):
            # Normal case: Negative integer that is a perfect cube (-1*-1*-1).
            self.assertTrue(mod.iscube(-1))

    def test_normal_positive_not_cube_small(self):
            # Normal case: Positive integer that is not a perfect cube.
            self.assertFalse(mod.iscube(2))

    def test_normal_positive_not_cube_large(self):
            # Normal case: Larger positive integer that is not a perfect cube.
            self.assertFalse(mod.iscube(180))

    def test_edge_zero_cube(self):
            # Edge case: Zero is a perfect cube (0*0*0).
            self.assertTrue(mod.iscube(0))

    def test_edge_one_cube(self):
            # Edge case: One is a perfect cube (1*1*1).
            self.assertTrue(mod.iscube(1))

    def test_edge_another_negative_cube(self):
            # Edge case: Another negative perfect cube (-2*-2*-2).
            self.assertTrue(mod.iscube(-8))

    def test_edge_positive_just_below_cube(self):
            # Edge case: Positive integer just below a perfect cube (8).
            self.assertFalse(mod.iscube(7))

    def test_edge_positive_just_above_cube(self):
            # Edge case: Positive integer just above a perfect cube (8).
            self.assertFalse(mod.iscube(9))

    def test_edge_negative_just_above_negative_cube(self):
            # Edge case: Negative integer just above a negative perfect cube (-8).
            self.assertFalse(mod.iscube(-7))

    def test_edge_negative_just_below_negative_cube(self):
            # Edge case: Negative integer just below a negative perfect cube (-8).
            self.assertFalse(mod.iscube(-9))

