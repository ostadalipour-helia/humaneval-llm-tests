import unittest
from sut_llm.problem_HumanEval_128 import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_1_empty_array(self):
        """
        Test case for an empty input array.
        Should return None as per docstring.
        Covers: Edge Case, Boundary Testing, Return Value Testing.
        """
        self.assertIsNone(prod_signs([]))

    def test_2_single_positive_element(self):
        """
        Test case for an array with a single positive element.
        Covers: Edge Case, Boundary Testing, Off-by-One Errors.
        """
        self.assertEqual(prod_signs([5]), 5)

    def test_3_single_negative_element(self):
        """
        Test case for an array with a single negative element.
        Covers: Edge Case, Boundary Testing, Off-by-One Errors, Sign Testing.
        """
        self.assertEqual(prod_signs([-7]), -7)

    def test_4_single_zero_element(self):
        """
        Test case for an array with a single zero element.
        Covers: Edge Case, Boundary Testing, Sign and Zero Testing.
        """
        self.assertEqual(prod_signs([0]), 0)

    def test_5_mixed_positive_negative_even_negatives(self):
        """
        Test case with mixed positive and negative numbers, even count of negatives.
        Product of signs should be 1.
        Covers: Typical Input, Logic Mutations, Return Value Testing.
        """
        self.assertEqual(prod_signs([1, 2, -3, -4]), 10) # sum_mag=10, prod_signs=1

    def test_6_mixed_positive_negative_odd_negatives(self):
        """
        Test case with mixed positive and negative numbers, odd count of negatives.
        Product of signs should be -1. (Example from docstring)
        Covers: Typical Input, Logic Mutations, Return Value Testing.
        """
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9) # sum_mag=9, prod_signs=-1

    def test_7_array_contains_zero(self):
        """
        Test case for an array containing zero.
        The product of signs should become 0. (Example from docstring)
        Covers: Logic Mutations, Sign and Zero Testing, Return Value Testing.
        """
        self.assertEqual(prod_signs([0, 1, -2, 3]), 0) # sum_mag=6, prod_signs=0

    def test_8_all_positive_numbers(self):
        """
        Test case with all positive numbers.
        Product of signs should be 1.
        Covers: Extreme/Unusual Input, Logic Mutations, Sign Testing.
        """
        self.assertEqual(prod_signs([10, 20, 30]), 60) # sum_mag=60, prod_signs=1

    def test_9_all_negative_numbers_odd_count(self):
        """
        Test case with all negative numbers, odd count.
        Product of signs should be -1.
        Covers: Extreme/Unusual Input, Logic Mutations, Sign Testing.
        """
        self.assertEqual(prod_signs([-1, -2, -3]), -6) # sum_mag=6, prod_signs=-1

    def test_10_all_negative_numbers_even_count(self):
        """
        Test case with all negative numbers, even count.
        Product of signs should be 1.
        Covers: Extreme/Unusual Input, Logic Mutations, Sign Testing.
        """
        self.assertEqual(prod_signs([-1, -2, -3, -4]), 10) # sum_mag=10, prod_signs=1