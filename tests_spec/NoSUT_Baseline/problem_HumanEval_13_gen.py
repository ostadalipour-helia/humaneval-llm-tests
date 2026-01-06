import unittest
import sut.problem_HumanEval_13 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1_coprime(self):
            # Typical case: two coprime positive integers
            self.assertEqual(mod.greatest_common_divisor(3, 5), 1)

    def test_docstring_example_2_common_factor(self):
            # Typical case: two positive integers with a common factor
            self.assertEqual(mod.greatest_common_divisor(25, 15), 5)

    def test_boundary_one_is_zero(self):
            # Boundary case: one input is zero. GCD(a, 0) = |a|.
            self.assertEqual(mod.greatest_common_divisor(10, 0), 10)
            self.assertEqual(mod.greatest_common_divisor(0, 7), 7)

    def test_boundary_both_are_zero(self):
            # Edge case: both inputs are zero. GCD(0, 0) is often defined as 0.
            self.assertEqual(mod.greatest_common_divisor(0, 0), 0)

    def test_edge_one_is_one(self):
            # Edge case: one input is one. GCD(a, 1) = 1.
            self.assertEqual(mod.greatest_common_divisor(7, 1), 1)
            self.assertEqual(mod.greatest_common_divisor(1, 100), 1)

    def test_logic_one_is_multiple_of_other(self):
            # Logic test: one number is a multiple of the other.
            # This tests the termination condition of Euclidean algorithm.
            self.assertEqual(mod.greatest_common_divisor(100, 10), 10)
            self.assertEqual(mod.greatest_common_divisor(77, 11), 11)

    def test_large_numbers(self):
            # Extreme case: large numbers to test efficiency and correctness with larger values.
            # GCD(1000000, 750000) = GCD(2^6 * 5^6, 2^4 * 3 * 5^6) = 2^4 * 5^6 = 16 * 15625 = 250000
            self.assertEqual(mod.greatest_common_divisor(1000000, 750000), 250000)

    def test_coprime_positive_integers(self):
            # Description: Two coprime positive integers.
            self.assertEqual(mod.greatest_common_divisor(3, 5), 1)

    def test_positive_common_factor(self):
            # Description: Two positive integers with a common factor.
            self.assertEqual(mod.greatest_common_divisor(25, 15), 5)

    def test_one_multiple_of_other(self):
            # Description: One integer is a multiple of the other.
            self.assertEqual(mod.greatest_common_divisor(10, 5), 5)

    def test_one_input_zero_other_positive(self):
            # Description: One input is zero, the other is positive.
            self.assertEqual(mod.greatest_common_divisor(0, 5), 5)

    def test_one_input_positive_other_zero(self):
            # Description: One input is positive, the other is zero.
            self.assertEqual(mod.greatest_common_divisor(5, 0), 5)

    def test_both_inputs_zero(self):
            # Description: Both inputs are zero.
            self.assertEqual(mod.greatest_common_divisor(0, 0), 0)

    def test_one_input_negative_other_positive(self):
            # Description: One input is negative, the other is positive.
            self.assertEqual(mod.greatest_common_divisor(-10, 5), 5)

    def test_smallest_positive_integers(self):
            # Description: Smallest positive integers.
            self.assertEqual(mod.greatest_common_divisor(1, 1), 1)

    def test_input_b_not_integer(self):
            # Description: Input 'b' is not an integer.
            with self.assertRaises(TypeError):
                mod.greatest_common_divisor(3, 'hello')

