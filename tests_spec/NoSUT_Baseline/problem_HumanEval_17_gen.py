import unittest
import sut.problem_HumanEval_17 as mod

class TestHybrid(unittest.TestCase):
    def test_01_docstring_example(self):
            """Test with the example provided in the docstring."""
            music_string = 'o o| .| o| o| .| .| .| .| o o'
            expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_02_empty_string_edge_case(self):
            """Test with an empty input string."""
            music_string = ''
            expected_output = []
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_03_single_whole_note_boundary(self):
            """Test with a single whole note 'o'."""
            music_string = 'o'
            expected_output = [4]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_04_single_half_note_boundary(self):
            """Test with a single half note 'o|'."""
            music_string = 'o|'
            expected_output = [2]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_05_single_quarter_note_boundary(self):
            """Test with a single quarter note '.|'."""
            music_string = '.|'
            expected_output = [1]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_06_all_whole_notes_extreme_input(self):
            """Test with a sequence consisting only of whole notes."""
            music_string = 'o o o o o o'
            expected_output = [4, 4, 4, 4, 4, 4]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_07_all_quarter_notes_extreme_input(self):
            """Test with a sequence consisting only of quarter notes."""
            music_string = '.| .| .| .| .| .|'
            expected_output = [1, 1, 1, 1, 1, 1]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_08_mixed_notes_short_sequence_logic_mutation(self):
            """Test a short sequence with all note types to check parsing logic."""
            music_string = 'o| .| o'
            expected_output = [2, 1, 4]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_09_long_mixed_sequence_typical_input(self):
            """Test a longer sequence with mixed notes and repetitions."""
            music_string = 'o o| .| o o| .| o o| .|'
            expected_output = [4, 2, 1, 4, 2, 1, 4, 2, 1]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_10_parsing_precedence_logic_mutation(self):
            """Test specific order of notes ('o|' before 'o') to catch precedence issues."""
            music_string = 'o| o .| o| o'
            expected_output = [2, 4, 1, 2, 4]
            self.assertListEqual(mod.parse_music(music_string), expected_output)

    def test_normal_mixed_notes(self):
            # Example from the docstring with a mix of all note types.
            music_string = "o o| .| o| o| .| .| .| .| o o"
            expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_normal_simple_sequence(self):
            # A simple sequence of different notes.
            music_string = "o| .| o"
            expected_output = [2, 1, 4]
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_normal_only_quarter_notes(self):
            # A sequence of only quarter notes.
            music_string = ".| .| .| .|"
            expected_output = [1, 1, 1, 1]
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_edge_empty_string(self):
            # An empty input string should result in an empty list.
            music_string = ""
            expected_output = []
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_edge_single_whole_note(self):
            # A single whole note.
            music_string = "o"
            expected_output = [4]
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_edge_with_extra_spaces(self):
            # Input string with leading, trailing, and multiple spaces between notes.
            music_string = "   o   o|   .|   "
            expected_output = [4, 2, 1]
            self.assertEqual(mod.parse_music(music_string), expected_output)

    def test_edge_only_one_type_of_note(self):
            # Input string with only one type of note.
            music_string = "o o o o"
            expected_output = [4, 4, 4, 4]
            self.assertEqual(mod.parse_music(music_string), expected_output)

