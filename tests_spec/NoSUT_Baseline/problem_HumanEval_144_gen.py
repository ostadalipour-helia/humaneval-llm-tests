import unittest
import sut.problem_HumanEval_144 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1_true(self):
            # Docstring example: Product is exactly 1, a whole number.
            self.assertEqual(mod.simplify("1/5", "5/1"), True)

    def test_docstring_example_2_false(self):
            # Docstring example: Product is 1/3, not a whole number.
            self.assertEqual(mod.simplify("1/6", "2/1"), False)

    def test_docstring_example_3_false(self):
            # Docstring example: Product is 3.5, not a whole number.
            self.assertEqual(mod.simplify("7/10", "10/2"), False)

    def test_boundary_product_is_exact_whole_number(self):
            # Boundary test: Product simplifies to an exact whole number (2).
            # Catches issues if intermediate calculations or final division are flawed.
            self.assertEqual(mod.simplify("3/7", "14/3"), True)

    def test_boundary_product_is_just_not_whole_number(self):
            # Boundary test: Product is very close to a whole number but not exactly (39/21).
            # Catches off-by-one errors in divisibility check.
            self.assertEqual(mod.simplify("3/7", "13/3"), False)

    def test_edge_case_both_fractions_are_whole_numbers(self):
            # Edge case: Both input fractions have denominator 1, product is a whole number.
            self.assertEqual(mod.simplify("5/1", "2/1"), True)

    def test_edge_case_fractions_with_numerator_one_product_not_whole(self):
            # Edge case: Both fractions have numerator 1, product is not a whole number.
            self.assertEqual(mod.simplify("1/2", "1/3"), False)

    def test_extreme_large_numbers_product_is_one(self):
            # Extreme input: Large numbers that cancel out to 1.
            # Tests handling of large integer multiplication and division.
            self.assertEqual(mod.simplify("999/1000", "1000/999"), True)

    def test_extreme_large_numbers_product_not_whole(self):
            # Extreme input: Large numbers where the product is not a whole number.
            # Tests robustness with large numbers that don't simplify cleanly.
            self.assertEqual(mod.simplify("1000/3", "2/1000"), False)

    def test_logic_mutation_one_fraction_is_one_other_is_whole(self):
            # Logic test: One fraction is equivalent to 1 (e.g., 5/5), the other is a whole number.
            # Catches issues if fraction simplification or parsing of X/X is incorrect.
            self.assertEqual(mod.simplify("5/5", "3/1"), True)

    def test_normal_product_is_integer(self):
            # Description: Product is an integer (1/5 * 5/1 = 1).
            self.assertTrue(mod.simplify("1/5", "5/1"))

    def test_normal_product_not_integer_simple(self):
            # Description: Product is not an integer (1/6 * 2/1 = 1/3).
            self.assertFalse(mod.simplify("1/6", "2/1"))

    def test_normal_product_is_integer_with_simplification(self):
            # Description: Product is an integer (3/4 * 8/3 = 24/12 = 2).
            self.assertTrue(mod.simplify("3/4", "8/3"))
    
        # Edge Cases

    def test_edge_both_one(self):
            # Description: Both fractions are 1, product is 1 (an integer).
            self.assertTrue(mod.simplify("1/1", "1/1"))

    def test_edge_large_numbers_product_one(self):
            # Description: Product is 1, involving large denominators/numerators.
            self.assertTrue(mod.simplify("1/100", "100/1"))

    def test_edge_no_common_factors(self):
            # Description: Product is a non-integer with no common factors (10/21).
            self.assertFalse(mod.simplify("2/3", "5/7"))

    def test_edge_one_fraction_simplifies_to_integer(self):
            # Description: One fraction simplifies to an integer, product is an integer (2 * 3 = 6).
            self.assertTrue(mod.simplify("10/5", "3/1"))
    
        # Error Cases

    def test_error_non_numeric_x(self):
            # Description: Input x contains non-numeric characters.
            # Expected behavior: ValueError due to non-numeric numerator/denominator.
            with self.assertRaises(ValueError):
                mod.simplify("abc/def", "1/2")

    def test_error_zero_denominator_x(self):
            # Description: Input x has a zero denominator.
            # Expected behavior: ZeroDivisionError.
            with self.assertRaises(ZeroDivisionError):
                mod.simplify("1/0", "2/3")

    def test_error_incorrect_format_x(self):
            # Description: Input x does not follow the specified fraction format.
            # Expected behavior: ValueError due to incorrect fraction format.
            with self.assertRaises(ValueError):
                mod.simplify("1_2", "3/4")

