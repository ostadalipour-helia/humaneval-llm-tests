import unittest
import sut.problem_HumanEval_55 as mod

class TestHybrid(unittest.TestCase):
    def test_fib_zero(self):
            # Edge case: n=0, often defined as 0
            self.assertEqual(mod.fib(0), 0)

    def test_fib_one(self):
            # Boundary case: n=1, first Fibonacci number, as per docstring
            self.assertEqual(mod.fib(1), 1)

    def test_fib_two(self):
            # Off-by-one from n=1, small value, covers the first step of iteration/recursion
            self.assertEqual(mod.fib(2), 1)

    def test_fib_three(self):
            # Typical input, small value
            self.assertEqual(mod.fib(3), 2)

    def test_fib_five(self):
            # Typical input, intermediate value
            self.assertEqual(mod.fib(5), 5)

    def test_fib_eight(self):
            # Docstring example, typical input
            self.assertEqual(mod.fib(8), 21)

    def test_fib_nine(self):
            # Boundary test: one less than a docstring example (n=10)
            self.assertEqual(mod.fib(9), 34)

    def test_fib_ten(self):
            # Docstring example, boundary test
            self.assertEqual(mod.fib(10), 55)

    def test_fib_eleven(self):
            # Boundary test: one more than a docstring example (n=10)
            self.assertEqual(mod.fib(11), 89)

    def test_fib_large_number(self):
            # Extreme input: a larger number to test efficiency and correctness for higher values
            self.assertEqual(mod.fib(15), 610)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_n_10(self):
            # Normal case: n = 10
            self.assertEqual(mod.fib(10), 55)

    def test_normal_n_8(self):
            # Normal case: n = 8
            self.assertEqual(mod.fib(8), 21)

    def test_normal_n_5(self):
            # Normal case: n = 5
            self.assertEqual(mod.fib(5), 5)

    def test_edge_n_1_smallest_valid(self):
            # Edge case: Smallest valid input n = 1
            self.assertEqual(mod.fib(1), 1)

    def test_edge_n_2_second_smallest(self):
            # Edge case: Second smallest valid input n = 2
            self.assertEqual(mod.fib(2), 1)

    def test_edge_n_3_third_smallest(self):
            # Edge case: Third smallest valid input n = 3
            self.assertEqual(mod.fib(3), 2)

    def test_error_n_string(self):
            # Error case: n is a string (violates n must be an integer)
            with self.assertRaises(TypeError):
                mod.fib("abc")

