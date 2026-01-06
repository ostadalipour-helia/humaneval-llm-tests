import unittest
from sut.problem_HumanEval_152 import compare

class Test_compare(unittest.TestCase):
    def test_normal_mixed_matches_mismatches(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected_output = [0, 0, 0, 0, 3, 3]
        self.assertEqual(compare(game, guess), expected_output)

    def test_normal_one_match_two_mismatches(self):
        game = [10, 20, 30]
        guess = [10, 15, 35]
        expected_output = [0, 5, 5]
        self.assertEqual(compare(game, guess), expected_output)

    def test_edge_empty_lists(self):
        game = []
        guess = []
        expected_output = []
        self.assertEqual(compare(game, guess), expected_output)

    def test_edge_all_elements_match(self):
        game = [1, 2, 3]
        guess = [1, 2, 3]
        expected_output = [0, 0, 0]
        self.assertEqual(compare(game, guess), expected_output)

    def test_edge_no_elements_match(self):
        game = [1, 2, 3]
        guess = [4, 5, 6]
        expected_output = [3, 3, 3]
        self.assertEqual(compare(game, guess), expected_output)

    def test_edge_floating_point_numbers(self):
        game = [1.5, 2.0]
        guess = [1.0, 2.0]
        expected_output = [0.5, 0.0]
        self.assertEqual(compare(game, guess), expected_output)

    def test_edge_large_and_negative_numbers(self):
        game = [100, -50, 0]
        guess = [-100, 50, 0]
        expected_output = [200, 100, 0]
        self.assertEqual(compare(game, guess), expected_output)

    def test_error_game_not_list(self):
        game = "not a list"
        guess = [1, 2]
        with self.assertRaises(TypeError):
            compare(game, guess)

    def test_error_guess_not_list(self):
        game = [1, 2]
        guess = "not a list"
        with self.assertRaises(TypeError):
            compare(game, guess)

    def test_error_different_lengths(self):
        game = [1, 2]
        guess = [1]
        # The spec allows ValueError or IndexError. ValueError is more common for length mismatch.
        with self.assertRaises((ValueError, IndexError)):
            compare(game, guess)

    def test_error_game_elements_not_numbers(self):
        game = [1, "a"]
        guess = [1, 2]
        with self.assertRaises(TypeError):
            compare(game, guess)

    def test_error_guess_elements_not_numbers(self):
        game = [1, 2]
        guess = [1, None] # 'null' in JSON translates to None in Python
        with self.assertRaises(TypeError):
            compare(game, guess)