import unittest
from sut_llm.problem_HumanEval_131 import digits

class TestDigits(unittest.TestCase):

    def test_single_odd_digit(self):
        self.assertEqual(digits(1), 1)

    def test_single_even_digit(self):
        self.assertEqual(digits(4), 0)

    def test_mixed_digits_example(self):
        self.assertEqual(digits(235), 15)

    def test_all_even_digits(self):
        self.assertEqual(digits(246), 0)

    def test_all_odd_digits(self):
        self.assertEqual(digits(135), 15)

    def test_mixed_digits_starting_even(self):
        self.assertEqual(digits(213), 3)

    def test_mixed_digits_ending_even(self):
        self.assertEqual(digits(132), 3)

    def test_large_number_all_odd(self):
        self.assertEqual(digits(13579), 945) # 1*3*5*7*9

    def test_large_number_all_even_including_zero(self):
        self.assertEqual(digits(24680), 0)

    def test_large_number_mixed_digits(self):
        self.assertEqual(digits(123456789), 945) # 1*3*5*7*9

if __name__ == '__main__':
    unittest.main()