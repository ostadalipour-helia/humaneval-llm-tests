import unittest
from sut.problem_HumanEval_17 import parse_music

class Test_parse_music(unittest.TestCase):

    def test_normal_case_mix(self):
        self.assertEqual(parse_music("o o| .| o| o| .| .| .| .| o o"), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_normal_case_simple(self):
        self.assertEqual(parse_music("o| .| o"), [2, 1, 4])

    def test_normal_case_all_quarter(self):
        self.assertEqual(parse_music(".| .| .| .|"), [1, 1, 1, 1])

    def test_edge_case_empty_string(self):
        self.assertEqual(parse_music(""), [])

    def test_edge_case_single_note(self):
        self.assertEqual(parse_music("o"), [4])

    def test_edge_case_extra_spaces(self):
        self.assertEqual(parse_music("   o   o|   .|   "), [4, 2, 1])

    def test_edge_case_all_same_note(self):
        self.assertEqual(parse_music("o o o o"), [4, 4, 4, 4])

    def test_error_invalid_note_symbol(self):
        with self.assertRaises(KeyError):
            parse_music("o x .|")

    def test_error_malformed_note(self):
        with self.assertRaises(KeyError):
            parse_music("o|o")

    def test_error_non_string_input(self):
        with self.assertRaises(AttributeError):
            parse_music(123)