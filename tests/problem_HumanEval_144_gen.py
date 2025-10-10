import unittest
from sut.problem_HumanEval_144 import simplify

class TestSimplify(unittest.TestCase):

    def test_docstring_example_1_true(self):
        # Docstring example: Product is exactly 1, a whole number.
        self.assertEqual(simplify("1/5", "5/1"), True)

    def test_docstring_example_2_false(self):
        # Docstring example: Product is 1/3, not a whole number.
        self.assertEqual(simplify("1/6", "2/1"), False)

    def test_docstring_example_3_false(self):
        # Docstring example: Product is 3.5, not a whole number.
        self.assertEqual(simplify("7/10", "10/2"), False)

    def test_boundary_product_is_exact_whole_number(self):
        # Boundary test: Product simplifies to an exact whole number (2).
        # Catches issues if intermediate calculations or final division are flawed.
        self.assertEqual(simplify("3/7", "14/3"), True)

    def test_boundary_product_is_just_not_whole_number(self):
        # Boundary test: Product is very close to a whole number but not exactly (39/21).
        # Catches off-by-one errors in divisibility check.
        self.assertEqual(simplify("3/7", "13/3"), False)

    def test_edge_case_both_fractions_are_whole_numbers(self):
        # Edge case: Both input fractions have denominator 1, product is a whole number.
        self.assertEqual(simplify("5/1", "2/1"), True)

    def test_edge_case_fractions_with_numerator_one_product_not_whole(self):
        # Edge case: Both fractions have numerator 1, product is not a whole number.
        self.assertEqual(simplify("1/2", "1/3"), False)

    def test_extreme_large_numbers_product_is_one(self):
        # Extreme input: Large numbers that cancel out to 1.
        # Tests handling of large integer multiplication and division.
        self.assertEqual(simplify("999/1000", "1000/999"), True)

    def test_extreme_large_numbers_product_not_whole(self):
        # Extreme input: Large numbers where the product is not a whole number.
        # Tests robustness with large numbers that don't simplify cleanly.
        self.assertEqual(simplify("1000/3", "2/1000"), False)

    def test_logic_mutation_one_fraction_is_one_other_is_whole(self):
        # Logic test: One fraction is equivalent to 1 (e.g., 5/5), the other is a whole number.
        # Catches issues if fraction simplification or parsing of X/X is incorrect.
        self.assertEqual(simplify("5/5", "3/1"), True)