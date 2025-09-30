import unittest
from sut.problem_HumanEval_13 import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_coprime_numbers(self):
        # Test case from docstring
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_common_divisor_numbers(self):
        # Test case from docstring
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_one_is_multiple_of_other(self):
        self.assertEqual(greatest_common_divisor(10, 5), 5)

    def test_one_number_is_zero(self):
        self.assertEqual(greatest_common_divisor(0, 7), 7)

    def test_both_numbers_are_zero(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_negative_and_positive(self):
        self.assertEqual(greatest_common_divisor(-12, 8), 4)

    def test_both_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-18, -24), 6)

    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(100, 75), 25)

    def test_prime_numbers(self):
        self.assertEqual(greatest_common_divisor(7, 13), 1)

    def test_one_number_is_one(self):
        self.assertEqual(greatest_common_divisor(1, 100), 1)

if __name__ == '__main__':
    unittest.main()