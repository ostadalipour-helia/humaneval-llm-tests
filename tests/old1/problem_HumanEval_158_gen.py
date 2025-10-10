import unittest
from sut.problem_HumanEval_158 import find_max

class TestFindMax(unittest.TestCase):

    def test_example_one(self):
        # Docstring example: basic max unique characters
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_example_two(self):
        # Docstring example: tie-breaker by lexicographical order
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_example_three(self):
        # Docstring example: all words have 1 unique char, tie-breaker
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), "aaaaaaa")

    def test_single_word_list(self):
        # Test with a list containing only one word
        self.assertEqual(find_max(["hello"]), "hello")

    def test_different_lengths_clear_max(self):
        # Words with varying lengths and clear maximum unique characters
        self.assertEqual(find_max(["apple", "apply", "apricot"]), "apricot")

    def test_case_sensitivity_tie_breaker(self):
        # Test case sensitivity and lexicographical tie-breaker
        self.assertEqual(find_max(["Apple", "apple"]), "Apple")

    def test_all_one_unique_char_tie_breaker(self):
        # All words have one unique character, tie-breaker applies
        self.assertEqual(find_max(["z", "a", "b"]), "a")

    def test_clear_max_unique_different_lengths(self):
        # Clear maximum unique characters with words of different lengths
        self.assertEqual(find_max(["cat", "dog", "elephant"]), "elephant")

    def test_multiple_words_with_clear_max(self):
        # Multiple words, one clearly has the most unique characters
        self.assertEqual(find_max(["python", "java", "javascript", "csharp"]), "javascript")

    def test_all_same_unique_count_tie_breaker(self):
        # All words have the same number of unique characters, tie-breaker applies
        self.assertEqual(find_max(["abc", "bca", "cab"]), "abc")

if __name__ == '__main__':
    unittest.main()