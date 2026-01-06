import unittest
import sut.problem_HumanEval_106 as mod

class TestHybrid(unittest.TestCase):
    def test_n_zero(self):
            # Edge case: n=0, should return an empty list.
            # Boundary: Smallest possible n.
            self.assertEqual(mod.f(0), [])

    def test_n_one(self):
            # Edge case: n=1, single element list.
            # Boundary: First element (i=1) is odd, so sum(1 to 1) = 1.
            self.assertEqual(mod.f(1), [1])

    def test_n_two(self):
            # Boundary: n=2, covers first even i (i=2).
            # i=1 (odd): sum(1 to 1) = 1
            # i=2 (even): factorial(2) = 2
            self.assertEqual(mod.f(2), [1, 2])

    def test_n_three(self):
            # Typical input: n=3, covers odd, even, odd sequence.
            # i=1 (odd): sum(1 to 1) = 1
            # i=2 (even): factorial(2) = 2
            # i=3 (odd): sum(1 to 3) = 6
            self.assertEqual(mod.f(3), [1, 2, 6])

    def test_n_four(self):
            # Boundary: n=4, covers up to i=4 (even).
            # i=1 (odd): sum(1 to 1) = 1
            # i=2 (even): factorial(2) = 2
            # i=3 (odd): sum(1 to 3) = 6
            # i=4 (even): factorial(4) = 24
            self.assertEqual(mod.f(4), [1, 2, 6, 24])

    def test_n_five_docstring_example(self):
            # Typical input: n=5, example from docstring.
            # i=1 (odd): sum(1 to 1) = 1
            # i=2 (even): factorial(2) = 2
            # i=3 (odd): sum(1 to 3) = 6
            # i=4 (even): factorial(4) = 24
            # i=5 (odd): sum(1 to 5) = 15
            self.assertEqual(mod.f(5), [1, 2, 6, 24, 15])

    def test_n_six_extreme_even_end(self):
            # Extreme/Unusual input: n=6, larger input, ends with even i.
            # i=6 (even): factorial(6) = 720
            self.assertEqual(mod.f(6), [1, 2, 6, 24, 15, 720])

    def test_n_seven_extreme_odd_end(self):
            # Extreme/Unusual input: n=7, larger input, ends with odd i.
            # i=7 (odd): sum(1 to 7) = 28
            self.assertEqual(mod.f(7), [1, 2, 6, 24, 15, 720, 28])

    def test_n_eight_large_factorial(self):
            # Extreme/Unusual input: n=8, tests larger factorial value.
            # i=8 (even): factorial(8) = 40320
            self.assertEqual(mod.f(8), [1, 2, 6, 24, 15, 720, 28, 40320])

    def test_n_nine_large_sum(self):
            # Extreme/Unusual input: n=9, tests larger sum value.
            # i=9 (odd): sum(1 to 9) = 45
            self.assertEqual(mod.f(9), [1, 2, 6, 24, 15, 720, 28, 40320, 45])

    def test_normal_n5(self):
            self.assertEqual(mod.f(5), [1, 2, 6, 24, 15])

    def test_normal_n1(self):
            self.assertEqual(mod.f(1), [1])

    def test_normal_n2(self):
            self.assertEqual(mod.f(2), [1, 2])

    def test_normal_n4(self):
            self.assertEqual(mod.f(4), [1, 2, 6, 24])

    def test_edge_n0(self):
            self.assertEqual(mod.f(0), [])

    def test_error_float_n(self):
            with self.assertRaises(TypeError):
                mod.f(3.5)

    def test_error_string_n(self):
            with self.assertRaises(TypeError):
                mod.f("abc")

