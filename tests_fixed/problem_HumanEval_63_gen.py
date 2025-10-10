import unittest
from sut_llm.problem_HumanEval_63 import fibfib

class TestFibFib(unittest.TestCase):

    def test_fibfib_0_base_case(self):
        """
        Test the base case for n=0.
        Covers: Boundary, Edge Case, Return Value.
        """
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_1_base_case(self):
        """
        Test the base case for n=1.
        Covers: Boundary, Edge Case, Return Value, Off-by-one from n=0.
        """
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_2_base_case(self):
        """
        Test the base case for n=2.
        Covers: Boundary, Return Value, Off-by-one from n=1.
        """
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_3_first_recursive_step(self):
        """
        Test the first value computed using the recursive definition.
        Covers: Boundary (first recursive), Off-by-one from n=2, Logic Mutation (ensures recursion starts correctly).
        fibfib(3) = fibfib(2) + fibfib(1) + fibfib(0) = 1 + 0 + 0 = 1
        """
        self.assertEqual(fibfib(3), 1)

    def test_fibfib_4_typical_input(self):
        """
        Test a typical input value.
        Covers: Typical Input, Off-by-one from n=3.
        fibfib(4) = fibfib(3) + fibfib(2) + fibfib(1) = 1 + 1 + 0 = 2
        """
        self.assertEqual(fibfib(4), 2)

    def test_fibfib_5_docstring_example(self):
        """
        Test an input value provided in the docstring example.
        Covers: Typical Input, Return Value.
        fibfib(5) = fibfib(4) + fibfib(3) + fibfib(2) = 2 + 1 + 1 = 4
        """
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_6_another_typical_input(self):
        """
        Test another typical input value.
        Covers: Typical Input.
        fibfib(6) = fibfib(5) + fibfib(4) + fibfib(3) = 4 + 2 + 1 = 7
        """
        self.assertEqual(fibfib(6), 7)

    def test_fibfib_8_docstring_example(self):
        """
        Test another input value provided in the docstring example.
        Covers: Typical Input, Return Value.
        fibfib(8) = fibfib(7) + fibfib(6) + fibfib(5) = 13 + 7 + 4 = 24
        """
        self.assertEqual(fibfib(8), 24)

    def test_fibfib_large_input_10(self):
        """
        Test a larger input value to check efficiency and correctness for deeper recursion.
        Covers: Extreme/Unusual Input.
        fibfib(10) = fibfib(9) + fibfib(8) + fibfib(7) = 44 + 24 + 13 = 81
        """
        self.assertEqual(fibfib(10), 81)

    def test_fibfib_larger_input_12(self):
        """
        Test an even larger input value.
        Covers: Extreme/Unusual Input.
        fibfib(12) = fibfib(11) + fibfib(10) + fibfib(9) = 149 + 81 + 44 = 274
        """
        self.assertEqual(fibfib(12), 274)

if __name__ == '__main__':
    unittest.main()