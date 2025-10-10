import unittest
from sut_llm.problem_HumanEval_50 import decode_shift

class TestDecodeShift(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(decode_shift(""), "")

    def test_basic_lowercase_string(self):
        # "abc" encoded is "fgh"
        self.assertEqual(decode_shift("fgh"), "abc")

    def test_string_with_wrap_around_at_end(self):
        # "xyz" encoded is "cde"
        self.assertEqual(decode_shift("cde"), "xyz")

    def test_single_character_no_wrap(self):
        # "g" encoded is "l"
        self.assertEqual(decode_shift("l"), "g")

    def test_single_character_wrap_around_to_a(self):
        # "v" encoded is "a"
        self.assertEqual(decode_shift("a"), "v")

    def test_single_character_wrap_around_to_z(self):
        # "u" encoded is "z"
        self.assertEqual(decode_shift("z"), "u")

    def test_mixed_characters_with_wrap(self):
        # "hello" encoded is "mjqqt"
        self.assertEqual(decode_shift("mjqqt"), "hello")

    def test_longer_string(self):
        # "python" encoded is "udymts"
        self.assertEqual(decode_shift("udymts"), "python")

    def test_string_with_repeated_characters(self):
        # "aaaaa" encoded is "fffff"
        self.assertEqual(decode_shift("fffff"), "aaaaa")

    def test_string_starting_near_end_of_alphabet(self):
        # "zebra" encoded is "ejgwf"
        self.assertEqual(decode_shift("ejgwf"), "zebra")

    def test_encode_shift_basic(self):
        # This test covers line 5 by executing the encode_shift function with a basic string.
        input_str = "hello"
        expected_output = "mjqqt"
        result = encode_shift(input_str)
        self.assertEqual(result, expected_output)

    def test_encode_shift_wrap_around(self):
        # This test also covers line 5, specifically with characters that wrap around 'z'.
        input_str = "xyz"
        expected_output = "cde"
        result = encode_shift(input_str)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()