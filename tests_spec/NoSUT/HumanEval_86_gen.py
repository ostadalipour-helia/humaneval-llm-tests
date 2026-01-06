import unittest
from sut.problem_HumanEval_86 import anti_shuffle

class Test_anti_shuffle(unittest.TestCase):
    def test_normal_single_word_reorder(self):
        # A single word with characters needing reordering.
        self.assertEqual(anti_shuffle("hello"), "ehllo")

    def test_normal_multiple_words_mixed(self):
        # Multiple words, some already sorted, some needing reordering, with special characters.
        # "Hello" is already sorted by ASCII (H, e, l, l, o).
        # "World!!!" sorted by ASCII is '!', '!', '!', 'W', 'd', 'l', 'o', 'r' -> "!!!Wdlor"
        self.assertEqual(anti_shuffle("Hello World!!!"), "Hello !!!Wdlor")

    def test_normal_multiple_words_all_reorder(self):
        # Multiple words, all needing reordering.
        # "Python" sorted by ASCII is 'h', 'n', 'o', 'P', 't', 'y' -> "hnoPty"
        # "is" sorted by ASCII is 'i', 's' -> "is"
        # "fun" sorted by ASCII is 'f', 'n', 'u' -> "fnu"
        self.assertEqual(anti_shuffle("Python is fun"), "hnoPty is fnu")

    def test_normal_mixed_case(self):
        # Mixed case characters in a single word.
        # "aBcDeFg" sorted by ASCII is 'B', 'D', 'F', 'a', 'c', 'e', 'g' -> "BDFaceg"
        self.assertEqual(anti_shuffle("aBcDeFg"), "BDFaceg")

    def test_edge_empty_string(self):
        # Empty string input.
        self.assertEqual(anti_shuffle(""), "")

    def test_edge_already_sorted(self):
        # A single word that is already sorted.
        self.assertEqual(anti_shuffle("Hi"), "Hi")

    def test_edge_only_spaces(self):
        # String containing only spaces.
        self.assertEqual(anti_shuffle("   "), "   ")

    def test_edge_leading_trailing_spaces(self):
        # String with leading and trailing spaces.
        # "test" sorted by ASCII is 'e', 's', 't', 't' -> "estt"
        self.assertEqual(anti_shuffle("  test  "), "  estt  ")

    def test_edge_multiple_spaces_between_words(self):
        # String with multiple spaces between words.
        # "one" sorted by ASCII is 'e', 'n', 'o' -> "eno"
        # "two" sorted by ASCII is 'o', 't', 'w' -> "otw"
        self.assertEqual(anti_shuffle("one   two"), "eno   otw")

    def test_edge_special_characters(self):
        # String with only special characters.
        # "!@#$" sorted by ASCII is '!', '#', '$', '@' -> "!#$@"
        self.assertEqual(anti_shuffle("!@#$"), "!#$@")

    def test_error_integer_input(self):
        # Input is an integer instead of a string.
        with self.assertRaises(TypeError):
            anti_shuffle(123)

    def test_error_none_input(self):
        # Input is None instead of a string.
        with self.assertRaises(TypeError):
            anti_shuffle(None)

    def test_error_list_input(self):
        # Input is a list instead of a string.
        with self.assertRaises(TypeError):
            anti_shuffle(["hello", "world"])