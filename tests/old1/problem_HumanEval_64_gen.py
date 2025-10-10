import unittest
from sut.problem_HumanEval_64 import vowels_count

class TestVowelsCount(unittest.TestCase):

    def test_basic_standard_vowels(self):
        self.assertEqual(vowels_count("apple"), 2)

    def test_uppercase_standard_vowels(self):
        self.assertEqual(vowels_count("ORANGE"), 3)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("rhythm"), 0)

    def test_all_standard_vowels_mixed_case(self):
        self.assertEqual(vowels_count("aeiouAEIOU"), 10)

    def test_y_at_the_end(self):
        self.assertEqual(vowels_count("happy"), 2)

    def test_y_not_at_the_end_middle(self):
        self.assertEqual(vowels_count("system"), 1)

    def test_y_at_the_beginning(self):
        self.assertEqual(vowels_count("yellow"), 2)

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_single_character_y(self):
        self.assertEqual(vowels_count("y"), 1)

    def test_multiple_ys_only_one_at_end(self):
        self.assertEqual(vowels_count("syzygy"), 1)

if __name__ == '__main__':
    unittest.main()