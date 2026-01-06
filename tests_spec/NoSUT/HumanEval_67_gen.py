import unittest
from sut.problem_HumanEval_67 import fruit_distribution

class Test_fruit_distribution(unittest.TestCase):
    def test_normal_positive_counts(self):
        # Typical case with positive counts for all fruits.
        s = "5 apples and 6 oranges"
        n = 19
        expected_output = 8
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_normal_zero_apples(self):
        # Case with zero apples.
        s = "0 apples and 1 oranges"
        n = 3
        expected_output = 2
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_normal_larger_total_fruits(self):
        # Case with a larger total number of fruits.
        s = "2 apples and 3 oranges"
        n = 100
        expected_output = 95
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_edge_no_fruits_specified(self):
        # No apples and no oranges specified.
        s = "0 apples and 0 oranges"
        n = 5
        expected_output = 5
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_edge_zero_mangoes(self):
        # Total fruits equals the sum of apples and oranges, resulting in zero mangoes.
        s = "10 apples and 20 oranges"
        n = 30
        expected_output = 0
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_edge_large_numbers(self):
        # Large numbers for fruit counts.
        s = "999999 apples and 1 oranges"
        n = 1000001
        expected_output = 1
        self.assertEqual(fruit_distribution(s, n), expected_output)

    def test_error_invalid_fruit_name(self):
        # String 's' does not contain 'apples' keyword.
        s = "5 bananas and 6 oranges"
        n = 19
        with self.assertRaises(ValueError):
            fruit_distribution(s, n)

    def test_error_non_integer_orange_count(self):
        # String 's' contains non-integer count for oranges.
        s = "5 apples and six oranges"
        n = 19
        with self.assertRaises(ValueError):
            fruit_distribution(s, n)

    def test_error_missing_apple_count(self):
        # String 's' is missing count for apples.
        s = "apples and 6 oranges"
        n = 19
        with self.assertRaises(ValueError):
            fruit_distribution(s, n)

    def test_error_n_not_integer(self):
        # Input 'n' is not an integer.
        s = "5 apples and 6 oranges"
        n = "twenty"
        with self.assertRaises(TypeError):
            fruit_distribution(s, n)

    def test_error_n_less_than_fruits(self):
        # Total fruits 'n' is less than the sum of apples and oranges, leading to a negative mango count.
        s = "5 apples and 6 oranges"
        n = 10
        with self.assertRaises(ValueError):
            fruit_distribution(s, n)

    def test_error_n_negative(self):
        # Total fruits 'n' is negative.
        s = "5 apples and 6 oranges"
        n = -5
        with self.assertRaises(ValueError):
            fruit_distribution(s, n)