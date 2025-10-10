import unittest
from sut_llm.problem_HumanEval_55 import fib

class TestFibonacci(unittest.TestCase):

    def test_fib_zero(self):
        # Edge case: n=0, often defined as 0
        self.assertEqual(fib(0), 0)

    def test_fib_one(self):
        # Boundary case: n=1, first Fibonacci number, as per docstring
        self.assertEqual(fib(1), 1)

    def test_fib_two(self):
        # Off-by-one from n=1, small value, covers the first step of iteration/recursion
        self.assertEqual(fib(2), 1)

    def test_fib_three(self):
        # Typical input, small value
        self.assertEqual(fib(3), 2)

    def test_fib_five(self):
        # Typical input, intermediate value
        self.assertEqual(fib(5), 5)

    def test_fib_eight(self):
        # Docstring example, typical input
        self.assertEqual(fib(8), 21)

    def test_fib_nine(self):
        # Boundary test: one less than a docstring example (n=10)
        self.assertEqual(fib(9), 34)

    def test_fib_ten(self):
        # Docstring example, boundary test
        self.assertEqual(fib(10), 55)

    def test_fib_eleven(self):
        # Boundary test: one more than a docstring example (n=10)
        self.assertEqual(fib(11), 89)

    def test_fib_large_number(self):
        # Extreme input: a larger number to test efficiency and correctness for higher values
        self.assertEqual(fib(15), 610)

    def test_fib_negative_input_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            fib(-1)
        self.assertEqual(str(cm.exception), "Input must be a non-negative integer.")

if __name__ == '__main__':
    unittest.main()