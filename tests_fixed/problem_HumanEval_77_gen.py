import unittest
from sut_llm.problem_HumanEval_77 import iscube

class TestIsCube(unittest.TestCase):

    def test_zero_is_cube(self):
        """Test that 0 is considered a cube (0^3 = 0)."""
        self.assertEqual(iscube(0), True)

    def test_one_is_cube(self):
        """Test that 1 is considered a cube (1^3 = 1)."""
        self.assertEqual(iscube(1), True)

    def test_negative_one_is_cube(self):
        """Test that -1 is considered a cube ((-1)^3 = -1)."""
        self.assertEqual(iscube(-1), True)

    def test_positive_perfect_cube(self):
        """Test a typical positive perfect cube (2^3 = 8)."""
        self.assertEqual(iscube(8), True)

    def test_negative_perfect_cube(self):
        """Test a typical negative perfect cube ((-2)^3 = -8)."""
        self.assertEqual(iscube(-8), True)

    def test_positive_not_cube_below_boundary(self):
        """Test a positive number just below a perfect cube (7, below 8)."""
        self.assertEqual(iscube(7), False)

    def test_positive_not_cube_above_boundary(self):
        """Test a positive number just above a perfect cube (9, above 8)."""
        self.assertEqual(iscube(9), False)

    def test_negative_not_cube_below_boundary(self):
        """Test a negative number just below a perfect cube (-9, below -8)."""
        self.assertEqual(iscube(-9), False)

    def test_large_positive_perfect_cube(self):
        """Test a large positive perfect cube (100^3 = 1,000,000)."""
        self.assertEqual(iscube(1000000), True)

    def test_large_positive_not_cube_above_boundary(self):
        """Test a large positive number just above a perfect cube (1,000,001, above 100^3)."""
        self.assertEqual(iscube(1000001), False)