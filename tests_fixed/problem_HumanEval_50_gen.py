import unittest
from sut_llm.problem_HumanEval_50 import decode_shift

class TestDecodeShift(unittest.TestCase):

    def test_01_basic_decode_simple_string(self):
        """
        Tests basic decoding of a common string.
        (Typical/Expected Input)
        """
        self.assertEqual(decode_shift("fghij"), "abcde")

    def test_02_decode_wraparound_from_z(self):
        """
        Tests decoding characters that wrap around from the end of the alphabet (e.g., 'x', 'y', 'z').
        (Boundary Condition, Extreme Input, Logic Mutation)
        """
        self.assertEqual(decode_shift("cde"), "xyz")

    def test_03_decode_wraparound_to_a(self):
        """
        Tests decoding characters that wrap around to the beginning of the alphabet (e.g., 'a', 'b', 'c').
        (Boundary Condition, Extreme Input, Logic Mutation)
        """
        self.assertEqual(decode_shift("fgh"), "abc")

    def test_04_empty_string(self):
        """
        Tests the function with an empty input string.
        (Edge Case)
        """
        self.assertEqual(decode_shift(""), "")

    def test_05_single_char_decodes_to_a(self):
        """
        Tests decoding a single character that results in 'a' (the first letter).
        (Boundary Condition, Off-by-One Error, Edge Case - single element)
        """
        self.assertEqual(decode_shift("f"), "a")

    def test_06_single_char_decodes_to_z(self):
        """
        Tests decoding a single character that results in 'z' (the last letter), involving wrap-around.
        (Boundary Condition, Off-by-One Error, Edge Case - single element)
        """
        self.assertEqual(decode_shift("e"), "z")

    def test_07_string_with_all_same_characters(self):
        """
        Tests decoding a string where all characters are identical.
        (Edge Case - all same values, Typical Input)
        """
        self.assertEqual(decode_shift("jjjjj"), "eeeee")

    def test_08_full_alphabet_cycle(self):
        """
        Tests decoding a string that represents the entire alphabet, covering all characters and wrap-arounds.
        (Extreme Input, Logic Mutation)
        """
        encoded_alphabet = "fghijklmnopqrstuvwxyzabcde"
        decoded_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(decode_shift(encoded_alphabet), decoded_alphabet)

    def test_09_chars_around_wraparound_boundaries(self):
        """
        Tests characters immediately adjacent to the wrap-around points ('a' and 'z').
        'd' -> 'y', 'e' -> 'z', 'f' -> 'a', 'g' -> 'b'.
        (Boundary Condition, Off-by-One Error)
        """
        self.assertEqual(decode_shift("defg"), "yzab")

    def test_10_string_with_duplicate_patterns(self):
        """
        Tests decoding a string with repeating patterns and duplicate characters.
        (Typical/Expected Input, Logic Mutation)
        """
        self.assertEqual(decode_shift("fghfgh"), "abcabc")