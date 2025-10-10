import unittest
from sut_llm.problem_HumanEval_113 import odd_count

class TestOddCount(unittest.TestCase):

    def test_example_one(self):
        # Test case from the docstring example 1
        self.assertEqual(odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])

    def test_example_two(self):
        # Test case from the docstring example 2
        self.assertEqual(odd_count(['3',"11111111"]), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."])

    def test_empty_list(self):
        # Edge case: empty input list
        self.assertEqual(odd_count([]), [])

    def test_list_with_empty_strings(self):
        # Edge case: list containing empty strings, tests count 0
        self.assertEqual(odd_count(['', '']), ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_all_even_digits(self):
        # Boundary condition: string with no odd digits (count 0)
        self.assertEqual(odd_count(['24680']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

    def test_all_odd_digits(self):
        # Boundary condition: string with all odd digits (max count for its length)
        self.assertEqual(odd_count(['13579']), ["the number of odd elements 5n the str5ng 5 of the 5nput."])

    def test_single_digit_strings(self):
        # Off-by-one/Boundary: list of single-digit strings (mix of odd/even)
        self.assertEqual(odd_count(['1', '2', '3', '0']), [
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 0n the str0ng 0 of the 0nput."
        ])

    def test_long_string_mixed_digits(self):
        # Extreme input: a very long string with mixed odd/even digits
        # Count of odd digits in '12345678901234567890' is 10
        self.assertEqual(odd_count(['12345678901234567890']), ["the number of odd elements 10n the str10ng 10 of the 10nput."])

    def test_duplicate_strings(self):
        # Edge case: list with duplicate strings to ensure independent processing
        self.assertEqual(odd_count(['12', '34', '12']), [
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput."
        ])

    def test_zero_digit_string(self):
        # Boundary/Off-by-one: string containing only '0' (which is even)
        self.assertEqual(odd_count(['000']), ["the number of odd elements 0n the str0ng 0 of the 0nput."])

if __name__ == '__main__':
    unittest.main()