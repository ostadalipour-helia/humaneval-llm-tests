import unittest
from sut_llm.problem_HumanEval_54 import same_chars

class TestSameChars(unittest.TestCase):

    def test_01_example_true_complex(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_02_example_true_simple(self):
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test_03_example_true_reversed(self):
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_04_example_false_s0_extra(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_05_example_false_s1_extra(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_06_example_false_different_sets(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

    def test_07_empty_strings(self):
        self.assertTrue(same_chars('', ''))

    def test_08_one_empty_one_non_empty(self):
        self.assertFalse(same_chars('a', ''))

    def test_09_single_character_repeated(self):
        self.assertTrue(same_chars('a', 'aaa'))

    def test_10_different_order_same_chars(self):
        self.assertTrue(same_chars('abc', 'cba'))

if __name__ == '__main__':
    unittest.main()