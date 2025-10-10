import unittest
from sut.problem_HumanEval_17 import parse_music


class TestParseMusic(unittest.TestCase):

    def test_docstring_example(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_single_whole_note(self):
        self.assertEqual(parse_music('o'), [4])

    def test_single_half_note(self):
        self.assertEqual(parse_music('o|'), [2])

    def test_single_quarter_note(self):
        self.assertEqual(parse_music('.|'), [1])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_all_whole_notes(self):
        self.assertEqual(parse_music('o o o o'), [4, 4, 4, 4])

    def test_all_half_notes(self):
        self.assertEqual(parse_music('o| o| o|'), [2, 2, 2])

    def test_all_quarter_notes(self):
        self.assertEqual(parse_music('.| .| .| .| .|'), [1, 1, 1, 1, 1])

    def test_mixed_short_sequence(self):
        self.assertEqual(parse_music('o .| o|'), [4, 1, 2])

    def test_longer_mixed_sequence(self):
        self.assertEqual(parse_music('o o| .| o o| .| o'), [4, 2, 1, 4, 2, 1, 4])


if __name__ == '__main__':
    unittest.main()