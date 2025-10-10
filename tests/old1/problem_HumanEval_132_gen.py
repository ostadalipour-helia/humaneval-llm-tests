import unittest
from sut.problem_HumanEval_132 import is_nested

class TestIsNested(unittest.TestCase):

    def test_example_simple_nested(self):
        self.assertTrue(is_nested('[[]]'))

    def test_example_unbalanced_no_nested(self):
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))

    def test_example_valid_not_nested_multiple(self):
        self.assertFalse(is_nested('[][]'))

    def test_example_valid_not_nested_single(self):
        self.assertFalse(is_nested('[]'))

    def test_example_mixed_nested_and_not(self):
        self.assertTrue(is_nested('[[][]]'))

    def test_example_nested_followed_by_unclosed(self):
        self.assertTrue(is_nested('[[]][['))

    def test_empty_string(self):
        self.assertFalse(is_nested(''))

    def test_single_opening_bracket(self):
        self.assertFalse(is_nested('['))

    def test_deeply_nested(self):
        self.assertTrue(is_nested('[[[[]]]]'))

    def test_non_nested_then_nested(self):
        self.assertTrue(is_nested('[]][[]]'))

if __name__ == '__main__':
    unittest.main()