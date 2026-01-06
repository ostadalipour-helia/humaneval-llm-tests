import unittest
from sut.problem_HumanEval_144 import simplify

class Test_simplify(unittest.TestCase):

    # Normal Cases
    def test_normal_product_is_integer(self):
        # Description: Product is an integer (1/5 * 5/1 = 1).
        self.assertTrue(simplify("1/5", "5/1"))

    def test_normal_product_not_integer_simple(self):
        # Description: Product is not an integer (1/6 * 2/1 = 1/3).
        self.assertFalse(simplify("1/6", "2/1"))

    def test_normal_product_is_integer_with_simplification(self):
        # Description: Product is an integer (3/4 * 8/3 = 24/12 = 2).
        self.assertTrue(simplify("3/4", "8/3"))

    # Edge Cases
    def test_edge_both_one(self):
        # Description: Both fractions are 1, product is 1 (an integer).
        self.assertTrue(simplify("1/1", "1/1"))

    def test_edge_large_numbers_product_one(self):
        # Description: Product is 1, involving large denominators/numerators.
        self.assertTrue(simplify("1/100", "100/1"))

    def test_edge_no_common_factors(self):
        # Description: Product is a non-integer with no common factors (10/21).
        self.assertFalse(simplify("2/3", "5/7"))

    def test_edge_one_fraction_simplifies_to_integer(self):
        # Description: One fraction simplifies to an integer, product is an integer (2 * 3 = 6).
        self.assertTrue(simplify("10/5", "3/1"))

    # Error Cases
    def test_error_non_numeric_x(self):
        # Description: Input x contains non-numeric characters.
        # Expected behavior: ValueError due to non-numeric numerator/denominator.
        with self.assertRaises(ValueError):
            simplify("abc/def", "1/2")

    def test_error_negative_number_x(self):
        # Description: Input x contains a negative number.
        # Expected behavior: ValueError due to negative denominator (violates 'positive whole numbers' precondition).
        with self.assertRaises(ValueError):
            simplify("1/-2", "3/4")

    def test_error_zero_denominator_x(self):
        # Description: Input x has a zero denominator.
        # Expected behavior: ZeroDivisionError.
        with self.assertRaises(ZeroDivisionError):
            simplify("1/0", "2/3")

    def test_error_incorrect_format_x(self):
        # Description: Input x does not follow the specified fraction format.
        # Expected behavior: ValueError due to incorrect fraction format.
        with self.assertRaises(ValueError):
            simplify("1_2", "3/4")