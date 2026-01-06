import unittest
import sut.problem_HumanEval_80 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge case: empty string, length < 3
            self.assertEqual(mod.is_happy(""), False)

    def test_single_char_string(self):
            # Edge case: single character string, length < 3
            self.assertEqual(mod.is_happy("a"), False)

    def test_two_char_string(self):
            # Boundary condition: string of length 2, length < 3
            self.assertEqual(mod.is_happy("ab"), False)

    def test_boundary_length_three_happy(self):
            # Boundary condition: string of length 3, all distinct (happy)
            self.assertEqual(mod.is_happy("abc"), True)

    def test_boundary_length_three_unhappy(self):
            # Boundary condition: string of length 3, not distinct (unhappy)
            # Catches mutations like changing '<' to '<=' for length check, or incorrect distinctness logic.
            self.assertEqual(mod.is_happy("aba"), False)

    def test_typical_happy_string_from_doc(self):
            # Typical input: happy string from docstring
            self.assertEqual(mod.is_happy("abcd"), True)

    def test_typical_unhappy_string_from_doc(self):
            # Typical input: unhappy string from docstring, fails in the middle
            # Catches mutations in loop conditions or distinctness check.
            self.assertEqual(mod.is_happy("aabb"), False)

    def test_unhappy_at_start_of_long_string(self):
            # Extreme input: long string, unhappy due to first triplet
            # Catches off-by-one errors in loop start or distinctness check.
            self.assertEqual(mod.is_happy("aaabcde"), False)

    def test_unhappy_at_end_of_long_string(self):
            # Extreme input: long string, unhappy due to last triplet
            # Catches off-by-one errors in loop end or distinctness check.
            self.assertEqual(mod.is_happy("abcdeff"), False)

    def test_long_happy_string_complex(self):
            # Extreme input: long string with many distinct triplets (happy)
            # Verifies robustness for longer inputs.
            self.assertEqual(mod.is_happy("abcdefghijk"), True)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_distinct_abcd(self):
            # Length is 4 (>=3). 'abc' are distinct, 'bcd' are distinct.
            self.assertTrue(mod.is_happy("abcd"))

    def test_normal_distinct_abcde(self):
            # Length is 5 (>=3). 'abc', 'bcd', 'cde' are all distinct.
            self.assertTrue(mod.is_happy("abcde"))

    def test_normal_distinct_xyzabc(self):
            # Length is 6 (>=3). All 3-consecutive substrings ('xyz', 'yza', 'zab', 'abc') have distinct characters.
            self.assertTrue(mod.is_happy("xyzabc"))

    def test_edge_short_string_a(self):
            # Length is 1, which is less than 3.
            self.assertFalse(mod.is_happy("a"))

    def test_edge_empty_string(self):
            # Length is 0, which is less than 3.
            self.assertFalse(mod.is_happy(""))

    def test_edge_repeating_substring_aabb(self):
            # Length is 4 (>=3). The substring 'aab' does not have distinct characters ('a' repeats).
            self.assertFalse(mod.is_happy("aabb"))

    def test_edge_repeating_substring_xyy(self):
            # Length is 3 (>=3). The substring 'xyy' does not have distinct characters ('y' repeats).
            self.assertFalse(mod.is_happy("xyy"))

    def test_edge_repeating_substring_abacaba(self):
            # Length is 7 (>=3). The substring 'aba' (at index 0, 2, 4) does not have distinct characters.
            self.assertFalse(mod.is_happy("abacaba"))

    def test_error_int_input(self):
            # Input is not a string.
            with self.assertRaises(TypeError):
                mod.is_happy(123)

    def test_error_none_input(self):
            # Input is not a string.
            with self.assertRaises(TypeError):
                mod.is_happy(None)

