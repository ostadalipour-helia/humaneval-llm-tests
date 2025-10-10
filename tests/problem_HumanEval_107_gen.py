import unittest
from sut.problem_HumanEval_107 import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_min_n_boundary(self):
        # Test with the minimum allowed value for n (n=1)
        # Palindromes in range(1, 1): [1]
        # 1 is odd.
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_n_equals_2_edge_case(self):
        # Test with n=2, a small edge case
        # Palindromes in range(1, 2): [1, 2]
        # 1 is odd, 2 is even.
        self.assertEqual(even_odd_palindrome(2), (1, 1))

    def test_example_n_3(self):
        # Test with the first example from the docstring
        # Palindromes in range(1, 3): [1, 2, 3]
        # 1 is odd, 2 is even, 3 is odd.
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_n_just_before_two_digit_palindrome(self):
        # Test n=10, where all single-digit numbers are palindromes, but 10 is not.
        # Palindromes in range(1, 10): [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9 (5)
        self.assertEqual(even_odd_palindrome(10), (4, 5))

    def test_n_first_two_digit_palindrome(self):
        # Test n=11, which includes the first two-digit palindrome (11).
        # Palindromes in range(1, 11): [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9, 11 (6)
        self.assertEqual(even_odd_palindrome(11), (4, 6))

    def test_example_n_12(self):
        # Test with the second example from the docstring
        # Palindromes in range(1, 12): [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        # Even: 2, 4, 6, 8 (4)
        # Odd: 1, 3, 5, 7, 9, 11 (6)
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_n_mid_range_with_two_digit_palindromes(self):
        # Test a typical mid-range value (n=50) to include more two-digit palindromes.
        # Palindromes in range(1, 50): [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44]
        # Even: 2, 4, 6, 8, 22, 44 (6)
        # Odd: 1, 3, 5, 7, 9, 11, 33 (7)
        self.assertEqual(even_odd_palindrome(50), (6, 7))

    def test_n_last_two_digit_palindrome_boundary(self):
        # Test n=99, which includes all two-digit palindromes.
        # Palindromes in range(1, 99): [1-9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
        # Even: 2, 4, 6, 8, 22, 44, 66, 88 (8)
        # Odd: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99 (10)
        self.assertEqual(even_odd_palindrome(99), (8, 10))

    def test_n_first_three_digit_palindrome_boundary(self):
        # Test n=101, which includes the first three-digit palindrome (101).
        # Palindromes in range(1, 101): [1-9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101]
        # Even: 2, 4, 6, 8, 22, 44, 66, 88 (8)
        # Odd: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99, 101 (11)
        self.assertEqual(even_odd_palindrome(101), (8, 11))

    def test_max_n_boundary(self):
        # Test with the maximum allowed value for n (n=1000)
        # Palindromes up to 1000:
        # 1-digit: 1,2,3,4,5,6,7,8,9 (4 even, 5 odd)
        # 2-digits: 11,22,33,44,55,66,77,88,99 (4 even, 5 odd)
        # 3-digits: 101,111,...,191, 202,...,292, ..., 909,...,999
        #   - Even 3-digit palindromes (A_A where A is even): 202,212,...,292 (10) + 404,...,494 (10) + 606,...,696 (10) + 808,...,898 (10) = 40
        #   - Odd 3-digit palindromes (A_A where A is odd): 101,...,191 (10) + 303,...,393 (10) + 505,...,595 (10) + 707,...,797 (10) + 909,...,999 (10) = 50
        # Total Even: 4 + 4 + 40 = 48
        # Total Odd: 5 + 5 + 50 = 60
        self.assertEqual(even_odd_palindrome(1000), (48, 60))