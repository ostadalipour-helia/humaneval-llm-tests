import unittest
from sut.problem_HumanEval_38 import decode_cyclic

class Test_decode_cyclic(unittest.TestCase):
    def test_multiple_full_groups(self):
        """
        Input string consists of multiple full groups of three characters.
        'bca' -> 'abc', 'efd' -> 'def', 'hig' -> 'ghi'
        """
        self.assertEqual(decode_cyclic("bcaefdhig"), "abcdefghi")

    def test_multiple_full_and_two_char_partial(self):
        """
        Input string consists of multiple full groups and one partial group of two characters at the end.
        'bca' -> 'abc', 'efd' -> 'def', 'gh' -> 'gh'
        """
        self.assertEqual(decode_cyclic("bcaefdgh"), "abcdefgh")

    def test_multiple_full_and_one_char_partial(self):
        """
        Input string consists of multiple full groups and one partial group of one character at the end.
        'bca' -> 'abc', 'efd' -> 'def', 'g' -> 'g'
        """
        self.assertEqual(decode_cyclic("bcaefdg"), "abcdefg")

    def test_single_full_group(self):
        """
        Input string consists of a single full group of three characters.
        'bca' -> 'abc'
        """
        self.assertEqual(decode_cyclic("bca"), "abc")

    def test_empty_string(self):
        """
        Empty input string.
        """
        self.assertEqual(decode_cyclic(""), "")

    def test_single_two_char_group(self):
        """
        Input string consists of a single partial group of two characters (unchanged by encode/decode).
        """
        self.assertEqual(decode_cyclic("ab"), "ab")

    def test_single_one_char_group(self):
        """
        Input string consists of a single partial group of one character (unchanged by encode/decode).
        """
        self.assertEqual(decode_cyclic("a"), "a")

    def test_one_full_and_two_char_partial(self):
        """
        Input string consists of one full group and one partial group of two characters.
        'bca' -> 'abc', 'de' -> 'de'
        """
        self.assertEqual(decode_cyclic("bcade"), "abcde")

    def test_one_full_and_one_char_partial(self):
        """
        Input string consists of one full group and one partial group of one character.
        'bca' -> 'abc', 'd' -> 'd'
        """
        self.assertEqual(decode_cyclic("bcad"), "abcd")

    def test_input_not_string_int(self):
        """
        Input is not a string (integer).
        """
        with self.assertRaises(TypeError):
            decode_cyclic(123)

    def test_input_none(self):
        """
        Input is None.
        """
        with self.assertRaises(TypeError):
            decode_cyclic(None)

    def test_input_not_string_list(self):
        """
        Input is a list, not a string.
        """
        with self.assertRaises(TypeError):
            decode_cyclic(["a", "b", "c"])