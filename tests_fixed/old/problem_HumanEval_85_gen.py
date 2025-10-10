import unittest
from sut_llm.problem_HumanEval_85 import add

class TestAddFunction(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_single_element_list(self):
        # Single element list, index 0 is even, so no elements at odd indices.
        self.assertEqual(add([10]), 0)

    def test_two_elements_second_even(self):
        # Index 1 (odd) has value 2 (even).
        self.assertEqual(add([1, 2]), 2)

    def test_two_elements_second_odd(self):
        # Index 1 (odd) has value 3 (odd).
        self.assertEqual(add([1, 3]), 0)

    def test_all_even_some_at_odd_indices(self):
        # Index 1 (20), Index 3 (40) contribute.
        self.assertEqual(add([10, 20, 30, 40, 50]), 60)

    def test_all_odd_no_contribution(self):
        # All elements are odd, so none contribute even if at odd indices.
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)

    def test_negative_numbers(self):
        # Index 1 (-2), Index 3 (-4) contribute.
        self.assertEqual(add([-1, -2, -3, -4, -5]), -6)

    def test_list_with_zeros(self):
        # Index 1 (0), Index 3 (0) contribute.
        self.assertEqual(add([0, 0, 0, 0]), 0)

    def test_longer_mixed_list(self):
        # Index 1 (1, odd), Index 3 (2, even), Index 5 (3, odd), Index 7 (4, even), Index 9 (5, odd)
        # Only 2 and 4 contribute.
        self.assertEqual(add([100, 1, 200, 2, 300, 3, 400, 4, 500, 5]), 6)

    def test_list_with_only_odd_indices_contributing(self):
        # Only elements at odd indices are even.
        self.assertEqual(add([1, 10, 3, 20, 5, 30]), 60)

if __name__ == '__main__':
    unittest.main()