import unittest
from sut_llm.problem_HumanEval_1 import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_docstring_example(self):
        # Test 1: Basic example from docstring, covers typical input with nesting and spaces.
        self.assertListEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_empty_string(self):
        # Test 2: Edge case - empty input string.
        # Covers: Boundary (minimum length), return value (empty list).
        self.assertListEqual(separate_paren_groups(''), [])

    def test_single_simple_group(self):
        # Test 3: Edge case - single, non-nested group.
        # Covers: Boundary (single element collection), off-by-one (smallest valid group).
        self.assertListEqual(separate_paren_groups('()'), ['()'])

    def test_multiple_adjacent_simple_groups(self):
        # Test 4: Multiple identical simple groups with no spaces.
        # Covers: Logic mutation (separation of adjacent groups), duplicate values.
        self.assertListEqual(separate_paren_groups('()()()'), ['()', '()', '()'])

    def test_single_deeply_nested_group(self):
        # Test 5: Edge case - single, deeply nested group.
        # Covers: Boundary (complex nesting), off-by-one (many levels of nesting).
        self.assertListEqual(separate_paren_groups('((()))'), ['((()))'])

    def test_groups_with_internal_spaces(self):
        # Test 6: Groups containing only spaces inside.
        # Covers: Logic mutation (ignoring spaces inside groups), typical input.
        self.assertListEqual(separate_paren_groups('(  ) ( ( ) )'), ['()', '(())'])

    def test_groups_separated_by_many_spaces(self):
        # Test 7: Groups separated by multiple spaces.
        # Covers: Boundary (many spaces between groups), extreme/unusual input.
        self.assertListEqual(separate_paren_groups('()   (())'), ['()', '(())'])

    def test_mixed_simple_and_nested_groups_no_spaces(self):
        # Test 8: Mixed simple and nested groups without any spaces.
        # Covers: Typical input, logic mutation (handling different group types adjacently).
        self.assertListEqual(separate_paren_groups('()(())()'), ['()', '(())', '()'])

    def test_string_with_only_spaces(self):
        # Test 9: Edge case - input string contains only spaces.
        # Covers: Boundary (zero groups after ignoring spaces), extreme/unusual input.
        self.assertListEqual(separate_paren_groups('      '), [])

    def test_complex_mix_with_leading_trailing_and_internal_spaces(self):
        # Test 10: Complex input with leading/trailing spaces, various group types, and internal spaces.
        # Covers: Extreme/unusual input, comprehensive space handling, multiple return paths.
        self.assertListEqual(separate_paren_groups(' ( ( ) ) ( ) ( ( ( ) ) ) '), ['(())', '()', '((()))'])