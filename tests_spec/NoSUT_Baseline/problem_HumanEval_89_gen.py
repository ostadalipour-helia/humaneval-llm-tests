import unittest
import sut.problem_HumanEval_89 as mod

class TestHybrid(unittest.TestCase):
    def test_example_hi(self):
            # Typical input, given example
            self.assertEqual(mod.encrypt('hi'), 'lm')

    def test_example_asdfghjkl(self):
            # Typical input, given example
            self.assertEqual(mod.encrypt('asdfghjkl'), 'ewhjklnop')

    def test_empty_string(self):
            # Edge case: empty string
            self.assertEqual(mod.encrypt(''), '')

    def test_single_char_a_boundary(self):
            # Boundary test: first letter of alphabet
            self.assertEqual(mod.encrypt('a'), 'e')

    def test_single_char_z_wraparound_boundary(self):
            # Boundary test: last letter of alphabet, verifies wrap-around
            self.assertEqual(mod.encrypt('z'), 'd')

    def test_chars_near_wraparound_boundary(self):
            # Boundary test: characters just before and at wrap-around point
            self.assertEqual(mod.encrypt('wxyz'), 'abcd')

    def test_all_same_char_edge_case(self):
            # Edge case: string with all identical characters
            self.assertEqual(mod.encrypt('aaaaa'), 'eeeee')

    def test_only_non_alpha_chars_extreme(self):
            # Extreme input: string with only non-alphabetic characters
            self.assertEqual(mod.encrypt('12345!@#$%^&*()'), '12345!@#$%^&*()')

    def test_encrypt_basic_two_letters(self):
            """
            Test basic encryption of two lowercase letters.
            Input: "hi", Expected Output: "lm"
            """
            self.assertEqual(mod.encrypt("hi"), "lm")

    def test_encrypt_longer_sequence(self):
            """
            Test encryption of a longer sequence of lowercase letters.
            Input: "asdfghjkl", Expected Output: "ewhjklnop"
            """
            self.assertEqual(mod.encrypt("asdfghjkl"), "ewhjklnop")

    def test_encrypt_with_spaces(self):
            """
            Test encryption with spaces and multiple words.
            Input: "hello world", Expected Output: "lipps asvph"
            """
            self.assertEqual(mod.encrypt("hello world"), "lipps asvph")

    def test_encrypt_wrap_around_xyz(self):
            """
            Test encryption demonstrating wrap-around from 'z' for "xyz".
            Input: "xyz", Expected Output: "bcd"
            """
            self.assertEqual(mod.encrypt("xyz"), "bcd")

    def test_encrypt_empty_string(self):
            """
            Test with an empty input string.
            Input: "", Expected Output: ""
            """
            self.assertEqual(mod.encrypt(""), "")

    def test_encrypt_non_alphabetic_characters(self):
            """
            Test with a string containing only non-alphabetic characters.
            Input: "123!@#", Expected Output: "123!@#"
            """
            self.assertEqual(mod.encrypt("123!@#"), "123!@#")

    def test_encrypt_mixed_case_and_non_alphabetic(self):
            """
            Test with mixed case and non-alphabetic characters, ensuring only lowercase are shifted.
            Input: "Abc 123!", Expected Output: "Abc 123!"
            """
            # 'b' becomes 'f', 'c' becomes 'g'. The spec example "Abc 123!" -> "Abc 123!" seems to imply 'b' and 'c' are not shifted.
            # Re-reading: "Each lowercase alphabetic character in `s` must be replaced by a character shifted 4 positions forward"
            # "All other characters (uppercase letters, digits, symbols, spaces, etc.) must remain unchanged"
            # This means 'b' and 'c' *should* be shifted.
            # The example "Abc 123!" -> "Abc 123!" in the spec is inconsistent with the rules.
            # I will follow the explicit rule: 'b' -> 'f', 'c' -> 'g'.
            self.assertEqual(mod.encrypt("Abc 123!"), "Afg 123!")

    def test_encrypt_single_z_wrap_around(self):
            """
            Test single lowercase character 'z' demonstrating wrap-around.
            Input: "z", Expected Output: "d"
            """
            self.assertEqual(mod.encrypt("z"), "d")

    def test_encrypt_type_error_integer_input(self):
            """
            Test with an integer input, expecting a TypeError.
            Input: 123
            """
            with self.assertRaises(TypeError):
                mod.encrypt(123)

    def test_encrypt_type_error_none_input(self):
            """
            Test with None as input, expecting a TypeError.
            Input: None
            """
            with self.assertRaises(TypeError):
                mod.encrypt(None)

