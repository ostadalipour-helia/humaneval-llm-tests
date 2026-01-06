import unittest
import sut.problem_HumanEval_63 as mod

class TestHybrid(unittest.TestCase):
    def test_fibfib_0_base_case(self):
            """
            Test the base case for n=0.
            Covers: Boundary, Edge Case, Return Value.
            """
            self.assertEqual(mod.fibfib(0), 0)

    def test_fibfib_1_base_case(self):
            """
            Test the base case for n=1.
            Covers: Boundary, Edge Case, Return Value, Off-by-one from n=0.
            """
            self.assertEqual(mod.fibfib(1), 0)

    def test_fibfib_2_base_case(self):
            """
            Test the base case for n=2.
            Covers: Boundary, Return Value, Off-by-one from n=1.
            """
            self.assertEqual(mod.fibfib(2), 1)

    def test_fibfib_3_first_recursive_step(self):
            """
            Test the first value computed using the recursive definition.
            Covers: Boundary (first recursive), Off-by-one from n=2, Logic Mutation (ensures recursion starts correctly).
            mod.fibfib(3) = mod.fibfib(2) + mod.fibfib(1) + mod.fibfib(0) = 1 + 0 + 0 = 1
            """
            self.assertEqual(mod.fibfib(3), 1)

    def test_fibfib_4_typical_input(self):
            """
            Test a typical input value.
            Covers: Typical Input, Off-by-one from n=3.
            mod.fibfib(4) = mod.fibfib(3) + mod.fibfib(2) + mod.fibfib(1) = 1 + 1 + 0 = 2
            """
            self.assertEqual(mod.fibfib(4), 2)

    def test_fibfib_5_docstring_example(self):
            """
            Test an input value provided in the docstring example.
            Covers: Typical Input, Return Value.
            mod.fibfib(5) = mod.fibfib(4) + mod.fibfib(3) + mod.fibfib(2) = 2 + 1 + 1 = 4
            """
            self.assertEqual(mod.fibfib(5), 4)

    def test_fibfib_6_another_typical_input(self):
            """
            Test another typical input value.
            Covers: Typical Input.
            mod.fibfib(6) = mod.fibfib(5) + mod.fibfib(4) + mod.fibfib(3) = 4 + 2 + 1 = 7
            """
            self.assertEqual(mod.fibfib(6), 7)

    def test_fibfib_8_docstring_example(self):
            """
            Test another input value provided in the docstring example.
            Covers: Typical Input, Return Value.
            mod.fibfib(8) = mod.fibfib(7) + mod.fibfib(6) + mod.fibfib(5) = 13 + 7 + 4 = 24
            """
            self.assertEqual(mod.fibfib(8), 24)

    def test_fibfib_large_input_10(self):
            """
            Test a larger input value to check efficiency and correctness for deeper recursion.
            Covers: Extreme/Unusual Input.
            mod.fibfib(10) = mod.fibfib(9) + mod.fibfib(8) + mod.fibfib(7) = 44 + 24 + 13 = 81
            """
            self.assertEqual(mod.fibfib(10), 81)

    def test_fibfib_larger_input_12(self):
            """
            Test an even larger input value.
            Covers: Extreme/Unusual Input.
            mod.fibfib(12) = mod.fibfib(11) + mod.fibfib(10) + mod.fibfib(9) = 149 + 81 + 44 = 274
            """
            self.assertEqual(mod.fibfib(12), 274)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_n5(self):
            """
            Test case for n = 5, expected output 4.
            Description: Typical case for n > 2
            """
            self.assertEqual(mod.fibfib(5), 4)

    def test_normal_n8(self):
            """
            Test case for n = 8, expected output 24.
            Description: Another typical case for n > 2
            """
            self.assertEqual(mod.fibfib(8), 24)

    def test_normal_n3(self):
            """
            Test case for n = 3, expected output 1.
            Description: First recursive step: mod.fibfib(3) = mod.fibfib(2) + mod.fibfib(1) + mod.fibfib(0) = 1 + 0 + 0 = 1
            """
            self.assertEqual(mod.fibfib(3), 1)

    def test_normal_n4(self):
            """
            Test case for n = 4, expected output 2.
            Description: Second recursive step: mod.fibfib(4) = mod.fibfib(3) + mod.fibfib(2) + mod.fibfib(1) = 1 + 1 + 0 = 2
            """
            self.assertEqual(mod.fibfib(4), 2)

    def test_edge_n0(self):
            """
            Test case for n = 0, expected output 0.
            Description: Base case: n = 0
            """
            self.assertEqual(mod.fibfib(0), 0)

    def test_edge_n1(self):
            """
            Test case for n = 1, expected output 0.
            Description: Base case: n = 1
            """
            self.assertEqual(mod.fibfib(1), 0)

    def test_edge_n2(self):
            """
            Test case for n = 2, expected output 1.
            Description: Base case: n = 2
            """
            self.assertEqual(mod.fibfib(2), 1)

    def test_error_non_integer_string(self):
            """
            Test case for n = "abc", expecting a TypeError.
            Description: Input n is not an integer.
            """
            with self.assertRaises(TypeError):
                mod.fibfib("abc")

