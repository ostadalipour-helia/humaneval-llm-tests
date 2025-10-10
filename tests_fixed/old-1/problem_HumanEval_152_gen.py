import unittest
from sut_llm.problem_HumanEval_152 import compare

class TestCompare(unittest.TestCase):

    def test_1(self):
        # Example from docstring
        game = [1,2,3,4,5,1]
        guess = [1,2,3,4,2,-2]
        expected = [0,0,0,0,3,3]
        self.assertEqual(compare(game, guess), expected)

    def test_2(self):
        # Second example from docstring
        game = [0,5,0,0,0,4]
        guess = [4,1,1,0,0,-2]
        expected = [4,4,1,0,0,6]
        self.assertEqual(compare(game, guess), expected)

    def test_3(self):
        # All guesses are correct
        game = [10, 20, 30]
        guess = [10, 20, 30]
        expected = [0, 0, 0]
        self.assertEqual(compare(game, guess), expected)

    def test_4(self):
        # All guesses are incorrect, guess > game
        game = [1, 2, 3]
        guess = [2, 4, 6]
        expected = [1, 2, 3]
        self.assertEqual(compare(game, guess), expected)

    def test_5(self):
        # All guesses are incorrect, guess < game
        game = [5, 4, 3]
        guess = [1, 2, 1]
        expected = [4, 2, 2]
        self.assertEqual(compare(game, guess), expected)

    def test_6(self):
        # Mixed correct/incorrect, including zeros and negative guesses
        game = [0, 10, -5, 7]
        guess = [0, 5, -10, 7]
        expected = [0, 5, 5, 0]
        self.assertEqual(compare(game, guess), expected)

    def test_7(self):
        # Single element array, correct guess
        game = [42]
        guess = [42]
        expected = [0]
        self.assertEqual(compare(game, guess), expected)

    def test_8(self):
        # Single element array, incorrect guess
        game = [100]
        guess = [50]
        expected = [50]
        self.assertEqual(compare(game, guess), expected)

    def test_9(self):
        # Longer array with various differences
        game = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        guess = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = [1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(compare(game, guess), expected)

    def test_10(self):
        # Empty arrays
        game = []
        guess = []
        expected = []
        self.assertEqual(compare(game, guess), expected)

if __name__ == '__main__':
    unittest.main()