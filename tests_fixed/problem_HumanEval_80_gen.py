import unittest
from sut_llm.problem_HumanEval_80 import is_happy

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        # Edge case: empty string, length < 3
        self.assertEqual(is_happy(""), False)

    def test_single_char_string(self):
        # Edge case: single character string, length < 3
        self.assertEqual(is_happy("a"), False)

    def test_two_char_string(self):
        # Boundary condition: string of length 2, length < 3
        self.assertEqual(is_happy("ab"), False)

    def test_boundary_length_three_happy(self):
        # Boundary condition: string of length 3, all distinct (happy)
        self.assertEqual(is_happy("abc"), True)

    def test_boundary_length_three_unhappy(self):
        # Boundary condition: string of length 3, not distinct (unhappy)
        # Catches mutations like changing '<' to '<=' for length check, or incorrect distinctness logic.
        self.assertEqual(is_happy("aba"), False)

    def test_typical_happy_string_from_doc(self):
        # Typical input: happy string from docstring
        self.assertEqual(is_happy("abcd"), True)

    def test_typical_unhappy_string_from_doc(self):
        # Typical input: unhappy string from docstring, fails in the middle
        # Catches mutations in loop conditions or distinctness check.
        self.assertEqual(is_happy("aabb"), False)

    def test_unhappy_at_start_of_long_string(self):
        # Extreme input: long string, unhappy due to first triplet
        # Catches off-by-one errors in loop start or distinctness check.
        self.assertEqual(is_happy("aaabcde"), False)

    def test_unhappy_at_end_of_long_string(self):
        # Extreme input: long string, unhappy due to last triplet
        # Catches off-by-one errors in loop end or distinctness check.
        self.assertEqual(is_happy("abcdeff"), False)

    def test_long_happy_string_complex(self):
        # Extreme input: long string with many distinct triplets (happy)
        # Verifies robustness for longer inputs.
        self.assertEqual(is_happy("abcdefghijk"), True)

if __name__ == '__main__':
    unittest.main()