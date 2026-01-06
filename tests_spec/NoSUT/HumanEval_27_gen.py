import unittest
from sut.problem_HumanEval_27 import flip_case

class Test_flip_case(unittest.TestCase):
    def test_normal_mixed_case(self):
        # Description: Mixed case string with standard letters.
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_normal_all_uppercase(self):
        # Description: All uppercase string.
        self.assertEqual(flip_case('WORLD'), 'world')

    def test_normal_all_lowercase(self):
        # Description: All lowercase string.
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_normal_alternating_case(self):
        # Description: Alternating case string.
        self.assertEqual(flip_case('PyThOn'), 'pYtHoN')

    def test_edge_empty_string(self):
        # Description: Empty string.
        self.assertEqual(flip_case(''), '')

    def test_edge_non_alphabetic_characters(self):
        # Description: String with only non-alphabetic characters.
        self.assertEqual(flip_case('123!@#'), '123!@#')

    def test_edge_mixed_alphanumeric_spaces(self):
        # Description: String with mixed alphabetic and non-alphabetic characters including spaces.
        self.assertEqual(flip_case('Hello World 123!'), 'hELLO wORLD 123!')

    def test_edge_single_lowercase_character(self):
        # Description: Single lowercase character.
        self.assertEqual(flip_case('a'), 'A')

    def test_edge_single_uppercase_character(self):
        # Description: Single uppercase character.
        self.assertEqual(flip_case('Z'), 'z')

    def test_error_none_input(self):
        # Description: Input is not a string (NoneType).
        with self.assertRaises(TypeError):
            flip_case(None)

    def test_error_integer_input(self):
        # Description: Input is not a string (integer).
        with self.assertRaises(TypeError):
            flip_case(123)

    def test_error_list_input(self):
        # Description: Input is not a string (list).
        with self.assertRaises(TypeError):
            flip_case([1, 'a'])