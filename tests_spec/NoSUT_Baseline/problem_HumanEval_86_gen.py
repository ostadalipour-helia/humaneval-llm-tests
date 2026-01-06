import unittest
import sut.problem_HumanEval_86 as mod

class TestHybrid(unittest.TestCase):
    def test_1_empty_string(self):
            # Edge Case: Empty string input
            # Catches: Incorrect handling of empty input, loop boundary issues.
            self.assertEqual(mod.anti_shuffle(''), '')

    def test_2_single_character_string(self):
            # Edge Case: Single character string
            # Catches: Off-by-one for single char word, loop boundary.
            self.assertEqual(mod.anti_shuffle('a'), 'a')

    def test_3_single_word_already_sorted(self):
            # Boundary Case: Single word, already in ascending ASCII order (from example)
            # Catches: Unnecessary sorting, incorrect comparison logic.
            self.assertEqual(mod.anti_shuffle('Hi'), 'Hi')

    def test_4_single_word_needs_sorting(self):
            # Typical Input: Single word that needs character sorting (from example)
            # Catches: Core sorting logic, character comparison.
            self.assertEqual(mod.anti_shuffle('hello'), 'ehllo')

    def test_5_multiple_words_mixed_sorting(self):
            # Typical Input: Multiple words, some sorted, some not (from example)
            # Catches: Word separation, individual word sorting, space preservation.
            self.assertEqual(mod.anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    def test_6_string_with_only_spaces(self):
            # Extreme Input: String consisting only of spaces
            # Catches: Handling of multiple consecutive spaces, empty words after splitting.
            self.assertEqual(mod.anti_shuffle('   '), '   ')

    def test_7_multiple_words_all_need_sorting(self):
            # Extreme Input: Multiple words, all of which need character sorting
            # Catches: Consistent application of sorting across all words.
            self.assertEqual(mod.anti_shuffle('olleh dlrow'), 'ehllo dlorw')

    def test_8_words_with_numbers_and_special_characters(self):
            # Unusual Input: Words containing numbers and special characters, already sorted
            # Catches: ASCII sorting behavior for non-alphabetic characters, handling of already sorted mixed types.
            self.assertEqual(mod.anti_shuffle('123 abc !!!'), '123 abc !!!')

    def test_10_leading_trailing_and_multiple_internal_spaces(self):
            # Boundary/Off-by-one Test: String with leading, trailing, and multiple internal spaces
            # Catches: Preservation of all types of spaces, off-by-one errors in splitting/joining.
            self.assertEqual(mod.anti_shuffle('  test   string  '), '  estt   ginrst  ')

    def test_normal_single_word_reorder(self):
            # A single word with characters needing reordering.
            self.assertEqual(mod.anti_shuffle("hello"), "ehllo")

    def test_normal_multiple_words_mixed(self):
            # Multiple words, some already sorted, some needing reordering, with special characters.
            # "Hello" is already sorted by ASCII (H, e, l, l, o).
            # "World!!!" sorted by ASCII is '!', '!', '!', 'W', 'd', 'l', 'o', 'r' -> "!!!Wdlor"
            self.assertEqual(mod.anti_shuffle("Hello World!!!"), "Hello !!!Wdlor")

    def test_normal_mixed_case(self):
            # Mixed case characters in a single word.
            # "aBcDeFg" sorted by ASCII is 'B', 'D', 'F', 'a', 'c', 'e', 'g' -> "BDFaceg"
            self.assertEqual(mod.anti_shuffle("aBcDeFg"), "BDFaceg")

    def test_edge_empty_string(self):
            # Empty string input.
            self.assertEqual(mod.anti_shuffle(""), "")

    def test_edge_already_sorted(self):
            # A single word that is already sorted.
            self.assertEqual(mod.anti_shuffle("Hi"), "Hi")

    def test_edge_only_spaces(self):
            # String containing only spaces.
            self.assertEqual(mod.anti_shuffle("   "), "   ")

    def test_edge_leading_trailing_spaces(self):
            # String with leading and trailing spaces.
            # "test" sorted by ASCII is 'e', 's', 't', 't' -> "estt"
            self.assertEqual(mod.anti_shuffle("  test  "), "  estt  ")

    def test_edge_multiple_spaces_between_words(self):
            # String with multiple spaces between words.
            # "one" sorted by ASCII is 'e', 'n', 'o' -> "eno"
            # "two" sorted by ASCII is 'o', 't', 'w' -> "otw"
            self.assertEqual(mod.anti_shuffle("one   two"), "eno   otw")

    def test_edge_special_characters(self):
            # String with only special characters.
            # "!@#$" sorted by ASCII is '!', '#', '$', '@' -> "!#$@"
            self.assertEqual(mod.anti_shuffle("!@#$"), "!#$@")

