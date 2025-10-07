import unittest
from sut_llm.problem_HumanEval_55 import fib

class TestFib(unittest.TestCase):
    def test_fib_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_one_from_docstring(self):
        self.assertEqual(fib(1), 1)

    def test_fib_two(self):
        self.assertEqual(fib(2), 1)

    def test_fib_three(self):
        self.assertEqual(fib(3), 2)

    def test_fib_four(self):
        self.assertEqual(fib(4), 3)

    def test_fib_five(self):
        self.assertEqual(fib(5), 5)

    def test_fib_six(self):
        self.assertEqual(fib(6), 8)

    def test_fib_eight_from_docstring(self):
        self.assertEqual(fib(8), 21)

    def test_fib_ten_from_docstring(self):
        self.assertEqual(fib(10), 55)

    def test_fib_twelve(self):
        self.assertEqual(fib(12), 144)

if __name__ == '__main__':
    unittest.main()