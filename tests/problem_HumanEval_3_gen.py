import unittest
from sut.problem_HumanEval_3 import below_zero

class TestBelowZero(unittest.TestCase):

    def test_empty_operations(self):
        """
        Test with an empty list of operations.
        Balance should remain 0, so it should return False.
        Covers: Edge case (empty list), Return Value (False).
        """
        operations = []
        self.assertEqual(below_zero(operations), False)

    def test_only_deposits(self):
        """
        Test with only positive deposit operations.
        Balance should always be positive, so it should return False.
        Covers: Typical input, Sign testing (only positive), Return Value (False).
        """
        operations = [10, 20, 5, 100]
        self.assertEqual(below_zero(operations), False)

    def test_immediate_withdrawal(self):
        """
        Test with a single negative operation that immediately makes balance below zero.
        Covers: Edge case (single negative element), Boundary (first operation), Return Value (True).
        """
        operations = [-5]
        self.assertEqual(below_zero(operations), True)

    def test_balance_just_below_zero(self):
        """
        Test a scenario where the balance goes from positive to exactly -1.
        This tests the '< 0' condition and off-by-one errors.
        Covers: Boundary (balance goes from positive to negative), Off-by-one (balance becomes -1), Logic mutation (catches '<' vs '<=').
        """
        operations = [10, -11] # Balance: 0 -> 10 -> -1
        self.assertEqual(below_zero(operations), True)

    def test_balance_reaches_zero_not_below(self):
        """
        Test a scenario where the balance reaches exactly zero but not below.
        This is crucial for distinguishing '< 0' from '<= 0'.
        Covers: Boundary (balance reaches exactly zero), Off-by-one (balance becomes 0), Logic mutation (catches '<' vs '<=').
        """
        operations = [10, -10] # Balance: 0 -> 10 -> 0
        self.assertEqual(below_zero(operations), False)

    def test_multiple_fluctuations_below_zero(self):
        """
        Test a sequence of operations where the balance fluctuates and eventually falls below zero.
        Covers: Typical input, Multiple fluctuations, Return Value (True).
        """
        operations = [5, -2, 3, -10, 1] # Balance: 0 -> 5 -> 3 -> 6 -> -4 (True)
        self.assertEqual(below_zero(operations), True)

    def test_multiple_fluctuations_never_below_zero(self):
        """
        Test a sequence of operations where the balance fluctuates but never falls below zero.
        Covers: Typical input, Multiple fluctuations, Return Value (False).
        """
        operations = [5, -2, 3, -4, 1] # Balance: 0 -> 5 -> 3 -> 6 -> 2 -> 3
        self.assertEqual(below_zero(operations), False)

    def test_large_numbers_below_zero(self):
        """
        Test with very large numbers where the balance eventually falls below zero.
        Covers: Extreme/Unusual inputs, Sign testing (large negative).
        """
        operations = [1000000000, -2000000000] # Balance: 0 -> 1B -> -1B
        self.assertEqual(below_zero(operations), True)

    def test_large_numbers_not_below_zero(self):
        """
        Test with very large numbers where the balance remains positive.
        Covers: Extreme/Unusual inputs, Sign testing (large positive).
        """
        operations = [2000000000, -1000000000] # Balance: 0 -> 2B -> 1B
        self.assertEqual(below_zero(operations), False)

    def test_operations_with_zeros(self):
        """
        Test a sequence of operations that includes zero-value operations.
        Zero operations should not change the balance.
        Covers: Sign testing (zero operations), Mixed operations.
        """
        operations = [0, 5, -2, 0, -4] # Balance: 0 -> 0 -> 5 -> 3 -> 3 -> -1 (True)
        self.assertEqual(below_zero(operations), True)