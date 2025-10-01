import unittest
from sut.problem_HumanEval_159 import eat

class TestEatFunction(unittest.TestCase):

    def test_example_1_sufficient_remaining(self):
        # Example from docstring: remaining carrots are more than needed
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_example_2_sufficient_remaining(self):
        # Example from docstring: remaining carrots are more than needed
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_example_3_exact_remaining(self):
        # Example from docstring: remaining carrots exactly match needed
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_example_4_insufficient_remaining(self):
        # Example from docstring: remaining carrots are less than needed
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_need_is_zero(self):
        # No carrots are needed, so total eaten and remaining should be unchanged
        self.assertEqual(eat(10, 0, 50), [10, 50])

    def test_remaining_is_zero(self):
        # No carrots are available to eat, so total eaten and remaining are unchanged
        self.assertEqual(eat(5, 10, 0), [5, 0])

    def test_initial_eaten_is_zero(self):
        # Rabbit starts with 0 eaten carrots, sufficient remaining
        self.assertEqual(eat(0, 5, 10), [5, 5])

    def test_remaining_just_equals_need(self):
        # All remaining carrots are eaten to satisfy the need exactly
        self.assertEqual(eat(100, 50, 50), [150, 0])

    def test_remaining_just_less_than_need(self):
        # All remaining carrots are eaten, but it's not enough to satisfy the need
        self.assertEqual(eat(100, 51, 50), [150, 0])

    def test_max_inputs_exact_remaining(self):
        # Test with maximum allowed input values, remaining exactly equals need
        self.assertEqual(eat(1000, 1000, 1000), [2000, 0])