import unittest
from sut_llm.problem_HumanEval_7 import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_input_list(self):
        # CRITICAL: Edge Case (empty collection), Return Value (empty list)
        # Docstring example 1
        self.assertListEqual(filter_by_substring([], 'a'), [])

    def test_typical_multiple_matches(self):
        # CRITICAL: Typical Input, Return Value (multiple elements)
        # Docstring example 2
        self.assertListEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_no_matches_found(self):
        # CRITICAL: Logic Mutation (all conditions false), Return Value (empty list)
        self.assertListEqual(filter_by_substring(['apple', 'banana', 'cherry'], 'x'), [])

    def test_all_strings_contain_substring(self):
        # CRITICAL: Logic Mutation (all conditions true), Return Value (all elements returned)
        self.assertListEqual(filter_by_substring(['apple', 'pineapple', 'grape'], 'p'), ['apple', 'pineapple', 'grape'])

    def test_single_element_list_match(self):
        # CRITICAL: Edge Case (single element collection), Boundary (substring at end)
        self.assertListEqual(filter_by_substring(['hello world'], 'world'), ['hello world'])

    def test_single_element_list_no_match(self):
        # CRITICAL: Edge Case (single element collection), Return Value (empty list)
        self.assertListEqual(filter_by_substring(['hello world'], 'python'), [])

    def test_empty_substring(self):
        # CRITICAL: Edge Case (empty substring), Logic Mutation (all conditions true)
        # An empty string is considered a substring of every string.
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ghi'], ''), ['abc', 'def', 'ghi'])

    def test_substring_is_entire_string(self):
        # CRITICAL: Boundary (substring is entire string), Off-by-One (exact match)
        self.assertListEqual(filter_by_substring(['exact', 'match', 'example'], 'match'), ['match'])

    def test_case_sensitivity(self):
        # CRITICAL: Logic Mutation (only one condition true), Boundary (case sensitivity)
        self.assertListEqual(filter_by_substring(['Apple', 'apple', 'Banana'], 'apple'), ['apple'])

    def test_substring_at_various_positions(self):
        # CRITICAL: Boundary (substring at start, middle, end), Off-by-One (various positions)
        self.assertListEqual(filter_by_substring(['_start', 'in_the_middle', 'end_'], '_'), ['_start', 'in_the_middle', 'end_'])

if __name__ == '__main__':
    unittest.main()