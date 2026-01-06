import unittest
import sut.problem_HumanEval_100 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_one_boundary_odd(self):
            # Boundary test: smallest positive integer n (odd)
            # Edge case: single element list
            self.assertListEqual(mod.make_a_pile(1), [1])

    def test_n_is_two_boundary_even(self):
            # Boundary test: smallest even positive integer n
            self.assertListEqual(mod.make_a_pile(2), [2, 4])

    def test_n_is_three_example_odd(self):
            # Typical input, matches docstring example (odd n)
            self.assertListEqual(mod.make_a_pile(3), [3, 5, 7])

    def test_n_is_four_typical_even(self):
            # Typical input (even n)
            self.assertListEqual(mod.make_a_pile(4), [4, 6, 8, 10])

    def test_n_is_five_typical_odd(self):
            # Typical input (odd n), slightly larger sequence
            self.assertListEqual(mod.make_a_pile(5), [5, 7, 9, 11, 13])

    def test_n_is_six_larger_even(self):
            # Larger input (even n), verifies sequence generation
            self.assertListEqual(mod.make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_n_is_seven_larger_odd(self):
            # Larger input (odd n), verifies sequence generation
            self.assertListEqual(mod.make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])

    def test_n_is_ten_extreme_even(self):
            # Extreme/unusual input (larger even n)
            self.assertListEqual(mod.make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_n_is_eleven_extreme_odd(self):
            # Extreme/unusual input (larger odd n)
            self.assertListEqual(mod.make_a_pile(11), [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])

    def test_n_is_eight_sequence_check_even(self):
            # Verifies the correct progression for an even n, catching off-by-one or step errors
            self.assertListEqual(mod.make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])

    def test_normal_odd_sequence(self):
            n = 3
            expected_output = [3, 5, 7]
            result = mod.make_a_pile(n)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), n)
            self.assertEqual(result[0], n)
            self.assertEqual(result, expected_output)
            for i in range(1, len(result)):
                self.assertEqual(result[i], result[i-1] + 2)
                self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_normal_even_sequence(self):
            n = 4
            expected_output = [4, 6, 8, 10]
            result = mod.make_a_pile(n)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), n)
            self.assertEqual(result[0], n)
            self.assertEqual(result, expected_output)
            for i in range(1, len(result)):
                self.assertEqual(result[i], result[i-1] + 2)
                self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_normal_another_odd_sequence(self):
            n = 5
            expected_output = [5, 7, 9, 11, 13]
            result = mod.make_a_pile(n)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), n)
            self.assertEqual(result[0], n)
            self.assertEqual(result, expected_output)
            for i in range(1, len(result)):
                self.assertEqual(result[i], result[i-1] + 2)
                self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_edge_smallest_positive_n(self):
            n = 1
            expected_output = [1]
            result = mod.make_a_pile(n)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), n)
            self.assertEqual(result[0], n)
            self.assertEqual(result, expected_output)
            # No subsequent elements to check difference for n=1
            self.assertEqual(result[0] % 2, n % 2) # Check parity

    def test_edge_smallest_even_n(self):
            n = 2
            expected_output = [2, 4]
            result = mod.make_a_pile(n)
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), n)
            self.assertEqual(result[0], n)
            self.assertEqual(result, expected_output)
            for i in range(1, len(result)):
                self.assertEqual(result[i], result[i-1] + 2)
                self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_error_n_is_float(self):
            with self.assertRaises((TypeError, AssertionError)):
                mod.make_a_pile(3.5)

    def test_error_n_is_string(self):
            with self.assertRaises((TypeError, AssertionError)):
                mod.make_a_pile("abc")

