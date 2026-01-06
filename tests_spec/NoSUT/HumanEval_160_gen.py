import unittest
from sut.problem_HumanEval_160 import do_algebra

class Test_do_algebra(unittest.TestCase):

    def test_normal_mixed_operations_precedence(self):
        # Example from docstring, demonstrating mixed operations and precedence.
        # 2 + 3 * 4 - 5 evaluates as 2 + (3 * 4) - 5 = 2 + 12 - 5 = 14 - 5 = 9.
        operator = ["+", "*", "-"]
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_normal_simple_addition(self):
        # Simple addition with two operands.
        # 10 + 5 = 15.
        operator = ["+"]
        operand = [10, 5]
        self.assertEqual(do_algebra(operator, operand), 15)

    def test_normal_exponentiation_addition(self):
        # Operations involving exponentiation and addition.
        # 2 ** 3 + 4 evaluates as (2 ** 3) + 4 = 8 + 4 = 12.
        operator = ["**", "+"]
        operand = [2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 12)

    def test_edge_minimum_valid_input(self):
        # Minimum valid input: one operator and two operands.
        # 2 ** 3 = 8.
        operator = ["**"]
        operand = [2, 3]
        self.assertEqual(do_algebra(operator, operand), 8)

    def test_edge_all_operands_zero(self):
        # All operands are zero.
        # 0 + 0 * 0 - 0 = 0 + 0 - 0 = 0.
        operator = ["+", "*", "-"]
        operand = [0, 0, 0, 0]
        self.assertEqual(do_algebra(operator, operand), 0)

    def test_edge_large_numbers(self):
        # Large numbers, testing Python's arbitrary precision integers.
        # 2 ** 60 + 1 = 1152921504606846976 + 1 = 1152921504606846977.
        operator = ["**", "+"]
        operand = [2, 60, 1]
        self.assertEqual(do_algebra(operator, operand), 1152921504606846977)

    def test_error_invalid_operator(self):
        # Invalid operator string in the 'operator' list.
        # The '%' operator is not among the allowed basic algebra operations.
        operator = ["+", "%"]
        operand = [1, 2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_error_non_integer_operand(self):
        # Operand list contains a non-integer value.
        # Operands must be integers, 2.5 is a float.
        operator = ["+"]
        operand = [1, 2.5]
        with self.assertRaises(TypeError):
            do_algebra(operator, operand)

    def test_error_negative_operand(self):
        # Operand list contains a negative integer.
        # Operands must be non-negative integers.
        operator = ["+"]
        operand = [1, -2]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_error_operator_operand_length_mismatch(self):
        # Length of 'operator' list does not match 'len(operand) - 1'.
        # len(operator) is 2, len(operand) is 4. Expected len(operator) == 3.
        operator = ["+", "*"]
        operand = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_error_empty_operator_list(self):
        # Empty 'operator' list (violates minimum length constraint).
        # The 'operator' list must have at least one operator.
        operator = []
        operand = [1, 2]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_error_division_by_zero(self):
        # Division by zero.
        # Attempting to perform floor division by zero.
        operator = ["//"]
        operand = [5, 0]
        with self.assertRaises(ZeroDivisionError):
            do_algebra(operator, operand)