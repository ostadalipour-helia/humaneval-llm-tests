import unittest
from sut.problem_HumanEval_152 import compare

class Test_compare(unittest.TestCase):

    def test_case_0(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected = [0, 0, 0, 0, 3, 3]
        self.assertEqual(compare(game, guess), expected)

    def test_case_1(self):
        game = [0, 5, 0, 0, 0, 4]
        guess = [4, 1, 1, 0, 0, -2]
        expected = [4, 4, 1, 0, 0, 6]
        self.assertEqual(compare(game, guess), expected)

    def test_case_2(self):
        game = [10, 20, 30]
        guess = [10, 15, 35]
        expected = [0, 5, 5]
        self.assertEqual(compare(game, guess), expected)

    def test_case_3(self):
        game = []
        guess = []
        expected = []
        self.assertEqual(compare(game, guess), expected)

    def test_case_4(self):
        game = [7]
        guess = [7]
        expected = [0]
        self.assertEqual(compare(game, guess), expected)

    def test_case_5(self):
        game = [7]
        guess = [10]
        expected = [3]
        self.assertEqual(compare(game, guess), expected)

    def test_case_6(self):
        game = [1, 2, 3]
        guess = [1, 2, 3]
        expected = [0, 0, 0]
        self.assertEqual(compare(game, guess), expected)

    def test_case_7(self):
        game = [1, 2, 3]
        guess = [4, 5, 6]
        expected = [3, 3, 3]
        self.assertEqual(compare(game, guess), expected)

    def test_case_8(self):
        game = [0, 0, 0]
        guess = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(compare(game, guess), expected)

    def test_case_9(self):
        game = [100, -50, 0]
        guess = [-100, 50, 0]
        expected = [200, 100, 0]
        self.assertEqual(compare(game, guess), expected)