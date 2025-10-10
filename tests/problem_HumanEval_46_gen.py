import unittest
from sut.problem_HumanEval_46 import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_0_boundary(self):
        """
        Test the base case for n=0.
        Covers: Boundary, Edge Case, Return Value.
        """
        self.assertEqual(fib4(0), 0)

    def test_fib4_1_boundary(self):
        """
        Test the base case for n=1.
        Covers: Boundary, Edge Case, Return Value.
        """
        self.assertEqual(fib4(1), 0)

    def test_fib4_2_boundary(self):
        """
        Test the base case for n=2.
        Covers: Boundary, Edge Case, Return Value.
        """
        self.assertEqual(fib4(2), 2)

    def test_fib4_3_boundary(self):
        """
        Test the base case for n=3. This is the last explicit base case.
        Covers: Boundary, Edge Case, Off-by-One (just before recurrence starts), Return Value.
        """
        self.assertEqual(fib4(3), 0)

    def test_fib4_4_first_recurrence(self):
        """
        Test the first value calculated using the recurrence relation (n=4).
        Crucial for catching off-by-one errors in loop/array indexing and logic mutations in summation.
        Covers: Boundary, Off-by-One, Logic Mutation, Return Value.
        fib4(4) = fib4(3) + fib4(2) + fib4(1) + fib4(0) = 0 + 2 + 0 + 0 = 2
        """
        self.assertEqual(fib4(4), 2)

    def test_fib4_5_docstring_example(self):
        """
        Test with n=5, a value provided in the docstring example.
        Covers: Typical Input, Return Value.
        """
        self.assertEqual(fib4(5), 4)

    def test_fib4_6_docstring_example(self):
        """
        Test with n=6, a value provided in the docstring example.
        Covers: Typical Input, Return Value.
        """
        self.assertEqual(fib4(6), 8)

    def test_fib4_7_docstring_example(self):
        """
        Test with n=7, a value provided in the docstring example.
        Covers: Typical Input, Return Value.
        """
        self.assertEqual(fib4(7), 14)

    def test_fib4_large_value_10(self):
        """
        Test with a moderately large value (n=10) to ensure correct computation over several steps.
        Covers: Extreme/Unusual Input, Return Value.
        fib4(10) = fib4(9) + fib4(8) + fib4(7) + fib4(6) = 54 + 28 + 14 + 8 = 104
        """
        self.assertEqual(fib4(10), 104)

    def test_fib4_large_value_15(self):
        """
        Test with a larger value (n=15) to stress the computation and verify efficiency.
        Covers: Extreme/Unusual Input, Return Value.
        fib4(15) = fib4(14) + fib4(13) + fib4(12) + fib4(11) = 1434 + 744 + 386 + 200 = 2764
        """
        self.assertEqual(fib4(15), 2764)

if __name__ == '__main__':
    unittest.main()