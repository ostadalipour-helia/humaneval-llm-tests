import unittest
from sut.problem_HumanEval_3 import below_zero

class Test_below_zero(unittest.TestCase):
    def test_normal_never_below_zero(self):
        # Description: Balance never goes below zero.
        operations = [1, 2, 3]
        self.assertEqual(below_zero(operations), False)

    def test_normal_goes_below_third_op(self):
        # Description: Balance goes below zero at the third operation (1+2-4 = -1).
        operations = [1, 2, -4, 5]
        self.assertEqual(below_zero(operations), True)

    def test_normal_remains_positive_or_zero(self):
        # Description: Balance remains positive or zero throughout.
        operations = [10, -5, -3, 2]
        self.assertEqual(below_zero(operations), False)

    def test_edge_empty_operations(self):
        # Description: Empty list of operations, balance remains 0.
        operations = []
        self.assertEqual(below_zero(operations), False)

    def test_edge_single_negative_operation(self):
        # Description: Single negative operation, balance goes below zero immediately.
        operations = [-1]
        self.assertEqual(below_zero(operations), True)

    def test_edge_balance_returns_to_zero(self):
        # Description: Balance returns to zero but never goes below.
        operations = [10, -10]
        self.assertEqual(below_zero(operations), False)

    def test_edge_balance_returns_to_zero_then_below(self):
        # Description: Balance returns to zero then goes below.
        operations = [10, -10, -1]
        self.assertEqual(below_zero(operations), True)

    def test_error_operations_not_list(self):
        # Description: Input 'operations' is not a list.
        operations = "not_a_list"
        with self.assertRaises(TypeError):
            below_zero(operations)

    def test_error_operations_contains_non_int(self):
        # Description: Input 'operations' contains non-integer elements.
        operations = [1, "two", 3]
        with self.assertRaises(TypeError):
            below_zero(operations)

    def test_error_operations_contains_float(self):
        # Description: Input 'operations' contains float elements.
        operations = [1.5, 2.0]
        with self.assertRaises(TypeError):
            below_zero(operations)