import unittest
from sut_llm.problem_HumanEval_117 import select_words

class TestSelectWords(unittest.TestCase):

    # Test 1: Empty string s (Edge Case, Return Value)
    # As per docstring, an empty string should return an empty list.
    def test_empty_string(self):
        self.assertListEqual(select_words("", 3), [])

    # Test 2: Basic example from docstring (Typical/Expected Input)
    # "little" has 'l', 't', 't', 'l' (4 consonants).
    def test_docstring_example_four_consonants(self):
        self.assertListEqual(select_words("Mary had a little lamb", 4), ["little"])

    # Test 3: Another basic example from docstring (Typical/Expected Input)
    # "Mary" has 'M', 'r', 'y' (3 consonants). "lamb" has 'l', 'm', 'b' (3 consonants).
    def test_docstring_example_three_consonants(self):
        self.assertListEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    # Test 4: No words match the given n (Return Value, Logic Mutation)
    # "simple" (s,m,p,l=4), "white" (w,h,t=3), "space" (s,p,c=3). None have exactly 2 consonants.
    def test_no_words_match_n(self):
        self.assertListEqual(select_words("simple white space", 2), [])

    # Test 5: Boundary condition n=0 (Boundary Testing, Sign and Zero Testing)
    # Words consisting only of vowels should have 0 consonants.
    def test_n_is_zero_all_vowels(self):
        self.assertListEqual(select_words("a e i o u", 0), ["a", "e", "i", "o", "u"])

    # Test 6: Boundary condition n=1 (Boundary Testing, Off-by-One Error)
    # Words with exactly one consonant.
    # "my" (m=1), "by" (b=1), "to" (t=1), "go" (g=1).
    def test_n_is_one_single_consonant_words(self):
        self.assertListEqual(select_words("my by to go", 1), ["to", "go"])
    def test_single_word_string_and_off_by_one_n(self):
        # The word "Programming" contains 8 consonants (P, r, g, r, m, m, n, g).
        # Test for n-1 (7 consonants)
        self.assertListEqual(select_words("Programming", 7), [])
        # Test for n (8 consonants)
        self.assertListEqual(select_words("Programming", 8), ["Programming"])
        # Test for n+1 (9 consonants)
        self.assertListEqual(select_words("Programming", 9), [])
    def test_multiple_and_leading_trailing_spaces(self):
        self.assertListEqual(select_words("  rhythm   sky  ", 6), ["rhythm"])
        self.assertListEqual(select_words("  rhythm   sky  ", 3), ["sky"])
        self.assertListEqual(select_words("  rhythm   sky  ", 5), []) # No match

    # Test 9: Case sensitivity of vowels/consonants (Logic Mutation, Extreme/Unusual Input)
    # Vowel/consonant check should be case-insensitive. "AEIOU" has 0 consonants. "BCDFG" has 5 consonants.
    def test_case_sensitivity_of_consonants(self):
        self.assertListEqual(select_words("AEIOU BCDFG", 0), ["AEIOU"])
        self.assertListEqual(select_words("AEIOU BCDFG", 5), ["BCDFG"])
        self.assertListEqual(select_words("aEiOu bCdFg", 0), ["aEiOu"])
        self.assertListEqual(select_words("aEiOu bCdFg", 5), ["bCdFg"])

    # Test 10: Very long word and n too large/small (Boundary Testing, Extreme/Unusual Input)
    # "pneumonoultramicroscopicsilicovolcanoconiosis" has 25 consonants.
    # Test with n=25 (exact match), n=24 (one less), and n=26 (one more).
    def test_very_long_word_and_n_off_by_one(self):
        long_word = "pneumonoultramicroscopicsilicovolcanoconiosis"
        # Consonants: p,n,m,n,l,t,r,m,c,r,s,c,p,c,s,l,c,v,l,c,n,c,n,s,s (25)
        self.assertListEqual(select_words(long_word, 25), [long_word])
        self.assertListEqual(select_words(long_word, 26), []) # n+1
        self.assertListEqual(select_words(long_word, 24), []) # n-1