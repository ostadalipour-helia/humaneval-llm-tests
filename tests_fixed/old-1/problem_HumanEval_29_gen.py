import unittest
from sut_llm.problem_HumanEval_29 import filter_by_prefix


class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_basic_filtering(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'cherry'], 'd'), [])

    def test_all_matches(self):
        self.assertEqual(filter_by_prefix(['apple', 'apricot', 'apply'], 'ap'), ['apple', 'apricot', 'apply'])

    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['hello', 'world'], ''), ['hello', 'world'])

    def test_prefix_longer_than_strings(self):
        self.assertEqual(filter_by_prefix(['a', 'ab', 'abc'], 'abcde'), [])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(['Apple', 'apple', 'apricot'], 'a'), ['apple', 'apricot'])

    def test_prefix_is_full_string(self):
        self.assertEqual(filter_by_prefix(['hello', 'hell', 'heaven'], 'hell'), ['hello', 'hell'])

    def test_strings_with_special_characters(self):
        self.assertEqual(filter_by_prefix(['$abc', '#def', '$ghi'], '$'), ['$abc', '$ghi'])

    def test_list_with_duplicate_strings(self):
        self.assertEqual(filter_by_prefix(['test', 'test', 'another', 'testing'], 'test'), ['test', 'test', 'testing'])


if __name__ == '__main__':
    unittest.main()