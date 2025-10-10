import unittest
from sut_llm.problem_HumanEval_100 import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_n_is_one_boundary_odd(self):
        # Boundary test: smallest positive integer n (odd)
        # Edge case: single element list
        self.assertListEqual(make_a_pile(1), [1])

    def test_n_is_two_boundary_even(self):
        # Boundary test: smallest even positive integer n
        self.assertListEqual(make_a_pile(2), [2, 4])

    def test_n_is_three_example_odd(self):
        # Typical input, matches docstring example (odd n)
        self.assertListEqual(make_a_pile(3), [3, 5, 7])

    def test_n_is_four_typical_even(self):
        # Typical input (even n)
        self.assertListEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_n_is_five_typical_odd(self):
        # Typical input (odd n), slightly larger sequence
        self.assertListEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_n_is_six_larger_even(self):
        # Larger input (even n), verifies sequence generation
        self.assertListEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])

    def test_n_is_seven_larger_odd(self):
        # Larger input (odd n), verifies sequence generation
        self.assertListEqual(make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])

    def test_n_is_ten_extreme_even(self):
        # Extreme/unusual input (larger even n)
        self.assertListEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_n_is_eleven_extreme_odd(self):
        # Extreme/unusual input (larger odd n)
        self.assertListEqual(make_a_pile(11), [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])

    def test_n_is_eight_sequence_check_even(self):
        # Verifies the correct progression for an even n, catching off-by-one or step errors
        self.assertListEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])