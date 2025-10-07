import unittest
from sut_llm.problem_HumanEval_1 import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_docstring_example(self):
        # Test case from the function's docstring
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_single_simple_group(self):
        # Test with a single, simplest balanced group
        self.assertEqual(separate_paren_groups('()'), ['()'])

    def test_single_nested_group(self):
        # Test with a single, deeply nested balanced group
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])

    def test_multiple_simple_groups(self):
        # Test with multiple simple, non-nested groups
        self.assertEqual(separate_paren_groups('()()()'), ['()', '()', '()'])

    def test_multiple_nested_groups(self):
        # Test with multiple distinct nested groups
        self.assertEqual(separate_paren_groups('(())(())'), ['(())', '(())'])

    def test_empty_string_input(self):
        # Test with an empty input string
        self.assertEqual(separate_paren_groups(''), [])

    def test_string_with_only_spaces(self):
        # Test with an input string containing only spaces
        self.assertEqual(separate_paren_groups('   '), [])

    def test_groups_with_varying_nesting_and_internal_spaces(self):
        # Test with groups of different nesting levels and internal spaces
        self.assertEqual(separate_paren_groups('( ( ) ) ( ( ( ) ) )'), ['(())', '((()))'])

    def test_leading_trailing_and_internal_spaces(self):
        # Test with leading, trailing, and internal spaces around and within groups
        self.assertEqual(separate_paren_groups('  ( )  ( ( ) )  '), ['()', '(())'])

    def test_complex_mix_of_deeply_nested_groups(self):
        # Test with a complex mix including very deeply nested groups
        self.assertEqual(separate_paren_groups('((((()))))((()))'), ['((((()))))', '((()))'])

if __name__ == '__main__':
    unittest.main()