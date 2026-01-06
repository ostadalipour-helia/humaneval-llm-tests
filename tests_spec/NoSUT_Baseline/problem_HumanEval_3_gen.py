import unittest
import sut.problem_HumanEval_3 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_operations(self):
            """
            Test with an empty list of operations.
            Balance should remain 0, so it should return False.
            Covers: Edge case (empty list), Return Value (False).
            """
            operations = []
            self.assertEqual(mod.below_zero(operations), False)

    def test_only_deposits(self):
            """
            Test with only positive deposit operations.
            Balance should always be positive, so it should return False.
            Covers: Typical input, Sign testing (only positive), Return Value (False).
            """
            operations = [10, 20, 5, 100]
            self.assertEqual(mod.below_zero(operations), False)

    def test_immediate_withdrawal(self):
            """
            Test with a single negative operation that immediately makes balance below zero.
            Covers: Edge case (single negative element), Boundary (first operation), Return Value (True).
            """
            operations = [-5]
            self.assertEqual(mod.below_zero(operations), True)

    def test_balance_reaches_zero_not_below(self):
            """
            Test a scenario where the balance reaches exactly zero but not below.
            This is crucial for distinguishing '< 0' from '<= 0'.
            Covers: Boundary (balance reaches exactly zero), Off-by-one (balance becomes 0), Logic mutation (catches '<' vs '<=').
            """
            operations = [10, -10] # Balance: 0 -> 10 -> 0
            self.assertEqual(mod.below_zero(operations), False)

    def test_operations_with_zeros(self):
            """
            Test a sequence of operations that includes zero-value operations.
            Zero operations should not change the balance.
            Covers: Sign testing (zero operations), Mixed operations.
            """
            operations = [0, 5, -2, 0, -4] # Balance: 0 -> 0 -> 5 -> 3 -> 3 -> -1 (True)
            self.assertEqual(mod.below_zero(operations), True)

    def test_normal_goes_below_third_op(self):
            # Description: Balance goes below zero at the third operation (1+2-4 = -1).
            operations = [1, 2, -4, 5]
            self.assertEqual(mod.below_zero(operations), True)

    def test_normal_remains_positive_or_zero(self):
            # Description: Balance remains positive or zero throughout.
            operations = [10, -5, -3, 2]
            self.assertEqual(mod.below_zero(operations), False)

    def test_edge_empty_operations(self):
            # Description: Empty list of operations, balance remains 0.
            operations = []
            self.assertEqual(mod.below_zero(operations), False)

    def test_edge_single_negative_operation(self):
            # Description: Single negative operation, balance goes below zero immediately.
            operations = [-1]
            self.assertEqual(mod.below_zero(operations), True)

    def test_edge_balance_returns_to_zero(self):
            # Description: Balance returns to zero but never goes below.
            operations = [10, -10]
            self.assertEqual(mod.below_zero(operations), False)

    def test_edge_balance_returns_to_zero_then_below(self):
            # Description: Balance returns to zero then goes below.
            operations = [10, -10, -1]
            self.assertEqual(mod.below_zero(operations), True)

    def test_error_operations_not_list(self):
            # Description: Input 'operations' is not a list.
            operations = "not_a_list"
            with self.assertRaises(TypeError):
                mod.below_zero(operations)

    def test_error_operations_contains_non_int(self):
            # Description: Input 'operations' contains non-integer elements.
            operations = [1, "two", 3]
            with self.assertRaises(TypeError):
                mod.below_zero(operations)

