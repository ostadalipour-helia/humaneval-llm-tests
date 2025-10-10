import unittest
from sut_llm.problem_HumanEval_118 import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_example_yogurt(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_example_full(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_example_quick(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_example_ab(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_rightmost_c_v_c(self):
        # 'e' is the rightmost vowel between two consonants ('c' and 'r')
        self.assertEqual(get_closest_vowel("racer"), "e")

    def test_multiple_c_v_c_pick_rightmost(self):
        # 'u' is between 'f' and 'l', 'i' is between 't' and 'f'. 'u' is rightmost.
        self.assertEqual(get_closest_vowel("beautiful"), "u")

    def test_case_sensitivity_rightmost(self):
        # 'E' is between 'c' and 'r'. 'A' is between 'r' and 'c'. 'E' is rightmost.
        self.assertEqual(get_closest_vowel("rAcEr"), "E")

    def test_no_vowels(self):
        self.assertEqual(get_closest_vowel("rhythm"), "")

    def test_short_c_v_c_word(self):
        self.assertEqual(get_closest_vowel("top"), "o")

    def test_all_vowels_no_c_v_c(self):
        # Vowels at beginning/end don't count, and no consonants to sandwich them
        self.assertEqual(get_closest_vowel("aeiou"), "")

if __name__ == '__main__':
    unittest.main()