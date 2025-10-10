import unittest
from sut_llm.problem_HumanEval_67 import fruit_distribution

class TestFruitDistribution(unittest.TestCase):

    def test_example_1(self):
        # From docstring example: "5 apples and 6 oranges", 19 -> 19 - 5 - 6 = 8
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_example_2(self):
        # From docstring example: "0 apples and 1 oranges",3 -> 3 - 0 - 1 = 2
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_example_3(self):
        # From docstring example: "2 apples and 3 oranges", 100 -> 100 - 2 - 3 = 95
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_example_4(self):
        # From docstring example: "100 apples and 1 oranges",120 -> 120 - 100 - 1 = 19
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_no_apples_no_oranges(self):
        # Test case with zero apples and zero oranges
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 10), 10)

    def test_only_apples(self):
        # Test case with only apples, no oranges
        self.assertEqual(fruit_distribution("7 apples and 0 oranges", 15), 8)

    def test_only_oranges(self):
        # Test case with only oranges, no apples
        self.assertEqual(fruit_distribution("0 apples and 4 oranges", 12), 8)

    def test_sum_equals_total(self):
        # Test case where apples + oranges equals total fruits
        self.assertEqual(fruit_distribution("10 apples and 5 oranges", 15), 0)

    def test_large_numbers(self):
        # Test case with larger numbers for fruits
        self.assertEqual(fruit_distribution("500 apples and 250 oranges", 1000), 250)

    def test_arbitrary_numbers(self):
        # Test case with arbitrary numbers
        self.assertEqual(fruit_distribution("123 apples and 456 oranges", 1000), 421)

if __name__ == '__main__':
    unittest.main()