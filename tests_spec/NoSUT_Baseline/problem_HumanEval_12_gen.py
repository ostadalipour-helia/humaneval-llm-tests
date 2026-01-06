import unittest
import sut.problem_HumanEval_12 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            """
            Test case for an empty input list.
            Should return None as per docstring.
            (Edge Case, Return Value Testing)
            """
            self.assertIsNone(mod.longest([]))

    def test_single_element_list(self):
            """
            Test case for a list with a single string.
            Should return that string.
            (Edge Case, Off-by-One Error, Return Value Testing)
            """
            self.assertEqual(mod.longest(['a']), 'a')

    def test_unique_lengths_increasing(self):
            """
            Test case with strings of unique, increasing lengths.
            Should return the longest one.
            (Typical Input, Return Value Testing)
            """
            self.assertEqual(mod.longest(['a', 'bb', 'ccc']), 'ccc')

    def test_unique_lengths_decreasing(self):
            """
            Test case with strings of unique, decreasing lengths.
            Should return the longest one.
            (Typical Input, Return Value Testing)
            """
            self.assertEqual(mod.longest(['ddd', 'cc', 'b']), 'ddd')

    def test_multiple_same_max_length_last_occurrence(self):
            """
            Test case where the first longest string is the last of its length group.
            Ensures the "first one" rule is correctly applied.
            (Boundary Testing, Logic Mutation, Off-by-One Error)
            """
            self.assertEqual(mod.longest(['x', 'yy', 'zzz', 'aaa']), 'zzz') # 'zzz' and 'aaa' are both length 3, 'zzz' comes first

    def test_list_with_empty_string(self):
            """
            Test case including an empty string.
            Ensures length 0 is handled correctly and not chosen if longer strings exist.
            (Extreme/Unusual Input, Sign and Zero Testing)
            """
            self.assertEqual(mod.longest(['', 'a', 'bb']), 'bb')

    def test_all_empty_strings(self):
            """
            Test case where all strings are empty.
            Should return an empty string.
            (Extreme/Unusual Input, Edge Case, Sign and Zero Testing)
            """
            self.assertEqual(mod.longest(['', '', '']), '')

    def test_long_strings_and_duplicates(self):
            """
            Test case with longer strings and duplicate values.
            Verifies correct handling of length comparisons and the "first one" rule.
            (Extreme/Unusual Input, Edge Case - duplicates)
            """
            self.assertEqual(mod.longest(['short', 'medium', 'verylongstring', 'medium', 'longer']), 'verylongstring')

    def test_normal_varying_lengths(self):
            # Returns the longest string when lengths vary.
            self.assertEqual(mod.longest(['apple', 'banana', 'cherry']), 'banana')

    def test_normal_first_of_max_length(self):
            # Returns the first string when multiple strings have the same maximum length.
            self.assertEqual(mod.longest(['hello', 'world']), 'hello')

    def test_normal_longest_from_mixed_lengths(self):
            # Returns the longest string from a list with varying lengths.
            self.assertEqual(mod.longest(['short', 'medium', 'longest_string']), 'longest_string')

    def test_edge_empty_list(self):
            # Returns None for an empty input list.
            self.assertIsNone(mod.longest([]))

    def test_edge_all_same_length(self):
            # Returns the first string when all strings have the same length.
            self.assertEqual(mod.longest(['a', 'b', 'c']), 'a')

    def test_edge_single_empty_string(self):
            # Returns an empty string if it's the only element.
            self.assertEqual(mod.longest(['']), '')

    def test_edge_empty_string_among_others(self):
            # Handles empty strings correctly when other strings are present.
            self.assertEqual(mod.longest(['', 'a', 'bb']), 'bb')

    def test_edge_single_element_list(self):
            # Returns the single string in a list with one element.
            self.assertEqual(mod.longest(['a']), 'a')

    def test_error_input_not_list_int(self):
            # Input is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.longest(123)

    def test_error_list_contains_ints(self):
            # List contains non-string elements (integers).
            with self.assertRaises(TypeError):
                mod.longest([1, 2, 3])

    def test_error_list_contains_mixed_types(self):
            # List contains mixed types, including non-string elements.
            with self.assertRaises(TypeError):
                mod.longest(['a', 1, 'b'])

