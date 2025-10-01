import unittest
from sut.problem_HumanEval_103 import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_example_1(self):
        # Test case from docstring: average is an integer
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_example_2_n_greater_than_m(self):
        # Test case from docstring: n > m
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_example_3(self):
        # Test case from docstring: average is an integer
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_example_4_round_half_to_even(self):
        # Test case from docstring: average ends in .5, rounds to nearest even (down)
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_n_equals_m(self):
        # Test case where n and m are the same
        self.assertEqual(rounded_avg(5, 5), "0b101")

    def test_round_half_to_even_up(self):
        # Test case where average ends in .5, rounds to nearest even (up)
        # (1 + 2) / 2 = 1.5, round(1.5) = 2, bin(2) = "0b10"
        self.assertEqual(rounded_avg(1, 2), "0b10")

    def test_round_half_to_even_down_another_case(self):
        # Test case where average ends in .5, rounds to nearest even (down)
        # (2 + 3) / 2 = 2.5, round(2.5) = 2, bin(2) = "0b10"
        self.assertEqual(rounded_avg(2, 3), "0b10")

    def test_larger_range_integer_average(self):
        # Test with a larger range where the average is an integer
        # (100 + 150) / 2 = 125, bin(125) = "0b1111101"
        self.assertEqual(rounded_avg(100, 150), "0b1111101")

    def test_larger_range_round_half_to_even_down(self):
        # Test with a larger range where average ends in .5, rounds to nearest even (down)
        # (99 + 150) / 2 = 124.5, round(124.5) = 124, bin(124) = "0b1111100"
        self.assertEqual(rounded_avg(99, 150), "0b1111100")

    def test_larger_range_round_half_to_even_up(self):
        # Test with a larger range where average ends in .5, rounds to nearest even (up)
        # (100 + 151) / 2 = 125.5, round(125.5) = 126, bin(126) = "0b1111110"
        self.assertEqual(rounded_avg(100, 151), "0b1111110")

if __name__ == '__main__':
    unittest.main()