import unittest
import sut.problem_HumanEval_137 as mod

class TestHybrid(unittest.TestCase):
    def test_1_int_vs_float_b_larger(self):
            # Docstring example: mod.compare_one(1, 2.5) ➞ 2.5
            # Typical input, float larger, verifies return type preservation.
            self.assertEqual(mod.compare_one(1, 2.5), 2.5)

    def test_2_int_vs_string_float_comma_b_larger(self):
            # Docstring example: mod.compare_one(1, "2,3") ➞ "2,3"
            # Typical input, string float larger, handles comma decimal, verifies return type preservation.
            self.assertEqual(mod.compare_one(1, "2,3"), "2,3")

    def test_3_string_float_dot_vs_string_int_b_larger(self):
            # Docstring example: mod.compare_one("5,1", "6") ➞ "6" (modified to use dot for variety)
            # Typical input, string int larger, handles dot decimal, verifies return type preservation.
            self.assertEqual(mod.compare_one("5.1", "6"), "6")

    def test_4_equal_integers_returns_none(self):
            # Boundary condition: exact equality for same types.
            # Verifies None return for equal values.
            self.assertEqual(mod.compare_one(5, 5), None)

    def test_5_equal_mixed_types_int_vs_string_int_returns_none(self):
            # Docstring example: mod.compare_one("1", 1) ➞ None
            # Boundary condition: exact equality for numerically equal but different types.
            # Verifies None return for equal values, handles string parsing.
            self.assertEqual(mod.compare_one("1", 1), None)

    def test_6_negative_float_vs_int_a_larger(self):
            # Edge case: negative numbers.
            # Verifies correct comparison and return type for negative float larger than negative int.
            self.assertEqual(mod.compare_one(-5.5, -6), -5.5)

    def test_7_zero_vs_negative_float_a_larger(self):
            # Boundary condition: zero and a very small negative number.
            # Verifies correct comparison with zero and negative values.
            self.assertEqual(mod.compare_one(0, -0.001), 0)

    def test_8_string_float_many_decimals_vs_int_a_larger(self):
            # Extreme input: string float with high precision.
            # Verifies correct parsing and comparison for detailed string floats.
            self.assertEqual(mod.compare_one("3.1415926535", 3), "3.1415926535")

    def test_9_boundary_very_close_floats_b_slightly_larger(self):
            # Boundary condition: off-by-one for floats, very close values.
            # Catches issues with precision or incorrect comparison operators (< vs <=).
            self.assertEqual(mod.compare_one(1.0000000000000001, 1.0000000000000002), 1.0000000000000002)

    def test_10_mixed_types_string_comma_vs_float_a_larger(self):
            # Edge case: mixed types with string float using comma, close values.
            # Verifies robust parsing and comparison across different types and string formats.
            self.assertEqual(mod.compare_one("100,0", 99.9), "100,0")

    def test_normal_float_larger(self):
            a = 1
            b = 2.5
            self.assertEqual(mod.compare_one(a, b), 2.5)

    def test_normal_string_comma_larger(self):
            a = 1
            b = "2,3"
            self.assertEqual(mod.compare_one(a, b), "2,3")

    def test_normal_int_larger(self):
            a = 10
            b = 5
            self.assertEqual(mod.compare_one(a, b), 10)

    def test_normal_string_dot_larger(self):
            a = "10.5"
            b = "9.2"
            self.assertEqual(mod.compare_one(a, b), "10.5")
    
        # Edge Cases

    def test_edge_equal_string_int(self):
            a = "1"
            b = 1
            self.assertIsNone(mod.compare_one(a, b))

    def test_edge_equal_float_int(self):
            a = 5.0
            b = 5
            self.assertIsNone(mod.compare_one(a, b))

    def test_edge_negative_int_larger(self):
            a = -1
            b = -2
            self.assertEqual(mod.compare_one(a, b), -1)

    def test_edge_negative_string_vs_int(self):
            a = "-1.5"
            b = -1
            self.assertEqual(mod.compare_one(a, b), -1)

    def test_edge_equal_zero_float_int(self):
            a = 0
            b = 0.0
            self.assertIsNone(mod.compare_one(a, b))
    
        # Error Cases

    def test_error_invalid_string_a(self):
            a = "abc"
            b = 1
            with self.assertRaises(ValueError):
                mod.compare_one(a, b)

    def test_error_invalid_type_b(self):
            a = 1
            b = [2]
            with self.assertRaises(TypeError):
                mod.compare_one(a, b)

    def test_error_invalid_separator_a(self):
            a = "1;2"
            b = 3
            with self.assertRaises(ValueError):
                mod.compare_one(a, b)

