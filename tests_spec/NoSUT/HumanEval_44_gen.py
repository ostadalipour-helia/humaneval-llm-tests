import unittest
from sut.problem_HumanEval_44 import change_base

class Test_change_base(unittest.TestCase):

    # Normal Cases
    def test_normal_case_eight_base_three(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_normal_case_eight_base_two(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_normal_case_fifteen_base_eight(self):
        self.assertEqual(change_base(15, 8), '17')

    # Edge Cases
    def test_edge_case_zero_x(self):
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(0, 9), '0')

    def test_edge_case_one_x(self):
        self.assertEqual(change_base(1, 2), '1')
        self.assertEqual(change_base(1, 9), '1')

    def test_edge_case_x_equals_base(self):
        self.assertEqual(change_base(9, 9), '10')

    def test_edge_case_x_less_than_base(self):
        self.assertEqual(change_base(5, 7), '5')

    # Error Cases
    def test_error_base_less_than_two(self):
        with self.assertRaises(ValueError):
            change_base(10, 1)
        with self.assertRaises(ValueError):
            change_base(10, 0)
        with self.assertRaises(ValueError):
            change_base(10, -2)

    def test_error_base_greater_than_nine(self):
        with self.assertRaises(ValueError):
            change_base(10, 10)
        with self.assertRaises(ValueError):
            change_base(10, 16)

    def test_error_x_negative(self):
        with self.assertRaises(ValueError):
            change_base(-5, 2)
        with self.assertRaises(ValueError):
            change_base(-1, 3)

    def test_error_x_not_integer(self):
        with self.assertRaises(TypeError):
            change_base(8.5, 3)
        with self.assertRaises(TypeError):
            change_base("8", 3)

    def test_error_base_not_integer(self):
        with self.assertRaises(TypeError):
            change_base(8, 2.5)
        with self.assertRaises(TypeError):
            change_base(8, "2")