import unittest
from sut.problem_HumanEval_38 import decode_cyclic

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

    def test_longer_string_multiple_groups_and_partial_end(self):
        # 'pythondeveloper' encoded is 'ytponhevdopperp'
        # (pyt->ytp, hon->onh, dev->evd, elo->olp, per->erp)
        self.assertEqual(decode_cyclic("ytponhevdopperp"), "pythondeveloper")

    def test_string_with_spaces(self):
        # 'hello world' encoded is 'elhorwld'
        # (hel->elh, lo ->o l, wor->orw, ld->ld)
        self.assertEqual(decode_cyclic("elhorwld"), "hello world")

if __name__ == '__main__':
    unittest.main()