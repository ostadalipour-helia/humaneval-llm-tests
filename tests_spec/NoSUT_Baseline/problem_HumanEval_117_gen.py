import unittest
import sut.problem_HumanEval_117 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            self.assertListEqual(mod.select_words("", 3), [])
    
        # Test 2: Basic example from docstring (Typical/Expected Input)
        # "little" has 'l', 't', 't', 'l' (4 consonants).

    def test_docstring_example_four_consonants(self):
            self.assertListEqual(mod.select_words("Mary had a little lamb", 4), ["little"])
    
        # Test 3: Another basic example from docstring (Typical/Expected Input)
        # "Mary" has 'M', 'r', 'y' (3 consonants). "lamb" has 'l', 'm', 'b' (3 consonants).

    def test_docstring_example_three_consonants(self):
            self.assertListEqual(mod.select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
    
        # Test 4: No words match the given n (Return Value, Logic Mutation)
        # "simple" (s,m,p,l=4), "white" (w,h,t=3), "space" (s,p,c=3). None have exactly 2 consonants.

    def test_no_words_match_n(self):
            self.assertListEqual(mod.select_words("simple white space", 2), [])
    
        # Test 5: Boundary condition n=0 (Boundary Testing, Sign and Zero Testing)
        # Words consisting only of vowels should have 0 consonants.

    def test_n_is_zero_all_vowels(self):
            self.assertListEqual(mod.select_words("a e i o u", 0), ["a", "e", "i", "o", "u"])
    
        # Test 6: Boundary condition n=1 (Boundary Testing, Off-by-One Error)
        # Words with exactly one consonant.
        # "my" (m=1), "by" (b=1), "to" (t=1), "go" (g=1).

    def test_multiple_and_leading_trailing_spaces(self):
            self.assertListEqual(mod.select_words("  rhythm   sky  ", 6), ["rhythm"])
            self.assertListEqual(mod.select_words("  rhythm   sky  ", 3), ["sky"])
            self.assertListEqual(mod.select_words("  rhythm   sky  ", 5), []) # No match
    
        # Test 9: Case sensitivity of vowels/consonants (Logic Mutation, Extreme/Unusual Input)
        # Vowel/consonant check should be case-insensitive. "AEIOU" has 0 consonants. "BCDFG" has 5 consonants.

    def test_case_sensitivity_of_consonants(self):
            self.assertListEqual(mod.select_words("AEIOU BCDFG", 0), ["AEIOU"])
            self.assertListEqual(mod.select_words("AEIOU BCDFG", 5), ["BCDFG"])
            self.assertListEqual(mod.select_words("aEiOu bCdFg", 0), ["aEiOu"])
            self.assertListEqual(mod.select_words("aEiOu bCdFg", 5), ["bCdFg"])
    
        # Test 10: Very long word and n too large/small (Boundary Testing, Extreme/Unusual Input)
        # "pneumonoultramicroscopicsilicovolcanoconiosis" has 25 consonants.
        # Test with n=25 (exact match), n=24 (one less), and n=26 (one more).

    def test_very_long_word_and_n_off_by_one(self):
            long_word = "pneumonoultramicroscopicsilicovolcanoconiosis"
            # Consonants: p,n,m,n,l,t,r,m,c,r,s,c,p,c,s,l,c,v,l,c,n,c,n,s,s (25)
            self.assertListEqual(mod.select_words(long_word, 25), [long_word])
            self.assertListEqual(mod.select_words(long_word, 26), []) # n+1
            self.assertListEqual(mod.select_words(long_word, 24), []) # n-1

    def test_normal_one_matching_word(self):
            # Standard case with one matching word.
            s = "Mary had a little lamb"
            n = 4
            expected_output = ["little"]
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_normal_multiple_matching_words(self):
            # Standard case with multiple matching words.
            s = "Mary had a little lamb"
            n = 3
            expected_output = ["Mary", "lamb"]
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_normal_capitalized_word(self):
            # Standard case with a capitalized word.
            s = "Uncle sam"
            n = 3
            expected_output = ["Uncle"]
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_edge_empty_input_string_n0(self):
            # Empty input string 's' with n=0.
            s = ""
            n = 0
            expected_output = []
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_edge_empty_input_string_n_nonzero(self):
            # Empty input string 's' with non-zero 'n'.
            s = ""
            n = 5
            expected_output = []
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_edge_words_only_vowels_n0(self):
            # Words consisting only of vowels, 'n' is 0.
            s = "a e i o u"
            n = 0
            expected_output = ["a", "e", "i", "o", "u"]
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_edge_word_only_consonants_match(self):
            # Word consisting only of consonants, 'n' matches.
            s = "rhythm"
            n = 6
            expected_output = ["rhythm"]
            self.assertEqual(mod.select_words(s, n), expected_output)

    def test_edge_string_only_spaces(self):
            # String containing only spaces.
            s = "   "
            n = 1
            expected_output = []
            self.assertEqual(mod.select_words(s, n), expected_output)

