import unittest
from sut.problem_HumanEval_154 import cycpattern_check

class TestCycpatternCheck(unittest.TestCase):

    def test_1_docstring_example_1(self):
        self.assertFalse(cycpattern_check("abcd", "abd"))

    def test_2_docstring_example_2(self):
        self.assertTrue(cycpattern_check("hello", "ell"))

    def test_3_docstring_example_3(self):
        self.assertFalse(cycpattern_check("whassup", "psus"))

    def test_4_docstring_example_4(self):
        self.assertTrue(cycpattern_check("abab", "baa"))

    def test_5_docstring_example_5(self):
        self.assertFalse(cycpattern_check("efef", "eeff"))

    def test_6_docstring_example_6(self):
        self.assertTrue(cycpattern_check("himenss", "simen"))

    def test_7_direct_substring(self):
        # b is a direct substring of a, no rotation needed
        self.assertTrue(cycpattern_check("programming", "gram"))

    def test_8_rotation_is_substring(self):
        # A rotation of b is a substring of a
        self.assertTrue(cycpattern_check("applepie", "pleap")) # "pleap" is a rotation of "apple"

    def test_9_b_longer_than_a(self):
        # b is longer than a, so it cannot be a substring
        self.assertFalse(cycpattern_check("short", "longerword"))

    def test_10_empty_b(self):
        # An empty string is always considered a substring of any string
        self.assertTrue(cycpattern_check("anytext", ""))