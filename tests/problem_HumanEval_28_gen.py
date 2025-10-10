import unittest
from sut.problem_HumanEval_28 import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case for an empty list of strings.
        Boundary condition: list length 0.
        """
        self.assertEqual(concatenate([]), '')

    def test_single_element_list(self):
        """
        Test case for a list with a single string.
        Boundary condition: list length 1.
        """
        self.assertEqual(concatenate(['hello']), 'hello')

    def test_two_elements_list(self):
        """
        Test case for a list with exactly two strings.
        Boundary condition: list length 2, often an off-by-one error point.
        """
        self.assertEqual(concatenate(['a', 'b']), 'ab')

    def test_multiple_elements_typical(self):
        """
        Test case for a typical list with several distinct strings.
        """
        self.assertEqual(concatenate(['apple', 'banana', 'cherry']), 'applebananacherry')

    def test_list_with_empty_strings(self):
        """
        Test case for a list containing empty strings.
        Logic mutation: ensures empty strings are handled correctly (effectively ignored).
        """
        self.assertEqual(concatenate(['first', '', 'middle', '', 'last']), 'firstmiddlelast')

    def test_list_with_all_same_elements(self):
        """
        Test case for a list where all elements are identical.
        Edge case: checks for unintended deduplication or special handling.
        """
        self.assertEqual(concatenate(['test', 'test', 'test']), 'testtesttest')

    def test_list_with_numbers_as_strings(self):
        """
        Test case for a list of numeric strings.
        Logic mutation: ensures no implicit type conversion or character set assumptions.
        """
        self.assertEqual(concatenate(['1', '23', '456']), '123456')

    def test_list_with_special_chars_and_whitespace(self):
        """
        Test case for a list containing strings with special characters and whitespace.
        Logic mutation: ensures all characters are preserved.
        """
        self.assertEqual(concatenate([' ', '\t', '\n', '!@#$']), ' \t\n!@#$')

    def test_long_list_of_short_strings(self):
        """
        Test case for a very long list of short strings.
        Extreme input: checks performance and loop termination for large N.
        """
        long_list = ['x'] * 1000
        expected_output = 'x' * 1000
        self.assertEqual(concatenate(long_list), expected_output)

    def test_list_with_very_long_strings(self):
        """
        Test case for a list containing very long individual strings.
        Extreme input: checks handling of large string data.
        """
        long_str1 = 'a' * 500
        long_str2 = 'b' * 500
        self.assertEqual(concatenate([long_str1, long_str2]), long_str1 + long_str2)

if __name__ == '__main__':
    unittest.main()