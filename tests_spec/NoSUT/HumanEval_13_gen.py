import unittest
from sut.problem_HumanEval_13 import greatest_common_divisor

class Test_greatest_common_divisor(unittest.TestCase):
    def test_coprime_positive_integers(self):
        # Description: Two coprime positive integers.
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_positive_common_factor(self):
        # Description: Two positive integers with a common factor.
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_one_multiple_of_other(self):
        # Description: One integer is a multiple of the other.
        self.assertEqual(greatest_common_divisor(10, 5), 5)

    def test_one_input_zero_other_positive(self):
        # Description: One input is zero, the other is positive.
        self.assertEqual(greatest_common_divisor(0, 5), 5)

    def test_one_input_positive_other_zero(self):
        # Description: One input is positive, the other is zero.
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_both_inputs_zero(self):
        # Description: Both inputs are zero.
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_one_input_negative_other_positive(self):
        # Description: One input is negative, the other is positive.
        self.assertEqual(greatest_common_divisor(-10, 5), 5)

    def test_both_inputs_negative(self):
        # Description: Both inputs are negative.
        self.assertEqual(greatest_common_divisor(-10, -5), 5)

    def test_smallest_positive_integers(self):
        # Description: Smallest positive integers.
        self.assertEqual(greatest_common_divisor(1, 1), 1)

    def test_input_a_not_integer(self):
        # Description: Input 'a' is not an integer.
        with self.assertRaises(TypeError):
            greatest_common_divisor(3.0, 5)

    def test_input_b_not_integer(self):
        # Description: Input 'b' is not an integer.
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, 'hello')