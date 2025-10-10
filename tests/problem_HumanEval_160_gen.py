import unittest
from sut.problem_HumanEval_160 import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_example_case(self):
        # Verifies the exact example from the docstring. (Typical/Expected)
        # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 14 - 5 = 9
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_smallest_valid_addition(self):
        # Smallest valid input, basic addition. (Boundary, Edge)
        # 1 + 2 = 3
        operator = ['+']
        operand = [1, 2]
        self.assertEqual(do_algebra(operator, operand), 3)

    def test_smallest_valid_multiplication(self):
        # Smallest valid input, basic multiplication. (Boundary, Edge)
        # 5 * 6 = 30
        operator = ['*']
        operand = [5, 6]
        self.assertEqual(do_algebra(operator, operand), 30)

    def test_mixed_operations_precedence(self):
        # Tests mixed operations with different precedence. (Typical/Expected, Logic Mutation)
        # 10 * 2 + 5 // 2 = 20 + 2 = 22
        operator = ['*', '+', '//']
        operand = [10, 2, 5, 2]
        self.assertEqual(do_algebra(operator, operand), 22)

    def test_exponentiation_and_addition(self):
        # Tests exponentiation with other operations, large numbers. (Extreme/Unusual, Boundary for **)
        # 2**10 + 100 = 1024 + 100 = 1124
        operator = ['**', '+']
        operand = [2, 10, 100]
        self.assertEqual(do_algebra(operator, operand), 1124)

    def test_all_same_operands(self):
        # Tests with all operands being the same value. (Edge, Logic Mutation)
        # 5 + 5 * 5 - 5 = 5 + 25 - 5 = 30 - 5 = 25
        operator = ['+', '*', '-']
        operand = [5, 5, 5, 5]
        self.assertEqual(do_algebra(operator, operand), 25)

    def test_only_one_operator_type_repeated(self):
        # Tests a sequence of the same operator. (Extreme/Unusual, Off-by-one for loop)
        # 1 + 2 + 3 + 4 = 10
        operator = ['+', '+', '+']
        operand = [1, 2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 10)

    def test_floor_division_with_remainder(self):
        # Tests floor division specifically to catch // vs / mutations. (Boundary, Logic Mutation)
        # 10 // 3 + 1 = 3 + 1 = 4
        operator = ['//', '+']
        operand = [10, 3, 1]
        self.assertEqual(do_algebra(operator, operand), 4)

    def test_operands_with_zero_and_one(self):
        # Tests with 0 and 1 as operands, ensuring they are handled correctly. (Sign/Zero, Boundary)
        # 0 * 5 + 1 ** 2 = 0 + 1 = 1
        operator = ['*', '+', '**']
        operand = [0, 5, 1, 2]
        self.assertEqual(do_algebra(operator, operand), 1)

    def test_subtraction_with_negative_intermediate_result(self):
        # Tests subtraction that could lead to negative intermediate results, ensuring correct arithmetic. (Boundary, Sign/Zero)
        # 10 - 2 * 3 + 1 = 10 - 6 + 1 = 4 + 1 = 5
        operator = ['-', '*', '+']
        operand = [10, 2, 3, 1]
        self.assertEqual(do_algebra(operator, operand), 5)