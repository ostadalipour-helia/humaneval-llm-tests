import unittest
from sut.problem_HumanEval_29 import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case: An empty list of strings.
        Expected: An empty list.
        Covers: Edge case (empty collection), Boundary (list length 0).
        """
        self.assertListEqual(filter_by_prefix([], 'a'), [])

    def test_empty_prefix(self):
        """
        Test case: An empty prefix string. All strings should match.
        Expected: The original list of strings.
        Covers: Edge case (empty string for prefix), Logic mutation (if prefix length check was flawed).
        """
        self.assertListEqual(filter_by_prefix(['abc', 'def', 'ghi'], ''), ['abc', 'def', 'ghi'])

    def test_single_element_match(self):
        """
        Test case: A list with a single string that matches the prefix.
        Expected: A list containing that single string.
        Covers: Edge case (single element collection), Boundary (list length 1).
        """
        self.assertListEqual(filter_by_prefix(['apple'], 'a'), ['apple'])

    def test_single_element_no_match(self):
        """
        Test case: A list with a single string that does not match the prefix.
        Expected: An empty list.
        Covers: Edge case (single element collection), Boundary (list length 1).
        """
        self.assertListEqual(filter_by_prefix(['banana'], 'a'), [])

    def test_typical_mixed_matches(self):
        """
        Test case: A typical list with some strings matching and some not. (From docstring)
        Expected: A filtered list with only matching strings.
        Covers: Typical input, Return value testing (partial match).
        """
        self.assertListEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_all_strings_match(self):
        """
        Test case: All strings in the list match the given prefix.
        Expected: The original list of strings.
        Covers: Typical input, Return value testing (all match).
        """
        self.assertListEqual(filter_by_prefix(['apple', 'apricot', 'apply'], 'ap'), ['apple', 'apricot', 'apply'])

    def test_no_strings_match(self):
        """
        Test case: None of the strings in the list match the given prefix.
        Expected: An empty list.
        Covers: Typical input, Return value testing (no match).
        """
        self.assertListEqual(filter_by_prefix(['banana', 'grape', 'orange'], 'a'), [])

    def test_prefix_longer_than_some_strings(self):
        """
        Test case: The prefix is longer than some or all strings in the list.
        Expected: An empty list, as shorter strings cannot start with a longer prefix.
        Covers: Boundary condition (prefix length > string length), Off-by-one (string.startswith logic).
        """
        self.assertListEqual(filter_by_prefix(['a', 'ab', 'abc'], 'abcd'), [])

    def test_single_char_prefix_and_strings(self):
        """
        Test case: Single character prefix and a mix of single and multi-character strings.
        Expected: Correctly filtered list.
        Covers: Boundary (minimal string/prefix length), Off-by-one (startswith logic for length 1).
        """
        self.assertListEqual(filter_by_prefix(['a', 'b', 'c', 'aa', 'ba'], 'a'), ['a', 'aa'])

    def test_long_strings_and_prefix(self):
        """
        Test case: Very long strings and a very long prefix.
        Expected: Correctly filtered list.
        Covers: Extreme/unusual input, Performance consideration.
        """
        long_prefix = 'x' * 1000
        long_string_match1 = long_prefix + 'abc'
        long_string_match2 = long_prefix + 'def'
        long_string_no_match = 'y' * 1000 + 'ghi'
        self.assertListEqual(
            filter_by_prefix([long_string_match1, long_string_no_match, long_string_match2], long_prefix),
            [long_string_match1, long_string_match2]
        )

if __name__ == '__main__':
    unittest.main()