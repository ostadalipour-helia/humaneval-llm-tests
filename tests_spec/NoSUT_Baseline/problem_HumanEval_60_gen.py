import unittest
import sut.problem_HumanEval_60 as mod

class TestHybrid(unittest.TestCase):
    def test_positive_small_n_1(self):
            # Edge case: single element sum, boundary for smallest positive n
            self.assertEqual(mod.sum_to_n(1), 1)

    def test_positive_small_n_2(self):
            # Off-by-one from n=1, typical small input
            self.assertEqual(mod.sum_to_n(2), 3)

    def test_positive_small_n_3(self):
            # Typical input, matches a docstring example (implicitly 1+2+3=6)
            self.assertEqual(mod.sum_to_n(3), 6)

    def test_positive_medium_n_5(self):
            # Typical input, matches a docstring example
            self.assertEqual(mod.sum_to_n(5), 15)

    def test_positive_medium_n_10(self):
            # Typical input, matches a docstring example
            self.assertEqual(mod.sum_to_n(10), 55)

    def test_positive_large_n_30(self):
            # Extreme/unusual input, matches a docstring example
            self.assertEqual(mod.sum_to_n(30), 465)

    def test_positive_large_n_100(self):
            # Extreme/unusual input, matches a docstring example
            self.assertEqual(mod.sum_to_n(100), 5050)

    def test_zero_n(self):
            # Boundary condition: n=0 (empty sum), edge case
            self.assertEqual(mod.sum_to_n(0), 0)

    def test_negative_n(self):
            # Sign testing: negative input, edge case
            # Sum from 1 to a negative number should typically be 0 (empty range)
            self.assertEqual(mod.sum_to_n(-5), 0)

    def test_large_positive_n_1000(self):
            # Extreme input to verify scalability and correctness for larger numbers
            self.assertEqual(mod.sum_to_n(1000), 500500)

    def test_normal_positive_30(self):
            """
            Test with a typical positive integer input: n = 30.
            Expected output: 465.
            """
            self.assertEqual(mod.sum_to_n(30), 465)

    def test_normal_positive_100(self):
            """
            Test with a larger positive integer input: n = 100.
            Expected output: 5050.
            """
            self.assertEqual(mod.sum_to_n(100), 5050)

    def test_normal_positive_5(self):
            """
            Test with another typical positive integer input: n = 5.
            Expected output: 15.
            """
            self.assertEqual(mod.sum_to_n(5), 15)

    def test_edge_zero(self):
            """
            Test with the smallest valid non-negative input: n = 0.
            Represents an empty sum, expected output: 0.
            """
            self.assertEqual(mod.sum_to_n(0), 0)

    def test_edge_one(self):
            """
            Test with the smallest positive integer input: n = 1.
            Sums only itself, expected output: 1.
            """
            self.assertEqual(mod.sum_to_n(1), 1)

    def test_error_float_input(self):
            """
            Test with a float input: n = 3.5.
            Should raise a TypeError as 'n' must be an integer.
            """
            with self.assertRaises(TypeError):
                mod.sum_to_n(3.5)

    def test_error_string_input(self):
            """
            Test with a string input: n = 'abc'.
            Should raise a TypeError as 'n' must be an integer.
            """
            with self.assertRaises(TypeError):
                mod.sum_to_n('abc')

