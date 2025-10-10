import unittest
from sut.problem_HumanEval_98 import count_upper

class TestCountUpper(unittest.TestCase):

    def test_docstring_example_1(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_docstring_example_2(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_docstring_example_3(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_single_uppercase_vowel_at_even_index(self):
        self.assertEqual(count_upper('A'), 1)

    def test_single_lowercase_consonant_at_even_index(self):
        self.assertEqual(count_upper('b'), 0)

    def test_mixed_case_with_one_match(self):
        self.assertEqual(count_upper('PYTHON'), 1) # O at index 4

    def test_multiple_uppercase_vowels_at_even_indices(self):
        self.assertEqual(count_upper('AEIOU'), 3) # A at 0, I at 2, U at 4

    def test_all_lowercase_vowels(self):
        self.assertEqual(count_upper('aeiou'), 0)

    def test_uppercase_vowels_only_at_odd_indices(self):
        self.assertEqual(count_upper('bAeIoU'), 0) # A at 1, I at 3, U at 5

if __name__ == '__main__':
    unittest.main()