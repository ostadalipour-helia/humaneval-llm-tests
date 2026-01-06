import unittest
import sut.problem_HumanEval_123 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_one_boundary_case(self):
            # Boundary: Smallest positive integer, explicit base case.
            # Sequence for 1 is [1]. Odd numbers: [1].
            self.assertListEqual(mod.get_odd_collatz(1), [1])

    def test_n_is_two_smallest_even(self):
            # Boundary: Smallest even number.
            # Sequence for 2 is [2, 1]. Odd numbers: [1].
            self.assertListEqual(mod.get_odd_collatz(2), [1])

    def test_n_is_three_smallest_odd_greater_than_one(self):
            # Boundary: Smallest odd number > 1, leads to a longer sequence.
            # Sequence for 3 is [3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers: [1, 3, 5].
            self.assertListEqual(mod.get_odd_collatz(3), [1, 3, 5])

    def test_n_is_four_power_of_two_edge_case(self):
            # Edge Case: Power of two, sequence quickly reaches 1, only 1 is odd.
            # Sequence for 4 is [4, 2, 1]. Odd numbers: [1].
            self.assertListEqual(mod.get_odd_collatz(4), [1])

    def test_n_is_five_docstring_example(self):
            # Typical Input: Example from docstring.
            # Sequence for 5 is [5, 16, 8, 4, 2, 1]. Odd numbers: [1, 5].
            self.assertListEqual(mod.get_odd_collatz(5), [1, 5])

    def test_n_is_six_even_leading_to_odd(self):
            # Typical Input: Even number that leads to an odd number other than 1.
            # Sequence for 6 is [6, 3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers: [1, 3, 5].
            self.assertListEqual(mod.get_odd_collatz(6), [1, 3, 5])

    def test_n_is_seven_longer_sequence(self):
            # Typical Input: Odd number leading to a moderately long sequence.
            # Sequence for 7 is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
            # Odd numbers: [1, 5, 7, 11, 13, 17].
            self.assertListEqual(mod.get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_n_is_eight_another_power_of_two(self):
            # Edge Case: Another power of two, only 1 is odd.
            # Sequence for 8 is [8, 4, 2, 1]. Odd numbers: [1].
            self.assertListEqual(mod.get_odd_collatz(8), [1])

    def test_n_large_even_extreme_input(self):
            # Extreme Input: A moderately large even number.
            # Sequence for 100 is [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
            # Odd numbers: [1, 5, 11, 13, 17, 19, 25, 29].
            self.assertListEqual(mod.get_odd_collatz(100), [1, 5, 11, 13, 17, 19, 25, 29])

    def test_normal_five(self):
            # Collatz sequence for 5 is [5, 16, 8, 4, 2, 1]. Odd numbers are 1, 5. Sorted: [1, 5].
            self.assertEqual(mod.get_odd_collatz(5), [1, 5])

    def test_normal_six(self):
            # Collatz sequence for 6 is [6, 3, 10, 5, 16, 8, 4, 2, 1]. Odd numbers are 1, 3, 5. Sorted: [1, 3, 5].
            self.assertEqual(mod.get_odd_collatz(6), [1, 3, 5])

    def test_normal_seven(self):
            # Collatz sequence for 7 is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1].
            # Odd numbers are 1, 5, 7, 11, 13, 17. Sorted: [1, 5, 7, 11, 13, 17].
            self.assertEqual(mod.get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_edge_one(self):
            # The smallest positive integer. Collatz sequence for 1 is [1]. Odd numbers are 1. Sorted: [1].
            self.assertEqual(mod.get_odd_collatz(1), [1])

    def test_edge_two(self):
            # An even number that quickly reaches 1. Collatz sequence for 2 is [2, 1]. Odd numbers are 1. Sorted: [1].
            self.assertEqual(mod.get_odd_collatz(2), [1])

    def test_error_string(self):
            # n must be an integer.
            with self.assertRaises(TypeError):
                mod.get_odd_collatz('abc')

