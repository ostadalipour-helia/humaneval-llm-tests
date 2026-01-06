import unittest
from sut.problem_HumanEval_132 import is_nested

class Test_is_nested(unittest.TestCase):
    def test_normal_nested_simple(self):
        # Input: '[[]]'
        # Output: True
        # Reason: The outermost brackets at indices 0 and 3 enclose '[]', which is a non-empty, valid bracket sequence.
        self.assertTrue(is_nested('[[]]'))

    def test_normal_nested_complex(self):
        # Input: '[[][]]'
        # Output: True
        # Reason: The outermost brackets at indices 0 and 5 enclose '[][]', which is a non-empty, valid bracket sequence.
        self.assertTrue(is_nested('[[][]]'))

    def test_normal_nested_with_trailing_unbalanced(self):
        # Input: '[[]][['
        # Output: True
        # Reason: The brackets at indices 0 and 3 enclose '[]', which is a non-empty, valid bracket sequence.
        self.assertTrue(is_nested('[[]][['))

    def test_normal_no_nested_valid_pairs(self):
        # Input: '[][]'
        # Output: False
        # Reason: Each pair of brackets encloses an empty string. No nested structure.
        self.assertFalse(is_nested('[][]'))

    def test_normal_no_nested_complex_unbalanced(self):
        # Input: '[]]]]]]][[[[[]'
        # Output: False
        # Reason: No pair of brackets encloses a non-empty, valid bracket sequence. All valid pairs enclose an empty string.
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))

    def test_edge_empty_string(self):
        # Input: ''
        # Output: False
        # Reason: An empty string contains no brackets, thus no nested brackets.
        self.assertFalse(is_nested(''))

    def test_edge_single_opening_bracket(self):
        # Input: '['
        # Output: False
        # Reason: A single opening bracket cannot form a pair, let alone a nested one.
        self.assertFalse(is_nested('['))

    def test_edge_single_closing_bracket(self):
        # Input: ']'
        # Output: False
        # Reason: A single closing bracket cannot form a pair.
        self.assertFalse(is_nested(']'))

    def test_edge_only_empty_enclosure(self):
        # Input: '[]'
        # Output: False
        # Reason: The only pair of brackets encloses an empty string, which is not a non-empty valid bracket sequence.
        self.assertFalse(is_nested('[]'))

    def test_edge_multiple_empty_enclosures(self):
        # Input: '[][][][][][][][][][]'
        # Output: False
        # Reason: Multiple non-nested valid pairs, none of which enclose a non-empty valid sequence.
        self.assertFalse(is_nested('[][][][][][][][][][]'))

    def test_error_non_string_integer(self):
        # Input: 123
        # Exception: TypeError
        # Reason: Input is not a string.
        with self.assertRaises(TypeError):
            is_nested(123)

    def test_error_non_string_none(self):
        # Input: None
        # Exception: TypeError
        # Reason: Input is not a string.
        with self.assertRaises(TypeError):
            is_nested(None)

    def test_error_invalid_chars_alphabetic(self):
        # Input: '[a]'
        # Exception: ValueError
        # Reason: Input string contains characters other than '[' and ']'.
        with self.assertRaises(ValueError):
            is_nested('[a]')

    def test_error_invalid_chars_curly_braces(self):
        # Input: '{}'
        # Exception: ValueError
        # Reason: Input string contains characters other than '[' and ']'.
        with self.assertRaises(ValueError):
            is_nested('{}')