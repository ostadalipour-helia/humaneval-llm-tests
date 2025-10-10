import unittest
from sut_llm.problem_HumanEval_38 import decode_cyclic

class TestDecodeCyclic(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(decode_cyclic(""), "")

    def test_single_character_string(self):
        self.assertEqual(decode_cyclic("a"), "a")

    def test_two_character_string(self):
        self.assertEqual(decode_cyclic("ab"), "ab")

    def test_three_character_string_perfect_group(self):
        # 'abc' encoded is 'bca'
        self.assertEqual(decode_cyclic("bca"), "abc")

    def test_four_character_string_one_perfect_one_partial(self):
        # 'abcd' encoded is 'bcad' (abc -> bca, d -> d)
        self.assertEqual(decode_cyclic("bcad"), "abcd")

    def test_five_character_string_one_perfect_one_partial(self):
        # 'abcde' encoded is 'bcade' (abc -> bca, de -> de)
        self.assertEqual(decode_cyclic("bcade"), "abcde")

    def test_six_character_string_two_perfect_groups(self):
        # 'abcdef' encoded is 'bcaefd' (abc -> bca, def -> efd)
        self.assertEqual(decode_cyclic("bcaefd"), "abcdef")

    def test_string_with_mixed_characters(self):
        # '123!@#' encoded is '231@#!' (123 -> 231, !@# -> @#!)
        self.assertEqual(decode_cyclic("231@#!"), "123!@#")


    def test_string_with_spaces(self):
        # 'hello world' encoded is 'elho lorwld'
        # (hel->elh, lo ->o l, wor->orw, ld->ld)
        self.assertEqual(decode_cyclic("elho lorwld"), "hello world")

    def test_encode_cyclic_mixed_length_groups(self):
        """
        Tests encode_cyclic with an input string that results in both
        full (length 3) and partial (less than 3) groups.
        This ensures coverage for:
        - Line 6: The list comprehension for group splitting.
        - Line 8: Both branches of the conditional `if len(group) == 3 else group`.
        - Line 9: The final string join and return.
        """
        # Input "abcdefg" will be split into ["abc", "def", "g"]
        # "abc" (len 3) will be cycled to "bca"
        # "def" (len 3) will be cycled to "efd"
        # "g" (len 1) will remain "g"
        s = "abcdefg"
        expected = "bcaefdg"
        result = encode_cyclic(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()