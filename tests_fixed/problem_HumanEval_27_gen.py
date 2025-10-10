import unittest
from sut_llm.problem_HumanEval_27 import flip_case

class TestFlipCase(unittest.TestCase):

    def test_basic_mixed_case(self):
        """
        Test a typical string with mixed upper and lower case characters.
        Covers: Typical input, mixed case.
        """
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_all_lowercase(self):
        """
        Test a string consisting entirely of lowercase characters.
        Covers: All characters flip from lower to upper. Catches if islower() check is wrong.
        """
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_all_uppercase(self):
        """
        Test a string consisting entirely of uppercase characters.
        Covers: All characters flip from upper to lower. Catches if isupper() check is wrong.
        """
        self.assertEqual(flip_case('WORLD'), 'world')

    def test_empty_string(self):
        """
        Test with an empty string.
        Covers: Edge case (empty collection), boundary condition.
        """
        self.assertEqual(flip_case(''), '')

    def test_single_lowercase_character(self):
        """
        Test with a single lowercase character.
        Covers: Edge case (single element), boundary for character set ('a').
        """
        self.assertEqual(flip_case('a'), 'A')

    def test_single_uppercase_character(self):
        """
        Test with a single uppercase character.
        Covers: Edge case (single element), boundary for character set ('Z').
        """
        self.assertEqual(flip_case('Z'), 'z')

    def test_string_with_non_alphabetic_characters(self):
        """
        Test a string containing numbers and symbols, along with letters.
        Covers: Unusual input, non-alphabetic characters should remain unchanged.
        """
        self.assertEqual(flip_case('123!@#$Hello'), '123!@#$hELLO')

    def test_mixed_case_with_numbers_and_symbols(self):
        """
        Test a complex string with mixed case, numbers, and symbols.
        Covers: Typical/complex input, verifies correct handling of all character types.
        """
        self.assertEqual(flip_case('PyThOn3.10'), 'pYtHoN3.10')

    def test_long_alternating_case_string(self):
        """
        Test a long string with alternating cases to check for consistent flipping.
        Covers: Extreme input, verifies consistent behavior over length.
        """
        self.assertEqual(flip_case('aBcDeFgHiJkLmNoPqRsTuVwXyZ'), 'AbCdEfGhIjKlMnOpQrStUvWxYz')

    def test_string_only_non_alphabetic_characters(self):
        """
        Test a string consisting entirely of non-alphabetic characters.
        Covers: Edge case, extreme input. All characters should remain unchanged.
        """
        self.assertEqual(flip_case('!@#$%^&*()_+-='), '!@#$%^&*()_+-=')