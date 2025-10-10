import unittest
from sut_llm.problem_HumanEval_86 import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_1_empty_string(self):
        # Edge Case: Empty string input
        # Catches: Incorrect handling of empty input, loop boundary issues.
        self.assertEqual(anti_shuffle(''), '')

    def test_2_single_character_string(self):
        # Edge Case: Single character string
        # Catches: Off-by-one for single char word, loop boundary.
        self.assertEqual(anti_shuffle('a'), 'a')

    def test_3_single_word_already_sorted(self):
        # Boundary Case: Single word, already in ascending ASCII order (from example)
        # Catches: Unnecessary sorting, incorrect comparison logic.
        self.assertEqual(anti_shuffle('Hi'), 'Hi')

    def test_4_single_word_needs_sorting(self):
        # Typical Input: Single word that needs character sorting (from example)
        # Catches: Core sorting logic, character comparison.
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_5_multiple_words_mixed_sorting(self):
        # Typical Input: Multiple words, some sorted, some not (from example)
        # Catches: Word separation, individual word sorting, space preservation.
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    def test_6_string_with_only_spaces(self):
        # Extreme Input: String consisting only of spaces
        # Catches: Handling of multiple consecutive spaces, empty words after splitting.
        self.assertEqual(anti_shuffle('   '), '   ')

    def test_7_multiple_words_all_need_sorting(self):
        # Extreme Input: Multiple words, all of which need character sorting
        # Catches: Consistent application of sorting across all words.
        self.assertEqual(anti_shuffle('olleh dlrow'), 'ehllo dlorw')

    def test_8_words_with_numbers_and_special_characters(self):
        # Unusual Input: Words containing numbers and special characters, already sorted
        # Catches: ASCII sorting behavior for non-alphabetic characters, handling of already sorted mixed types.
        self.assertEqual(anti_shuffle('123 abc !!!'), '123 abc !!!')

    def test_9_words_with_duplicate_characters_and_mixed_case(self):
        # Logic Mutation Test: Words with duplicate characters and mixed case
        # Catches: Correct handling of duplicate characters, case sensitivity in ASCII sort.
        self.assertEqual(anti_shuffle('Banana Apple'), 'Baaann Aelpp')

    def test_10_leading_trailing_and_multiple_internal_spaces(self):
        # Boundary/Off-by-one Test: String with leading, trailing, and multiple internal spaces
        # Catches: Preservation of all types of spaces, off-by-one errors in splitting/joining.
        self.assertEqual(anti_shuffle('  test   string  '), '  estt   ginrst  ')