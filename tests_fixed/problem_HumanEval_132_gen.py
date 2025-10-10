import unittest
from sut_llm.problem_HumanEval_132 import is_nested

class TestIsNested(unittest.TestCase):

    def test_1_empty_string(self):
        self.assertFalse(is_nested(""))

    def test_2_simple_non_nested_pair(self):
        self.assertFalse(is_nested("[]"))

    def test_3_multiple_non_nested_pairs(self):
        self.assertFalse(is_nested("[][]"))

    def test_4_simple_nested_pair(self):
        self.assertTrue(is_nested("[[]]"))

    def test_5_nested_with_inner_sequence(self):
        self.assertTrue(is_nested("[[][]]"))

    def test_6_long_string_no_nested(self):
        self.assertFalse(is_nested("[]]]]]]][[[[[]"))

    def test_7_only_opening_brackets(self):
        self.assertFalse(is_nested("[[[[["))

    def test_8_only_closing_brackets(self):
        self.assertFalse(is_nested("]]]]]"))

    def test_9_nested_at_start_with_extra_closing(self):
        self.assertTrue(is_nested("[[]]]]]]]"))

    def test_10_nested_in_middle_surrounded_by_non_nested(self):
        self.assertTrue(is_nested("[][[]][]"))