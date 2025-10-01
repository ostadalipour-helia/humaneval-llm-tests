import unittest
from sut.problem_HumanEval_111 import histogram

class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(histogram(''), {})

    def test_single_letter(self):
        """Test with a single letter input."""
        self.assertEqual(histogram('a'), {'a': 1})

    def test_all_unique_letters(self):
        """Test with multiple unique letters, all having count 1."""
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})

    def test_two_letters_one_repeated(self):
        """Test with two distinct letters, one repeated more."""
        self.assertEqual(histogram('a b a'), {'a': 2})

    def test_two_letters_both_repeated_equally(self):
        """Test with two distinct letters, both repeated equally as max."""
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})

    def test_three_letters_two_repeated_equally_as_max(self):
        """Test with three distinct letters, two repeated equally as max."""
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})

    def test_one_letter_repeated_many_times(self):
        """Test with one letter significantly more frequent than others."""
        self.assertEqual(histogram('b b b b a'), {'b': 4})

    def test_multiple_letters_with_different_counts_one_max(self):
        """Test with various counts, one clear maximum frequency."""
        self.assertEqual(histogram('a a b c c c d'), {'c': 3})

    def test_multiple_letters_with_multiple_max_counts(self):
        """Test with several letters sharing the maximum frequency."""
        self.assertEqual(histogram('x y z x y z x y'), {'x': 3, 'y': 3})

    def test_longer_string_with_one_dominant_letter(self):
        """Test with a longer string where one letter is clearly dominant."""
        self.assertEqual(histogram('a a a b b c c c c d d d d d e f g h i j k l m n o p q r s t u v w x y z'), {'d': 5})

if __name__ == '__main__':
    unittest.main()