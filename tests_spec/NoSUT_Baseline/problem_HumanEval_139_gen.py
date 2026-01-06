import unittest
import sut.problem_HumanEval_139 as mod

class TestHybrid(unittest.TestCase):
    def test_n1_smallest_valid_input(self):
            self.assertEqual(mod.special_factorial(1), 1)
    
        # Test 2: Second smallest valid input (off-by-one from n=1, edge case: n=2)
        # mod.special_factorial(2) = 2! * 1! = 2 * 1 = 2

    def test_n2_second_smallest_input(self):
            self.assertEqual(mod.special_factorial(2), 2)
    
        # Test 3: Typical input (n=3), verifying the product logic for a few terms
        # mod.special_factorial(3) = 3! * 2! * 1! = 6 * 2 * 1 = 12

    def test_n3_typical_input(self):
            self.assertEqual(mod.special_factorial(3), 12)
    
        # Test 4: Example from docstring (n=4), critical for verifying problem understanding
        # mod.special_factorial(4) = 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288

    def test_n4_docstring_example(self):
            self.assertEqual(mod.special_factorial(4), 288)
    
        # Test 5: Larger input (n=5), checking for correctness with more iterations
        # mod.special_factorial(5) = 5! * 4! * 3! * 2! * 1! = 120 * 288 = 34560

    def test_n5_larger_input(self):
            self.assertEqual(mod.special_factorial(5), 34560)
    
        # Test 6: Extreme input (n=6), pushing the calculation to larger numbers
        # mod.special_factorial(6) = 6! * 5! * 4! * 3! * 2! * 1! = 720 * 34560 = 24883200

    def test_n6_extreme_input(self):
            self.assertEqual(mod.special_factorial(6), 24883200)
    
        # Test 7: Re-verify boundary condition (n=1) to ensure robustness against mutations

    def test_n1_boundary_reverification(self):
            self.assertEqual(mod.special_factorial(1), 1)
    
        # Test 8: Off-by-one check (n=3), ensuring the loop/product logic handles transitions correctly

    def test_n3_off_by_one_logic_check(self):
            self.assertEqual(mod.special_factorial(3), 12)
    
        # Test 9: Another typical input (n=4) to confirm consistency and exact output

    def test_n4_another_typical_input_check(self):
            self.assertEqual(mod.special_factorial(4), 288)
    
        # Test 10: Very large input (n=7) to test scalability and potential overflow issues (Python handles large ints)
        # mod.special_factorial(7) = 7! * 6! * 5! * 4! * 3! * 2! * 1! = 5040 * 24883200 = 125411328000

    def test_n7_very_large_input(self):
            self.assertEqual(mod.special_factorial(7), 125411328000)

    def test_normal_case_four(self):
            # n = 4, output = 288 (4! * 3! * 2! * 1! = 24 * 6 * 2 * 1)
            self.assertEqual(mod.special_factorial(4), 288)

    def test_normal_case_three(self):
            # n = 3, output = 12 (3! * 2! * 1! = 6 * 2 * 1)
            self.assertEqual(mod.special_factorial(3), 12)

    def test_edge_case_one(self):
            # n = 1, output = 1 (1! = 1)
            self.assertEqual(mod.special_factorial(1), 1)

    def test_error_case_float(self):
            # n = 3.5, n must be an integer
            with self.assertRaises(TypeError):
                mod.special_factorial(3.5)

    def test_error_case_string(self):
            # n = 'abc', n must be an integer
            with self.assertRaises(TypeError):
                mod.special_factorial('abc')

