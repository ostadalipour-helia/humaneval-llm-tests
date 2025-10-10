import unittest
from sut_llm.problem_HumanEval_137 import compare_one

class TestCompareOne(unittest.TestCase):

    def test_1_int_vs_float_b_larger(self):
        # Docstring example: compare_one(1, 2.5) ➞ 2.5
        # Typical input, float larger, verifies return type preservation.
        self.assertEqual(compare_one(1, 2.5), 2.5)

    def test_2_int_vs_string_float_comma_b_larger(self):
        # Docstring example: compare_one(1, "2,3") ➞ "2,3"
        # Typical input, string float larger, handles comma decimal, verifies return type preservation.
        self.assertEqual(compare_one(1, "2,3"), "2,3")

    def test_3_string_float_dot_vs_string_int_b_larger(self):
        # Docstring example: compare_one("5,1", "6") ➞ "6" (modified to use dot for variety)
        # Typical input, string int larger, handles dot decimal, verifies return type preservation.
        self.assertEqual(compare_one("5.1", "6"), "6")

    def test_4_equal_integers_returns_none(self):
        # Boundary condition: exact equality for same types.
        # Verifies None return for equal values.
        self.assertEqual(compare_one(5, 5), None)

    def test_5_equal_mixed_types_int_vs_string_int_returns_none(self):
        # Docstring example: compare_one("1", 1) ➞ None
        # Boundary condition: exact equality for numerically equal but different types.
        # Verifies None return for equal values, handles string parsing.
        self.assertEqual(compare_one("1", 1), None)

    def test_6_negative_float_vs_int_a_larger(self):
        # Edge case: negative numbers.
        # Verifies correct comparison and return type for negative float larger than negative int.
        self.assertEqual(compare_one(-5.5, -6), -5.5)

    def test_7_zero_vs_negative_float_a_larger(self):
        # Boundary condition: zero and a very small negative number.
        # Verifies correct comparison with zero and negative values.
        self.assertEqual(compare_one(0, -0.001), 0)

    def test_8_string_float_many_decimals_vs_int_a_larger(self):
        # Extreme input: string float with high precision.
        # Verifies correct parsing and comparison for detailed string floats.
        self.assertEqual(compare_one("3.1415926535", 3), "3.1415926535")

    def test_9_boundary_very_close_floats_b_slightly_larger(self):
        # Boundary condition: off-by-one for floats, very close values.
        # Catches issues with precision or incorrect comparison operators (< vs <=).
        self.assertEqual(compare_one(1.0000000000000001, 1.0000000000000002), 1.0000000000000002)

    def test_10_mixed_types_string_comma_vs_float_a_larger(self):
        # Edge case: mixed types with string float using comma, close values.
        # Verifies robust parsing and comparison across different types and string formats.
        self.assertEqual(compare_one("100,0", 99.9), "100,0")

    def test_invalid_string_input_for_parsing_error(self):
        """
        Tests the scenario where a string cannot be parsed to a float,
        covering lines 21 (except ValueError), 26 (pass), 27 (return None
        """
        result = compare_one("not_a_number", 5)
        self.assertIsNone(result)

    def test_non_numeric_type_input(self):
        """
        Tests the scenario where an input is not an int, float, or string,
        covering lines 27 (return None from _parse_to_float) and 35 (return None
        """
        result = compare_one(None, 10)
        self.assertIsNone(result)

