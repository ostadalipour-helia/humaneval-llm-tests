import unittest
from sut_llm.problem_HumanEval_12 import longest

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case for an empty input list.
        Should return None as per docstring.
        (Edge Case, Return Value Testing)
        """
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        """
        Test case for a list with a single string.
        Should return that string.
        (Edge Case, Off-by-One Error, Return Value Testing)
        """
        self.assertEqual(longest(['a']), 'a')

    def test_unique_lengths_increasing(self):
        """
        Test case with strings of unique, increasing lengths.
        Should return the longest one.
        (Typical Input, Return Value Testing)
        """
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_unique_lengths_decreasing(self):
        """
        Test case with strings of unique, decreasing lengths.
        Should return the longest one.
        (Typical Input, Return Value Testing)
        """
        self.assertEqual(longest(['ddd', 'cc', 'b']), 'ddd')

    def test_multiple_same_max_length_first_occurrence(self):
        """
        Test case where multiple strings have the same maximum length.
        Should return the first one encountered.
        (Boundary Testing, Logic Mutation, Off-by-One Error)
        """
        # 'apple', 'grape', and 'melon' are all length 5. 'apple' comes first.
        self.assertEqual(longest(['apple', 'grape', 'melon']), 'apple')

    def test_multiple_same_max_length_middle_occurrence(self):
        """
        Test case where the first longest string is in the middle of the list.
        Ensures the "first one" rule is correctly applied.
        (Boundary Testing, Logic Mutation, Off-by-One Error)
        """
        self.assertEqual(longest(['a', 'bb', 'cc', 'd']), 'bb') # 'bb' and 'cc' are both length 2, 'bb' comes first

    def test_multiple_same_max_length_last_occurrence(self):
        """
        Test case where the first longest string is the last of its length group.
        Ensures the "first one" rule is correctly applied.
        (Boundary Testing, Logic Mutation, Off-by-One Error)
        """
        self.assertEqual(longest(['x', 'yy', 'zzz', 'aaa']), 'zzz') # 'zzz' and 'aaa' are both length 3, 'zzz' comes first

    def test_list_with_empty_string(self):
        """
        Test case including an empty string.
        Ensures length 0 is handled correctly and not chosen if longer strings exist.
        (Extreme/Unusual Input, Sign and Zero Testing)
        """
        self.assertEqual(longest(['', 'a', 'bb']), 'bb')

    def test_all_empty_strings(self):
        """
        Test case where all strings are empty.
        Should return an empty string.
        (Extreme/Unusual Input, Edge Case, Sign and Zero Testing)
        """
        self.assertEqual(longest(['', '', '']), '')

    def test_long_strings_and_duplicates(self):
        """
        Test case with longer strings and duplicate values.
        Verifies correct handling of length comparisons and the "first one" rule.
        (Extreme/Unusual Input, Edge Case - duplicates)
        """
        self.assertEqual(longest(['short', 'medium', 'verylongstring', 'medium', 'longer']), 'verylongstring')