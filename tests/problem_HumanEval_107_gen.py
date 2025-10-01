import unittest
from sut.problem_HumanEval_107 import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_n_is_1(self):
        # Palindromes in range(1, 1): 1 (odd)
        # Even: 0, Odd: 1
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_n_is_3_example(self):
        # Palindromes in range(1, 3): 1 (odd), 2 (even), 3 (odd)
        # Even: 1, Odd: 2
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_n_is_9_all_single_digit_palindromes(self):
        # Palindromes in range(1, 9): 1, 2, 3, 4, 5, 6, 7, 8, 9
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9 (5)
        self.assertEqual(even_odd_palindrome(9), (4, 5))

    def test_n_is_10_before_first_two_digit_palindrome(self):
        # Palindromes in range(1, 10): 1, 2, 3, 4, 5, 6, 7, 8, 9
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9 (5)
        self.assertEqual(even_odd_palindrome(10), (4, 5))

    def test_n_is_12_example(self):
        # Palindromes in range(1, 12): 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9, 11 (6)
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_n_is_25_includes_22(self):
        # Palindromes in range(1, 25): 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22
        # Even: 2, 4, 6, 8, 22 (5)
        # Odd: 1, 3, 5, 7, 9, 11 (6)
        self.assertEqual(even_odd_palindrome(25), (5, 6))

    def test_n_is_99_all_two_digit_palindromes(self):
        # Single-digit palindromes: (4 even, 5 odd)
        # Two-digit palindromes (11, 22, ..., 99): (4 even, 5 odd)
        # Total: (8 even, 10 odd)
        self.assertEqual(even_odd_palindrome(99), (8, 10))

    def test_n_is_100_before_first_three_digit_palindrome(self):
        # Same as n=99
        self.assertEqual(even_odd_palindrome(100), (8, 10))

    def test_n_is_101_first_three_digit_palindrome(self):
        # Palindromes up to 99: (8 even, 10 odd)
        # 101 (odd)
        # Total: (8 even, 11 odd)
        self.assertEqual(even_odd_palindrome(101), (8, 11))

    def test_n_is_1000_max_n(self):
        # Single-digit palindromes: (4 even, 5 odd)
        # Two-digit palindromes: (4 even, 5 odd)
        # Three-digit palindromes (101-999): (40 even, 50 odd)
        # Total: (4+4+40 even, 5+5+50 odd) = (48 even, 60 odd)
        self.assertEqual(even_odd_palindrome(1000), (48, 60))