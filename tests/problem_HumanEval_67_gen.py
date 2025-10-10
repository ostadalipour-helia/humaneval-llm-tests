import unittest
from sut.problem_HumanEval_67 import fruit_distribution

class TestFruitDistribution(unittest.TestCase):

    def test_example_one(self):
        # Typical case from docstring: 5 apples, 6 oranges, 19 total -> 8 mangoes
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_example_two(self):
        # Typical case from docstring: 0 apples, 1 orange, 3 total -> 2 mangoes
        # Also covers X=0 and Y=1 (single element)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_zero_mangoes(self):
        # Boundary condition: total fruits equals sum of apples and oranges
        # Tests X+Y = n
        self.assertEqual(fruit_distribution("10 apples and 15 oranges", 25), 0)

    def test_one_mango(self):
        # Off-by-one error check: total fruits is just one more than apples and oranges
        # Tests X+Y = n-1
        self.assertEqual(fruit_distribution("7 apples and 8 oranges", 16), 1)

    def test_only_apples(self):
        # Boundary condition: zero oranges (Y=0)
        self.assertEqual(fruit_distribution("12 apples and 0 oranges", 20), 8)

    def test_only_oranges(self):
        # Boundary condition: zero apples (X=0)
        self.assertEqual(fruit_distribution("0 apples and 9 oranges", 15), 6)

    def test_no_apples_no_oranges(self):
        # Edge case: zero apples and zero oranges (X=0, Y=0)
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 7), 7)

    def test_large_numbers(self):
        # Extreme input: large number of apples and total fruits
        # Tests robustness with larger values
        self.assertEqual(fruit_distribution("999 apples and 1 oranges", 1001), 1)

    def test_minimum_total_fruits(self):
        # Edge case: total fruits is zero, implies zero mangoes if apples/oranges are also zero
        # Tests n=0
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 0), 0)

    def test_n_just_greater_than_sum(self):
        # Off-by-one error check: total fruits is just one more than apples and oranges, different values
        # Tests X+Y = n-1 again with different numbers to ensure consistency
        self.assertEqual(fruit_distribution("49 apples and 50 oranges", 100), 1)