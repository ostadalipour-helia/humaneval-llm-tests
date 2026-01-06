import unittest
from sut.problem_HumanEval_107 import even_odd_palindrome

class Test_even_odd_palindrome(unittest.TestCase):

    # Normal Cases
    def test_normal_n_3(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_normal_n_12(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_normal_n_50(self):
        self.assertEqual(even_odd_palindrome(50), (6, 7))

    # Edge Cases
    def test_edge_n_1(self):
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_edge_n_9(self):
        self.assertEqual(even_odd_palindrome(9), (4, 5))

    def test_edge_n_1000(self):
        # Palindromes up to 1000:
        # 1-digit: 1,2,3,4,5,6,7,8,9 (Even: 2,4,6,8 (4); Odd: 1,3,5,7,9 (5))
        # 2-digits: 11,22,33,44,55,66,77,88,99 (Even: 22,44,66,88 (4); Odd: 11,33,55,77,99 (5))
        # 3-digits: aba form. 'a' determines parity.
        #   'a' is even (2,4,6,8) -> 4 choices. 'b' is 0-9 -> 10 choices. Total 4*10 = 40 even.
        #   'a' is odd (1,3,5,7,9) -> 5 choices. 'b' is 0-9 -> 10 choices. Total 5*10 = 50 odd.
        # 4-digits: 1001 is the smallest, which is > 1000. So no 4-digit palindromes.
        # Total Even: 4 + 4 + 40 = 48
        # Total Odd: 5 + 5 + 50 = 60
        self.assertEqual(even_odd_palindrome(1000), (48, 60))

    # Error Cases
    def test_error_n_zero(self):
        with self.assertRaises(ValueError) as cm:
            even_odd_palindrome(0)
        self.assertIn("n must be a positive integer", str(cm.exception))

    def test_error_n_negative(self):
        with self.assertRaises(ValueError) as cm:
            even_odd_palindrome(-5)
        self.assertIn("n must be a positive integer", str(cm.exception))

    def test_error_n_too_large(self):
        with self.assertRaises(ValueError) as cm:
            even_odd_palindrome(1001)
        self.assertIn("n must not exceed 1000", str(cm.exception))

    def test_error_n_float(self):
        with self.assertRaises(TypeError) as cm:
            even_odd_palindrome(3.5)
        self.assertIn("n must be an integer", str(cm.exception))

    def test_error_n_string(self):
        with self.assertRaises(TypeError) as cm:
            even_odd_palindrome('abc')
        self.assertIn("n must be an integer", str(cm.exception))