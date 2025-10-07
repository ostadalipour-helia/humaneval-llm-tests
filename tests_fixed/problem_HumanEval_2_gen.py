import unittest
from sut_llm.problem_HumanEval_2 import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_example_from_docstring(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    def test_simple_positive_float(self):
        self.assertAlmostEqual(truncate_number(1.25), 0.25)

    def test_number_with_many_decimal_places(self):
        self.assertAlmostEqual(truncate_number(123.456789), 0.456789)

    def test_number_with_very_small_decimal_part(self):
        self.assertAlmostEqual(truncate_number(5.000001), 0.000001)

    def test_number_with_decimal_part_close_to_one(self):
        self.assertAlmostEqual(truncate_number(4.999999), 0.999999)

    def test_exact_integer_input(self):
        self.assertAlmostEqual(truncate_number(7.0), 0.0)

    def test_number_less_than_one(self):
        self.assertAlmostEqual(truncate_number(0.75), 0.75)

    def test_large_integer_part_with_decimal(self):
        self.assertAlmostEqual(truncate_number(1000.1), 0.1)

    def test_number_with_extremely_small_decimal_part(self):
        self.assertAlmostEqual(truncate_number(2.000000000000001), 0.000000000000001)

    def test_another_decimal_part_close_to_one(self):
        self.assertAlmostEqual(truncate_number(99.99), 0.99)