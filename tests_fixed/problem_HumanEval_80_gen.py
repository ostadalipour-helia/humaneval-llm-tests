import unittest
from sut_llm.problem_HumanEval_80 import is_happy

class TestIsHappy(unittest.TestCase):

    def test_length_one_string(self):
        # Test case from docstring: length < 3
        self.assertFalse(is_happy("a"))

    def test_length_two_string(self):
        # Test case from docstring: length < 3
        self.assertFalse(is_happy("aa"))

    def test_empty_string(self):
        # Edge case: length 0
        self.assertFalse(is_happy(""))

    def test_happy_string_abcd(self):
        # Test case from docstring: happy string
        self.assertTrue(is_happy("abcd"))

    def test_happy_string_adb(self):
        # Test case from docstring: happy string
        self.assertTrue(is_happy("adb"))

    def test_unhappy_string_aabb(self):
        # Test case from docstring: not happy due to s[i] == s[i+1]
        self.assertFalse(is_happy("aabb"))

    def test_unhappy_string_xyy(self):
        # Test case from docstring: not happy due to s[i+1] == s[i+2]
        self.assertFalse(is_happy("xyy"))

    def test_unhappy_string_aba(self):
        # Test case: not happy due to s[i] == s[i+2]
        self.assertFalse(is_happy("aba"))

    def test_longer_happy_string(self):
        # Test case: longer string that is happy
        self.assertTrue(is_happy("abcdefg"))

    def test_longer_unhappy_string_middle_failure(self):
        # Test case: longer string that fails in the middle due to s[i] == s[i+2]
        self.assertFalse(is_happy("abacdef"))