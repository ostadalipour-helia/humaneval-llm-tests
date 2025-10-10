import unittest
from sut.problem_HumanEval_44 import change_base

class TestChangeBase(unittest.TestCase):

    def test_example_1(self):
        # Test case from docstring: typical input
        self.assertEqual(change_base(8, 3), '22')

    def test_example_2(self):
        # Test case from docstring: typical input, smallest valid base
        self.assertEqual(change_base(8, 2), '1000')

    def test_example_3(self):
        # Test case from docstring: typical input, smallest valid base
        self.assertEqual(change_base(7, 2), '111')

    def test_zero_x(self):
        # Edge case: x is zero
        self.assertEqual(change_base(0, 5), '0')

    def test_one_x(self):
        # Edge case: x is one
        self.assertEqual(change_base(1, 7), '1')

    def test_smallest_base_boundary(self):
        # Boundary test: x with the smallest allowed base (base=2)
        self.assertEqual(change_base(10, 2), '1010')

    def test_largest_base_boundary(self):
        # Boundary test: x with the largest allowed base (base=9)
        self.assertEqual(change_base(80, 9), '88')

    def test_x_power_of_base(self):
        # Off-by-one/Logic test: x is an exact power of the base (e.g., 3^3 = 27)
        self.assertEqual(change_base(27, 3), '1000')

    def test_x_one_less_than_power_of_base(self):
        # Off-by-one/Logic test: x is one less than a power of the base (e.g., 3^3 - 1 = 26)
        self.assertEqual(change_base(26, 3), '222')

    def test_large_x_mid_base(self):
        # Extreme/Unusual input: larger x value with a mid-range base
        self.assertEqual(change_base(123, 7), '234')