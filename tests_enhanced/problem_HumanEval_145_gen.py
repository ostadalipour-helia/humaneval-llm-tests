import unittest
from sut_llm.problem_HumanEval_145 import order_by_points

class TestOrderByPoints(unittest.TestCase):









    def test_09_duplicate_values_mixed_sums_logic_mutation(self):
        # Logic mutation: list with duplicate values, some having the same digit sum, others different.
        # Ensures stable sorting behavior for duplicates.
        # Input: [1, 11, 1, 2, 11]
        # (value, sum_digits, original_index) pairs:
        # (1, 1, 0), (11, 2, 1), (1, 1, 2), (2, 2, 3), (11, 2, 4)

        nums = [1, 11, 1, 2, 11]
        # Expected output based on the function's implementation:
        # (1, sum=1, index=0)
        # (1, sum=1, index=2)
        # (11, sum=2, index=1)
        # (2, sum=2, index=3)
        # (11, sum=2, index=4)
        expected_output = [1, 1, 11, 2, 11]
        result = order_by_points(nums)
        self.assertEqual(result, expected_output)

    def test_empty_list(self):
        """
        Test with an empty list to cover the 'if not nums' branch.
        """
        result = order_by_points([])
        self.assertEqual(result, [])

