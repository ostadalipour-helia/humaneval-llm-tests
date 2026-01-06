import unittest
import sut.problem_HumanEval_160 as mod

class TestHybrid(unittest.TestCase):
    def test_example_case(self):
            # Verifies the exact example from the docstring. (Typical/Expected)
            # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 14 - 5 = 9
            operator = ['+', '*', '-']
            operand = [2, 3, 4, 5]
            self.assertEqual(mod.do_algebra(operator, operand), 9)

    def test_smallest_valid_addition(self):
            # Smallest valid input, basic addition. (Boundary, Edge)
            # 1 + 2 = 3
            operator = ['+']
            operand = [1, 2]
            self.assertEqual(mod.do_algebra(operator, operand), 3)

    def test_smallest_valid_multiplication(self):
            # Smallest valid input, basic multiplication. (Boundary, Edge)
            # 5 * 6 = 30
            operator = ['*']
            operand = [5, 6]
            self.assertEqual(mod.do_algebra(operator, operand), 30)

    def test_mixed_operations_precedence(self):
            # Tests mixed operations with different precedence. (Typical/Expected, Logic Mutation)
            # 10 * 2 + 5 // 2 = 20 + 2 = 22
            operator = ['*', '+', '//']
            operand = [10, 2, 5, 2]
            self.assertEqual(mod.do_algebra(operator, operand), 22)

    def test_exponentiation_and_addition(self):
            # Tests exponentiation with other operations, large numbers. (Extreme/Unusual, Boundary for **)
            # 2**10 + 100 = 1024 + 100 = 1124
            operator = ['**', '+']
            operand = [2, 10, 100]
            self.assertEqual(mod.do_algebra(operator, operand), 1124)

    def test_all_same_operands(self):
            # Tests with all operands being the same value. (Edge, Logic Mutation)
            # 5 + 5 * 5 - 5 = 5 + 25 - 5 = 30 - 5 = 25
            operator = ['+', '*', '-']
            operand = [5, 5, 5, 5]
            self.assertEqual(mod.do_algebra(operator, operand), 25)

    def test_only_one_operator_type_repeated(self):
            # Tests a sequence of the same operator. (Extreme/Unusual, Off-by-one for loop)
            # 1 + 2 + 3 + 4 = 10
            operator = ['+', '+', '+']
            operand = [1, 2, 3, 4]
            self.assertEqual(mod.do_algebra(operator, operand), 10)

    def test_floor_division_with_remainder(self):
            # Tests floor division specifically to catch // vs / mutations. (Boundary, Logic Mutation)
            # 10 // 3 + 1 = 3 + 1 = 4
            operator = ['//', '+']
            operand = [10, 3, 1]
            self.assertEqual(mod.do_algebra(operator, operand), 4)

    def test_operands_with_zero_and_one(self):
            # Tests with 0 and 1 as operands, ensuring they are handled correctly. (Sign/Zero, Boundary)
            # 0 * 5 + 1 ** 2 = 0 + 1 = 1
            operator = ['*', '+', '**']
            operand = [0, 5, 1, 2]
            self.assertEqual(mod.do_algebra(operator, operand), 1)

    def test_subtraction_with_negative_intermediate_result(self):
            # Tests subtraction that could lead to negative intermediate results, ensuring correct arithmetic. (Boundary, Sign/Zero)
            # 10 - 2 * 3 + 1 = 10 - 6 + 1 = 4 + 1 = 5
            operator = ['-', '*', '+']
            operand = [10, 2, 3, 1]
            self.assertEqual(mod.do_algebra(operator, operand), 5)

    def test_normal_mixed_operations_precedence(self):
            # Example from docstring, demonstrating mixed operations and precedence.
            # 2 + 3 * 4 - 5 evaluates as 2 + (3 * 4) - 5 = 2 + 12 - 5 = 14 - 5 = 9.
            operator = ["+", "*", "-"]
            operand = [2, 3, 4, 5]
            self.assertEqual(mod.do_algebra(operator, operand), 9)

    def test_normal_simple_addition(self):
            # Simple addition with two operands.
            # 10 + 5 = 15.
            operator = ["+"]
            operand = [10, 5]
            self.assertEqual(mod.do_algebra(operator, operand), 15)

    def test_normal_exponentiation_addition(self):
            # Operations involving exponentiation and addition.
            # 2 ** 3 + 4 evaluates as (2 ** 3) + 4 = 8 + 4 = 12.
            operator = ["**", "+"]
            operand = [2, 3, 4]
            self.assertEqual(mod.do_algebra(operator, operand), 12)

    def test_edge_minimum_valid_input(self):
            # Minimum valid input: one operator and two operands.
            # 2 ** 3 = 8.
            operator = ["**"]
            operand = [2, 3]
            self.assertEqual(mod.do_algebra(operator, operand), 8)

    def test_edge_all_operands_zero(self):
            # All operands are zero.
            # 0 + 0 * 0 - 0 = 0 + 0 - 0 = 0.
            operator = ["+", "*", "-"]
            operand = [0, 0, 0, 0]
            self.assertEqual(mod.do_algebra(operator, operand), 0)

    def test_edge_large_numbers(self):
            # Large numbers, testing Python's arbitrary precision integers.
            # 2 ** 60 + 1 = 1152921504606846976 + 1 = 1152921504606846977.
            operator = ["**", "+"]
            operand = [2, 60, 1]
            self.assertEqual(mod.do_algebra(operator, operand), 1152921504606846977)

    def test_error_division_by_zero(self):
            # Division by zero.
            # Attempting to perform floor division by zero.
            operator = ["//"]
            operand = [5, 0]
            with self.assertRaises(ZeroDivisionError):
                mod.do_algebra(operator, operand)

