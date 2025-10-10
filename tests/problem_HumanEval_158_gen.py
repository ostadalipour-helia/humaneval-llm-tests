import unittest
from sut.problem_HumanEval_158 import find_max

class TestFindMax(unittest.TestCase):

    def test_example_one_clear_winner(self):
        # Docstring example: clear winner by unique character count
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_example_two_lexicographical_tie_break(self):
        # Docstring example: multiple words with max unique, tie-break by lexicographical order
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_example_three_all_same_unique_count_tie_break(self):
        # Docstring example: all words have same (minimal) unique count, tie-break by lexicographical order
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_edge_case_empty_list(self):
        # Edge case: empty input list. Assumes an empty string is returned.
        self.assertEqual(find_max([]), "")

    def test_edge_case_single_element_list(self):
        # Edge case: list with a single word.
        self.assertEqual(find_max(["hello"]), "hello")

    def test_boundary_two_elements_clear_winner(self):
        # Boundary: list with two elements, one clearly has more unique characters.
        self.assertEqual(find_max(["a", "abc"]), "abc")

    def test_boundary_two_elements_lexicographical_tie_break(self):
        # Boundary: list with two elements, same unique count, tie-break by lexicographical order.
        self.assertEqual(find_max(["b", "a"]), "a")

    def test_logic_mutation_different_lengths_same_unique_tie_break(self):
        # Logic mutation: words with different lengths but same max unique count, requiring lexicographical tie-break.
        # "apple": 4 unique, "banana": 3 unique, "aple": 4 unique. "aple" comes before "apple".
        self.assertEqual(find_max(["apple", "banana", "aple"]), "aple")

    def test_extreme_input_all_unique_chars_word(self):
        # Extreme input: a word with many unique characters vs others with fewer.
        self.assertEqual(find_max(["abcdefg", "hello", "world", "python"]), "abcdefg")

    def test_boundary_all_one_unique_char_lexicographical_tie_break(self):
        # Boundary: all words have only one unique character, requiring lexicographical tie-break.
        self.assertEqual(find_max(["zzzz", "aaaa", "bbbb"]), "aaaa")