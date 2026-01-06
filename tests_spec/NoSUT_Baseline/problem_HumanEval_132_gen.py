import unittest
import sut.problem_HumanEval_132 as mod

class TestHybrid(unittest.TestCase):
    def test_1_empty_string(self):
            self.assertFalse(mod.is_nested(""))

    def test_2_simple_non_nested_pair(self):
            self.assertFalse(mod.is_nested("[]"))

    def test_3_multiple_non_nested_pairs(self):
            self.assertFalse(mod.is_nested("[][]"))

    def test_4_simple_nested_pair(self):
            self.assertTrue(mod.is_nested("[[]]"))

    def test_5_nested_with_inner_sequence(self):
            self.assertTrue(mod.is_nested("[[][]]"))

    def test_6_long_string_no_nested(self):
            self.assertFalse(mod.is_nested("[]]]]]]][[[[[]"))

    def test_7_only_opening_brackets(self):
            self.assertFalse(mod.is_nested("[[[[["))

    def test_8_only_closing_brackets(self):
            self.assertFalse(mod.is_nested("]]]]]"))

    def test_9_nested_at_start_with_extra_closing(self):
            self.assertTrue(mod.is_nested("[[]]]]]]]"))

    def test_10_nested_in_middle_surrounded_by_non_nested(self):
            self.assertTrue(mod.is_nested("[][[]][]"))

    def test_normal_nested_simple(self):
            # Input: '[[]]'
            # Output: True
            # Reason: The outermost brackets at indices 0 and 3 enclose '[]', which is a non-empty, valid bracket sequence.
            self.assertTrue(mod.is_nested('[[]]'))

    def test_normal_nested_complex(self):
            # Input: '[[][]]'
            # Output: True
            # Reason: The outermost brackets at indices 0 and 5 enclose '[][]', which is a non-empty, valid bracket sequence.
            self.assertTrue(mod.is_nested('[[][]]'))

    def test_normal_nested_with_trailing_unbalanced(self):
            # Input: '[[]][['
            # Output: True
            # Reason: The brackets at indices 0 and 3 enclose '[]', which is a non-empty, valid bracket sequence.
            self.assertTrue(mod.is_nested('[[]][['))

    def test_normal_no_nested_valid_pairs(self):
            # Input: '[][]'
            # Output: False
            # Reason: Each pair of brackets encloses an empty string. No nested structure.
            self.assertFalse(mod.is_nested('[][]'))

    def test_normal_no_nested_complex_unbalanced(self):
            # Input: '[]]]]]]][[[[[]'
            # Output: False
            # Reason: No pair of brackets encloses a non-empty, valid bracket sequence. All valid pairs enclose an empty string.
            self.assertFalse(mod.is_nested('[]]]]]]][[[[[]'))

    def test_edge_empty_string(self):
            # Input: ''
            # Output: False
            # Reason: An empty string contains no brackets, thus no nested brackets.
            self.assertFalse(mod.is_nested(''))

    def test_edge_single_opening_bracket(self):
            # Input: '['
            # Output: False
            # Reason: A single opening bracket cannot form a pair, let alone a nested one.
            self.assertFalse(mod.is_nested('['))

    def test_edge_single_closing_bracket(self):
            # Input: ']'
            # Output: False
            # Reason: A single closing bracket cannot form a pair.
            self.assertFalse(mod.is_nested(']'))

    def test_edge_only_empty_enclosure(self):
            # Input: '[]'
            # Output: False
            # Reason: The only pair of brackets encloses an empty string, which is not a non-empty valid bracket sequence.
            self.assertFalse(mod.is_nested('[]'))

    def test_error_non_string_integer(self):
            # Input: 123
            # Exception: TypeError
            # Reason: Input is not a string.
            with self.assertRaises(TypeError):
                mod.is_nested(123)

    def test_error_non_string_none(self):
            # Input: None
            # Exception: TypeError
            # Reason: Input is not a string.
            with self.assertRaises(TypeError):
                mod.is_nested(None)

