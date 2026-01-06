import unittest
import sut.problem_HumanEval_53 as mod

class TestHybrid(unittest.TestCase):
    def test_positive_integers_from_docstring_1(self):
            """Test with positive integers as per docstring example 1."""
            self.assertEqual(mod.add(2, 3), 5)

    def test_positive_integers_from_docstring_2(self):
            """Test with positive integers as per docstring example 2."""
            self.assertEqual(mod.add(5, 7), 12)

    def test_zero_and_positive(self):
            """Test adding zero to a positive number (boundary case)."""
            self.assertEqual(mod.add(0, 10), 10)

    def test_positive_and_zero(self):
            """Test adding a positive number to zero (boundary case)."""
            self.assertEqual(mod.add(15, 0), 15)

    def test_two_zeros(self):
            """Test adding two zeros (edge case, boundary case)."""
            self.assertEqual(mod.add(0, 0), 0)

    def test_negative_integers(self):
            """Test adding two negative integers (sign testing)."""
            self.assertEqual(mod.add(-5, -3), -8)

    def test_positive_and_negative_sum_positive(self):
            """Test adding a positive and a negative number where sum is positive (sign testing)."""
            self.assertEqual(mod.add(10, -3), 7)

    def test_positive_and_negative_sum_negative(self):
            """Test adding a positive and a negative number where sum is negative (sign testing)."""
            self.assertEqual(mod.add(3, -10), -7)

    def test_positive_and_negative_sum_zero(self):
            """Test adding a positive and a negative number that sum to zero (boundary case)."""
            self.assertEqual(mod.add(7, -7), 0)

    def test_large_positive_integers(self):
            """Test with very large positive integers (extreme input)."""
            self.assertEqual(mod.add(1000000000, 2000000000), 3000000000)

    def test_normal_positive_integers_1(self):
            # Adding two positive integers.
            self.assertEqual(mod.add(2, 3), 5)

    def test_normal_positive_integers_2(self):
            # Another example of adding two positive integers.
            self.assertEqual(mod.add(10, 20), 30)

    def test_edge_one_input_zero(self):
            # One input is zero.
            self.assertEqual(mod.add(0, 5), 5)

    def test_edge_both_inputs_zero(self):
            # Both inputs are zero.
            self.assertEqual(mod.add(0, 0), 0)

    def test_edge_negative_and_positive_result_positive(self):
            # Adding a negative and a positive integer, result is positive.
            self.assertEqual(mod.add(-2, 3), 1)

    def test_edge_positive_and_negative_result_negative(self):
            # Adding a positive and a negative integer, result is negative.
            self.assertEqual(mod.add(2, -3), -1)

    def test_edge_two_negative_integers(self):
            # Adding two negative integers.
            self.assertEqual(mod.add(-5, -7), -12)

    def test_edge_additive_inverse(self):
            # Adding a number and its additive inverse.
            self.assertEqual(mod.add(5, -5), 0)

    def test_edge_large_integers(self):
            # Adding very large integers (Python handles arbitrary precision).
            self.assertEqual(mod.add(1000000000000000000, 2000000000000000000), 3000000000000000000)

