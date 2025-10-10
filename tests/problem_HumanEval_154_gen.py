import unittest
from sut.problem_HumanEval_154 import cycpattern_check

class TestCycpatternCheck(unittest.TestCase):

    def test_docstring_example_hello_ell(self):
        # Typical case: 'ell' is a substring of 'hello'.
        self.assertEqual(cycpattern_check("hello", "ell"), True)

    def test_docstring_example_abcd_abd(self):
        # Typical case: 'abd' is not a substring, nor any rotation.
        self.assertEqual(cycpattern_check("abcd", "abd"), False)

    def test_edge_case_empty_strings(self):
        # Edge case: Both strings are empty. An empty string is a substring of itself.
        self.assertEqual(cycpattern_check("", ""), True)

    def test_edge_case_empty_pattern(self):
        # Edge case: Pattern is empty. An empty string is always a substring of any string.
        self.assertEqual(cycpattern_check("abc", ""), True)

    def test_boundary_pattern_longer_than_main(self):
        # Boundary case: Pattern is longer than the main string. Should always be False.
        self.assertEqual(cycpattern_check("abc", "abcd"), False)

    def test_boundary_pattern_same_length_and_rotation(self):
        # Boundary case: Pattern has same length as main string and is a rotation.
        self.assertEqual(cycpattern_check("abc", "bca"), True)

    def test_boundary_pattern_same_length_but_not_rotation(self):
        # Boundary case: Pattern has same length as main string but is not a rotation.
        self.assertEqual(cycpattern_check("abc", "abd"), False)

    def test_logic_mutation_multiple_rotations_one_match(self):
        # Logic mutation: 'nana' rotations are 'nana', 'anan'. 'anan' is in 'banana'.
        # Ensures all rotations are checked and not just the original pattern.
        self.assertEqual(cycpattern_check("banana", "nana"), True)

    def test_extreme_long_strings_no_match(self):
        # Extreme case: Long strings, no match found after checking all rotations.
        self.assertEqual(cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyxw"), False)

    def test_extreme_long_strings_match_at_end_via_rotation(self):
        # Extreme case: Long strings, match found via rotation that wraps around.
        # Rotations of "yzabc": "yzabc", "zabcy", "abcza", "bczy", "czyab". "abcza" is in the main string.
        self.assertEqual(cycpattern_check("abcdefghijklmnopqrstuvwxyz", "abcza"), True)