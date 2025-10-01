import unittest
from sut.problem_HumanEval_144 import simplify

class TestSimplifyFunction(unittest.TestCase):

    def test_example_one(self):
        # Test case from docstring: 1/5 * 5/1 = 5/5 = 1 (whole number)
        self.assertTrue(simplify("1/5", "5/1"))

    def test_example_two(self):
        # Test case from docstring: 1/6 * 2/1 = 2/6 (not a whole number)
        self.assertFalse(simplify("1/6", "2/1"))

    def test_example_three(self):
        # Test case from docstring: 7/10 * 10/2 = 70/20 = 7/2 (not a whole number)
        self.assertFalse(simplify("7/10", "10/2"))

    def test_reciprocal_fractions(self):
        # Test case: 2/3 * 3/2 = 6/6 = 1 (whole number)
        self.assertTrue(simplify("2/3", "3/2"))

    def test_fraction_times_whole_number_result_whole(self):
        # Test case: 1/2 * 4/1 = 4/2 = 2 (whole number)
        self.assertTrue(simplify("1/2", "4/1"))

    def test_two_whole_numbers(self):
        # Test case: 3/1 * 2/1 = 6/1 = 6 (whole number)
        self.assertTrue(simplify("3/1", "2/1"))

    def test_product_is_fraction(self):
        # Test case: 1/2 * 1/2 = 1/4 (not a whole number)
        self.assertFalse(simplify("1/2", "1/2"))

    def test_cross_cancellation_to_whole_number(self):
        # Test case: 3/4 * 8/3 = 24/12 = 2 (whole number)
        self.assertTrue(simplify("3/4", "8/3"))

    def test_no_cancellation_not_whole(self):
        # Test case: 5/7 * 2/3 = 10/21 (not a whole number)
        self.assertFalse(simplify("5/7", "2/3"))

    def test_whole_number_times_fraction_result_whole(self):
        # Test case: 10/1 * 1/5 = 10/5 = 2 (whole number)
        self.assertTrue(simplify("10/1", "1/5"))

if __name__ == '__main__':
    unittest.main()