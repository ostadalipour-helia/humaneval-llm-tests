import unittest
from sut.problem_HumanEval_17 import parse_music

class TestParseMusic(unittest.TestCase):

    def test_01_docstring_example(self):
        """Test with the example provided in the docstring."""
        music_string = 'o o| .| o| o| .| .| .| .| o o'
        expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_02_empty_string_edge_case(self):
        """Test with an empty input string."""
        music_string = ''
        expected_output = []
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_03_single_whole_note_boundary(self):
        """Test with a single whole note 'o'."""
        music_string = 'o'
        expected_output = [4]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_04_single_half_note_boundary(self):
        """Test with a single half note 'o|'."""
        music_string = 'o|'
        expected_output = [2]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_05_single_quarter_note_boundary(self):
        """Test with a single quarter note '.|'."""
        music_string = '.|'
        expected_output = [1]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_06_all_whole_notes_extreme_input(self):
        """Test with a sequence consisting only of whole notes."""
        music_string = 'o o o o o o'
        expected_output = [4, 4, 4, 4, 4, 4]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_07_all_quarter_notes_extreme_input(self):
        """Test with a sequence consisting only of quarter notes."""
        music_string = '.| .| .| .| .| .|'
        expected_output = [1, 1, 1, 1, 1, 1]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_08_mixed_notes_short_sequence_logic_mutation(self):
        """Test a short sequence with all note types to check parsing logic."""
        music_string = 'o| .| o'
        expected_output = [2, 1, 4]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_09_long_mixed_sequence_typical_input(self):
        """Test a longer sequence with mixed notes and repetitions."""
        music_string = 'o o| .| o o| .| o o| .|'
        expected_output = [4, 2, 1, 4, 2, 1, 4, 2, 1]
        self.assertListEqual(parse_music(music_string), expected_output)

    def test_10_parsing_precedence_logic_mutation(self):
        """Test specific order of notes ('o|' before 'o') to catch precedence issues."""
        music_string = 'o| o .| o| o'
        expected_output = [2, 4, 1, 2, 4]
        self.assertListEqual(parse_music(music_string), expected_output)