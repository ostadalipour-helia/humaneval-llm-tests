import unittest
from sut_llm.problem_HumanEval_152 import compare

class TestCompare(unittest.TestCase):

    def test_1_all_correct_guesses(self):
        # Test case where all guesses are perfectly correct (all zeros in output)
        # Covers: Logic Mutation (all true), Return Value (all 0s), Typical Input
        game = [1, 2, 3, 4, 5]
        guess = [1, 2, 3, 4, 5]
        expected = [0, 0, 0, 0, 0]
        self.assertListEqual(compare(game, guess), expected)

    def test_2_all_incorrect_guesses(self):
        # Test case where all guesses are incorrect (all non-zero absolute differences)
        # Covers: Logic Mutation (all false), Return Value (all non-0s), Typical Input
        game = [1, 2, 3, 4, 5]
        guess = [6, 7, 8, 9, 10]
        expected = [5, 5, 5, 5, 5]
        self.assertListEqual(compare(game, guess), expected)

    def test_3_mixed_correct_and_incorrect_docstring_example_1(self):
        # Test case with a mix of correct and incorrect guesses, including negative guess
        # Covers: Typical Input, Return Value (mixed 0s and non-0s), Sign Testing (negative guess)
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected = [0, 0, 0, 0, 3, 3]
        self.assertListEqual(compare(game, guess), expected)

    def test_4_empty_lists_edge_case(self):
        # Test case with empty input lists
        # Covers: Edge Case (empty collection)
        game = []
        guess = []
        expected = []
        self.assertListEqual(compare(game, guess), expected)

    def test_5_single_element_list_edge_case(self):
        # Test case with single-element lists, both correct and incorrect
        # Covers: Edge Case (single element collection), Off-by-One (list length)
        game = [7]
        guess = [5]
        expected = [2]
        self.assertListEqual(compare(game, guess), expected)

    def test_6_boundary_off_by_one_differences(self):
        # Test case where guesses are exactly game-1, game, or game+1
        # Covers: Boundary Testing (n, n-1, n+1), Off-by-One (value difference)
        game = [10, 10, 10, 10]
        guess = [9, 10, 11, 8]
        expected = [1, 0, 1, 2]
        self.assertListEqual(compare(game, guess), expected)

    def test_7_sign_and_zero_testing(self):
        # Test case involving zero, negative numbers, and differences across zero
        # Covers: Sign and Zero Testing, Extreme/Unusual Input
        game = [0, -5, 10, -3]
        guess = [0, -2, 12, -7]
        expected = [0, 3, 2, 4] # abs(-5 - -2) = abs(-3) = 3; abs(-3 - -7) = abs(4) = 4
        self.assertListEqual(compare(game, guess), expected)

    def test_8_extreme_large_numbers(self):
        # Test case with very large numbers to check robustness
        # Covers: Extreme/Unusual Input
        game = [1000000000, 1, 500000000]
        guess = [999999999, 100, 500000000]
        expected = [1, 99, 0]
        self.assertListEqual(compare(game, guess), expected)

    def test_9_duplicate_values_and_boundary_around_zero(self):
        # Test case with duplicate values in game, and guesses around zero
        # Covers: Edge Case (duplicate values), Boundary Testing (around zero)
        game = [0, 0, 0, 5, 5]
        guess = [0, 1, -1, 5, 6]
        expected = [0, 1, 1, 0, 1]
        self.assertListEqual(compare(game, guess), expected)

    def test_10_mixed_correct_and_incorrect_docstring_example_2(self):
        # Another example from the docstring, with zeros and negatives
        # Covers: Typical Input, Return Value, Sign and Zero Testing
        game = [0, 5, 0, 0, 0, 4]
        guess = [4, 1, 1, 0, 0, -2]
        expected = [4, 4, 1, 0, 0, 6]
        self.assertListEqual(compare(game, guess), expected)