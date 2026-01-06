import unittest
import sut.problem_HumanEval_46 as mod

class TestHybrid(unittest.TestCase):
    def test_fib4_0_boundary(self):
            """
            Test the base case for n=0.
            Covers: Boundary, Edge Case, Return Value.
            """
            self.assertEqual(mod.fib4(0), 0)

    def test_fib4_1_boundary(self):
            """
            Test the base case for n=1.
            Covers: Boundary, Edge Case, Return Value.
            """
            self.assertEqual(mod.fib4(1), 0)

    def test_fib4_2_boundary(self):
            """
            Test the base case for n=2.
            Covers: Boundary, Edge Case, Return Value.
            """
            self.assertEqual(mod.fib4(2), 2)

    def test_fib4_3_boundary(self):
            """
            Test the base case for n=3. This is the last explicit base case.
            Covers: Boundary, Edge Case, Off-by-One (just before recurrence starts), Return Value.
            """
            self.assertEqual(mod.fib4(3), 0)

    def test_fib4_4_first_recurrence(self):
            """
            Test the first value calculated using the recurrence relation (n=4).
            Crucial for catching off-by-one errors in loop/array indexing and logic mutations in summation.
            Covers: Boundary, Off-by-One, Logic Mutation, Return Value.
            mod.fib4(4) = mod.fib4(3) + mod.fib4(2) + mod.fib4(1) + mod.fib4(0) = 0 + 2 + 0 + 0 = 2
            """
            self.assertEqual(mod.fib4(4), 2)

    def test_fib4_5_docstring_example(self):
            """
            Test with n=5, a value provided in the docstring example.
            Covers: Typical Input, Return Value.
            """
            self.assertEqual(mod.fib4(5), 4)

    def test_fib4_6_docstring_example(self):
            """
            Test with n=6, a value provided in the docstring example.
            Covers: Typical Input, Return Value.
            """
            self.assertEqual(mod.fib4(6), 8)

    def test_fib4_7_docstring_example(self):
            """
            Test with n=7, a value provided in the docstring example.
            Covers: Typical Input, Return Value.
            """
            self.assertEqual(mod.fib4(7), 14)

    def test_fib4_large_value_10(self):
            """
            Test with a moderately large value (n=10) to ensure correct computation over several steps.
            Covers: Extreme/Unusual Input, Return Value.
            mod.fib4(10) = mod.fib4(9) + mod.fib4(8) + mod.fib4(7) + mod.fib4(6) = 54 + 28 + 14 + 8 = 104
            """
            self.assertEqual(mod.fib4(10), 104)

    def test_fib4_large_value_15(self):
            """
            Test with a larger value (n=15) to stress the computation and verify efficiency.
            Covers: Extreme/Unusual Input, Return Value.
            mod.fib4(15) = mod.fib4(14) + mod.fib4(13) + mod.fib4(12) + mod.fib4(11) = 1434 + 744 + 386 + 200 = 2764
            """
            self.assertEqual(mod.fib4(15), 2764)
    
    if __name__ == '__main__':
        unittest.main()

    def test_fib4_n0_edge(self):
            """Test case for n = 0, an edge case."""
            self.assertEqual(mod.fib4(0), 0)

    def test_fib4_n1_edge(self):
            """Test case for n = 1, an edge case."""
            self.assertEqual(mod.fib4(1), 0)

    def test_fib4_n2_edge(self):
            """Test case for n = 2, an edge case."""
            self.assertEqual(mod.fib4(2), 2)

    def test_fib4_n3_edge(self):
            """Test case for n = 3, an edge case."""
            self.assertEqual(mod.fib4(3), 0)

    def test_fib4_n4_normal(self):
            """Test case for n = 4, a normal case."""
            self.assertEqual(mod.fib4(4), 2)

    def test_fib4_n5_normal(self):
            """Test case for n = 5, a normal case."""
            self.assertEqual(mod.fib4(5), 4)

    def test_fib4_n6_normal(self):
            """Test case for n = 6, a normal case."""
            self.assertEqual(mod.fib4(6), 8)

    def test_fib4_n7_normal(self):
            """Test case for n = 7, a normal case."""
            self.assertEqual(mod.fib4(7), 14)

    def test_fib4_non_integer_input(self):
            """Test case for non-integer input, expecting TypeError."""
            with self.assertRaises(TypeError):
                mod.fib4(3.5)
            with self.assertRaises(TypeError):
                mod.fib4("abc")
            with self.assertRaises(TypeError):
                mod.fib4([1])

