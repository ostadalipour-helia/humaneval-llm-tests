import unittest
from sut.problem_HumanEval_160 import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_01_simple_addition(self):
        # Test case for a single addition operation
        operators = ['+']
        operands = [2, 3]
        self.assertEqual(do_algebra(operators, operands), 5)

    def test_02_simple_subtraction(self):
        # Test case for a single subtraction operation
        operators = ['-']
        operands = [10, 4]
        self.assertEqual(do_algebra(operators, operands), 6)

    def test_03_simple_multiplication(self):
        # Test case for a single multiplication operation
        operators = ['*']
        operands = [5, 6]
        self.assertEqual(do_algebra(operators, operands), 30)

    def test_04_simple_floor_division(self):
        # Test case for a single floor division operation
        operators = ['//']
        operands = [15, 4]
        self.assertEqual(do_algebra(operators, operands), 3)

    def test_05_simple_exponentiation(self):
        # Test case for a single exponentiation operation
        operators = ['**']
        operands = [2, 4]
        self.assertEqual(do_algebra(operators, operands), 16)

    def test_06_mixed_operations_docstring_example(self):
        # Test case matching the example provided in the docstring
        operators = ['+', '*', '-']
        operands = [2, 3, 4, 5]
        # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
        self.assertEqual(do_algebra(operators, operands), 9)

    def test_07_longer_expression_with_precedence(self):
        # Test case with a longer expression involving multiple operators and precedence
        operators = ['+', '*', '//', '**', '-']
        operands = [10, 2, 3, 2, 2, 1]
        # 10 + 2 * 3 // 2 ** 2 - 1
        # 10 + 2 * 3 // 4 - 1
        # 10 + 6 // 4 - 1
        # 10 + 1 - 1 = 10
        self.assertEqual(do_algebra(operators, operands), 10)

    def test_08_operations_involving_zero(self):
        # Test case to check behavior with zero operands
        operators = ['*', '+', '//']
        operands = [5, 0, 10, 2]
        # 5 * 0 + 10 // 2
        # 0 + 5 = 5
        self.assertEqual(do_algebra(operators, operands), 5)

    def test_09_exponentiation_with_zero_and_one(self):
        # Test case for exponentiation with 0 and 1
        operators = ['**', '+', '**']
        operands = [5, 0, 1, 10]
        # 5 ** 0 + 1 ** 10
        # 1 + 1 = 2
        self.assertEqual(do_algebra(operators, operands), 2)

    def test_10_complex_chain_of_operations(self):
        # Test case with a complex chain of operations, including subtractions
        operators = ['-', '*', '+', '-']
        operands = [100, 10, 5, 20, 3]
        # 100 - 10 * 5 + 20 - 3
        # 100 - 50 + 20 - 3
        # 50 + 20 - 3
        # 70 - 3 = 67
        self.assertEqual(do_algebra(operators, operands), 67)

if __name__ == '__main__':
    unittest.main()