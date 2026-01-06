import unittest
import sut.problem_HumanEval_7 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_input_list(self):
            # CRITICAL: Edge Case (empty collection), Return Value (empty list)
            # Docstring example 1
            self.assertListEqual(mod.filter_by_substring([], 'a'), [])

    def test_typical_multiple_matches(self):
            # CRITICAL: Typical Input, Return Value (multiple elements)
            # Docstring example 2
            self.assertListEqual(mod.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_no_matches_found(self):
            # CRITICAL: Logic Mutation (all conditions false), Return Value (empty list)
            self.assertListEqual(mod.filter_by_substring(['apple', 'banana', 'cherry'], 'x'), [])

    def test_all_strings_contain_substring(self):
            # CRITICAL: Logic Mutation (all conditions true), Return Value (all elements returned)
            self.assertListEqual(mod.filter_by_substring(['apple', 'pineapple', 'grape'], 'p'), ['apple', 'pineapple', 'grape'])

    def test_single_element_list_match(self):
            # CRITICAL: Edge Case (single element collection), Boundary (substring at end)
            self.assertListEqual(mod.filter_by_substring(['hello world'], 'world'), ['hello world'])

    def test_single_element_list_no_match(self):
            # CRITICAL: Edge Case (single element collection), Return Value (empty list)
            self.assertListEqual(mod.filter_by_substring(['hello world'], 'python'), [])

    def test_empty_substring(self):
            # CRITICAL: Edge Case (empty substring), Logic Mutation (all conditions true)
            # An empty string is considered a substring of every string.
            self.assertListEqual(mod.filter_by_substring(['abc', 'def', 'ghi'], ''), ['abc', 'def', 'ghi'])

    def test_substring_is_entire_string(self):
            # CRITICAL: Boundary (substring is entire string), Off-by-One (exact match)
            self.assertListEqual(mod.filter_by_substring(['exact', 'match', 'example'], 'match'), ['match'])

    def test_case_sensitivity(self):
            # CRITICAL: Logic Mutation (only one condition true), Boundary (case sensitivity)
            self.assertListEqual(mod.filter_by_substring(['Apple', 'apple', 'Banana'], 'apple'), ['apple'])

    def test_substring_at_various_positions(self):
            # CRITICAL: Boundary (substring at start, middle, end), Off-by-One (various positions)
            self.assertListEqual(mod.filter_by_substring(['_start', 'in_the_middle', 'end_'], '_'), ['_start', 'in_the_middle', 'end_'])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_common_substring(self):
            # Description: Filter a list of strings for a common substring.
            strings_input = ["abc", "bacd", "cde", "array"]
            substring_input = "a"
            expected_output = ["abc", "bacd", "array"]
            
            # Test postcondition: The original 'strings' list must not be modified.
            original_strings_copy = list(strings_input) 
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_normal_no_match(self):
            # Description: No strings contain the given substring.
            strings_input = ["apple", "banana", "cherry"]
            substring_input = "z"
            expected_output = []
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_empty_strings_list(self):
            # Description: Input list of strings is empty.
            strings_input = []
            substring_input = "a"
            expected_output = []
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_empty_substring(self):
            # Description: Substring is an empty string (all strings contain an empty string).
            strings_input = ["abc", "def", "ghi"]
            substring_input = ""
            expected_output = ["abc", "def", "ghi"]
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_case_sensitive(self):
            # Description: Case-sensitive filtering.
            strings_input = ["apple", "Apple", "APple"]
            substring_input = "apple"
            expected_output = ["apple"]
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_substring_is_full_string(self):
            # Description: Substring is an entire string in the list.
            strings_input = ["fullmatch", "partial", "nomatch"]
            substring_input = "fullmatch"
            expected_output = ["fullmatch"]
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_edge_substring_multiple_times_in_string(self):
            # Description: Substring appears multiple times within a single string.
            strings_input = ["aaaaa", "bbbbb", "ccccc"]
            substring_input = "a"
            expected_output = ["aaaaa"]
    
            original_strings_copy = list(strings_input)
    
            result = mod.filter_by_substring(strings_input, substring_input)
            self.assertEqual(result, expected_output)
            self.assertEqual(strings_input, original_strings_copy, "Original strings list was modified.")

    def test_error_strings_elements_not_str(self):
            # Description: Elements in 'strings' list are not all strings.
            strings_input = [123, "abc"]
            substring_input = "a"
            with self.assertRaises(TypeError):
                mod.filter_by_substring(strings_input, substring_input)

    def test_error_substring_not_str(self):
            # Description: The 'substring' argument is not a string.
            strings_input = ["abc", "def"]
            substring_input = 123
            with self.assertRaises(TypeError):
                mod.filter_by_substring(strings_input, substring_input)

