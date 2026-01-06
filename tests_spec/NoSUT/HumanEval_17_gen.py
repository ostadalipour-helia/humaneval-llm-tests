import unittest
from sut.problem_HumanEval_17 import parse_music

class Test_parse_music(unittest.TestCase):

    def test_normal_mixed_notes(self):
        # Example from the docstring with a mix of all note types.
        music_string = "o o| .| o| o| .| .| .| .| o o"
        expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_normal_simple_sequence(self):
        # A simple sequence of different notes.
        music_string = "o| .| o"
        expected_output = [2, 1, 4]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_normal_only_quarter_notes(self):
        # A sequence of only quarter notes.
        music_string = ".| .| .| .|"
        expected_output = [1, 1, 1, 1]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_edge_empty_string(self):
        # An empty input string should result in an empty list.
        music_string = ""
        expected_output = []
        self.assertEqual(parse_music(music_string), expected_output)

    def test_edge_single_whole_note(self):
        # A single whole note.
        music_string = "o"
        expected_output = [4]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_edge_with_extra_spaces(self):
        # Input string with leading, trailing, and multiple spaces between notes.
        music_string = "   o   o|   .|   "
        expected_output = [4, 2, 1]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_edge_only_one_type_of_note(self):
        # Input string with only one type of note.
        music_string = "o o o o"
        expected_output = [4, 4, 4, 4]
        self.assertEqual(parse_music(music_string), expected_output)

    def test_error_input_none(self):
        # Input is not a string (None).
        with self.assertRaises(TypeError):
            parse_music(None)

    def test_error_input_integer(self):
        # Input is an integer, not a string.
        with self.assertRaises(TypeError):
            parse_music(123)

    def test_error_invalid_note_symbol_x(self):
        # Input contains an invalid note symbol 'x'.
        with self.assertRaises(ValueError):
            parse_music("o x .|")

    def test_error_malformed_note_no_space(self):
        # Input contains a malformed note 'o|o' (missing space delimiter).
        with self.assertRaises(ValueError):
            parse_music("o|o")

    def test_error_invalid_note_symbol_o_pipe_pipe(self):
        # Input contains an invalid note symbol 'o||'.
        with self.assertRaises(ValueError):
            parse_music("o||")