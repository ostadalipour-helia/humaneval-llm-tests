import unittest
from sut_llm.problem_HumanEval_155 import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_example_positive(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_example_negative(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_single_even_digit(self):
        self.assertEqual(even_odd_count(4), (1, 0))

    def test_single_odd_digit(self):
        self.assertEqual(even_odd_count(7), (0, 1))

    def test_mixed_digits_with_zero(self):
        self.assertEqual(even_odd_count(1024), (3, 1))

    def test_all_odd_digits(self):
        self.assertEqual(even_odd_count(13579), (0, 5))

    def test_all_even_digits(self):
        self.assertEqual(even_odd_count(24680), (5, 0))

    def test_large_negative_mixed_digits(self):
        self.assertEqual(even_odd_count(-987654321), (4, 5))

    def test_number_with_many_zeros(self):
        self.assertEqual(even_odd_count(1000000000), (9, 1))

if __name__ == '__main__':
    unittest.main()