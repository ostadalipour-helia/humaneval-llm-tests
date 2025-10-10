import unittest
from sut_llm.problem_HumanEval_125 import split_words

class TestSplitWords(unittest.TestCase):

    def test_whitespace_split_typical(self):
        # CRITICAL: Typical input, Return Value Testing (list)
        # SPECIFIC: Typical/expected inputs
        self.assertListEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split_typical(self):
        # CRITICAL: Typical input, Return Value Testing (list)
        # SPECIFIC: Typical/expected inputs
        self.assertListEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_odd_order_count_typical(self):
        # CRITICAL: Typical input, Return Value Testing (integer)
        # SPECIFIC: Typical/expected inputs
        self.assertEqual(split_words("abcdef"), 3) # b=1, d=3, f=5 are odd

    def test_whitespace_split_multiple_spaces_and_trim(self):
        # CRITICAL: Boundary Testing (multiple spaces), Off-by-One Errors (leading/trailing/extra spaces)
        # SPECIFIC: Boundary conditions, Extreme/unusual inputs
        self.assertListEqual(split_words("  leading  middle   trailing  "), ["leading", "middle", "trailing"])

    def test_comma_split_multiple_commas_and_empty_parts(self):
        # CRITICAL: Boundary Testing (multiple commas), Off-by-One Errors (leading/trailing/extra commas)
        # SPECIFIC: Boundary conditions, Extreme/unusual inputs
        self.assertListEqual(split_words(",word1,,word2,"), ["", "word1", "", "word2", ""])

    def test_edge_empty_string(self):
        # CRITICAL: Edge Cases (empty collection), Return Value Testing (default/computed 0)
        # SPECIFIC: Edge cases (empty)
        self.assertEqual(split_words(""), 0)

    def test_edge_single_word_no_split(self):
        # CRITICAL: Edge Cases (single element collection), Return Value Testing (computed value)
        # SPECIFIC: Edge cases (single element)
        self.assertEqual(split_words("Python"), 3) # 't'=19, 'h'=7, 'n'=13 are odd

    def test_logic_priority_whitespace_over_comma(self):
        # CRITICAL: Logic Mutations (ensures whitespace check precedes comma check)
        # SPECIFIC: Extreme/unusual inputs (mixed delimiters)
        self.assertListEqual(split_words("Hello, world!"), ["Hello,", "world!"])

    def test_extreme_non_alphabetic_for_count(self):
        # CRITICAL: Edge Cases (string with only special characters/numbers), Sign and Zero Testing (result 0)
        # SPECIFIC: Extreme/unusual inputs
        self.assertEqual(split_words("!@#$123"), 0)

    def test_boundary_odd_order_count_all_even_letters(self):
        # CRITICAL: Boundary Testing (0 odd-ordered letters), Off-by-One Errors (letters just missing odd order)
        # SPECIFIC: Boundary conditions
        self.assertEqual(split_words("acegik"), 0) # a=0, c=2, e=4, g=6, i=8, k=10 are all even