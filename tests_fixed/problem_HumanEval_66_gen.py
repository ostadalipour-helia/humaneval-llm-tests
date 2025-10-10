import unittest
from sut_llm.problem_HumanEval_66 import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        """
        Test case for an empty input string.
        This is an edge case and should return 0.
        """
        self.assertEqual(digitSum(""), 0)

    def test_string_with_only_lowercase_characters(self):
        """
        Test case for a string containing only lowercase characters.
        No uppercase characters means the sum should be 0.
        This tests the 'upper characters only' logic.
        """
        self.assertEqual(digitSum("abcdefg"), 0)

    def test_string_with_only_uppercase_characters(self):
        """
        Test case for a string containing only uppercase characters.
        This verifies the sum calculation for all relevant characters.
        Covers boundary characters 'A', 'B', 'C'.
        """
        # ord('A')=65, ord('B')=66, ord('C')=67
        self.assertEqual(digitSum("ABC"), 198)

    def test_mixed_case_string_example_1(self):
        """
        Test case with a mixed-case string, including an example from the docstring.
        Verifies correct filtering of uppercase characters.
        """
        # ord('A')=65, ord('B')=66
        self.assertEqual(digitSum("abAB"), 131)

    def test_string_with_non_alphabetic_and_mixed_case_characters(self):
        """
        Test case with numbers, symbols, and mixed-case letters.
        Ensures only uppercase letters are considered and non-alphabetic characters are ignored.
        This is an extreme/unusual input.
        """
        # ord('A')=65, ord('B')=66, ord('C')=67
        self.assertEqual(digitSum("123!@#ABCxyz"), 198)

    def test_single_uppercase_character(self):
        """
        Test case for a string with a single uppercase character.
        This is an edge case (single element) and tests the upper boundary 'Z'.
        """
        # ord('Z')=90
        self.assertEqual(digitSum("Z"), 90)

    def test_single_lowercase_character(self):
        """
        Test case for a string with a single lowercase character.
        This is an edge case (single element) and should result in 0.
        """
        self.assertEqual(digitSum("z"), 0)

    def test_string_with_all_same_uppercase_characters(self):
        """
        Test case for a string where all characters are the same uppercase letter.
        Verifies correct summation for duplicate values.
        """
        # 4 * ord('A') = 4 * 65 = 260
        self.assertEqual(digitSum("AAAA"), 260)

    def test_string_with_uppercase_at_ascii_boundaries_and_separator(self):
        """
        Test case with uppercase characters at the ASCII range boundaries ('A', 'Z')
        separated by a non-alphabetic character.
        This is a boundary condition test.
        """
        # ord('A')=65, ord('Z')=90
        self.assertEqual(digitSum("A_Z"), 155)

    def test_mixed_case_string_example_2(self):
        """
        Another test case with a mixed-case string from the docstring examples.
        Further verifies the logic for filtering and summing.
        """
        # ord('A')=65, ord('B')=66
        self.assertEqual(digitSum("woArBld"), 131)