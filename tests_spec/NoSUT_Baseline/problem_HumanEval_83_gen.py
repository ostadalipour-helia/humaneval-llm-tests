import unittest
import sut.problem_HumanEval_83 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_one_boundary(self):
            # Test case for the smallest positive integer n (boundary condition, edge case)
            # For n=1, the only 1-digit number that starts or ends with 1 is '1'.
            self.assertEqual(mod.starts_one_ends(1), 1)

    def test_n_is_two_boundary(self):
            # Test case for n=2 (boundary condition, transition point for formula)
            # 2-digit numbers: 10-99
            # Starts with 1: 10, 11, ..., 19 (10 numbers)
            # Ends with 1: 11, 21, ..., 91 (9 numbers)
            # Starts AND ends with 1: 11 (1 number)
            # Total = 10 + 9 - 1 = 18
            self.assertEqual(mod.starts_one_ends(2), 18)

    def test_n_is_three_typical(self):
            # Test case for n=3 (typical input, checks general formula)
            # 3-digit numbers: 100-999
            # Starts with 1: 100-199 (100 numbers)
            # Ends with 1: 101, 111, ..., 991 (9 * 10 = 90 numbers)
            # Starts AND ends with 1: 101, 111, ..., 191 (10 numbers)
            # Total = 100 + 90 - 10 = 180
            self.assertEqual(mod.starts_one_ends(3), 180)

    def test_n_is_four_typical(self):
            # Test case for n=4 (typical input, verifies formula consistency)
            # Expected: 18 * 10^(4-2) = 18 * 10^2 = 1800
            self.assertEqual(mod.starts_one_ends(4), 1800)

    def test_n_is_five_larger_input(self):
            # Test case for a slightly larger input (checks scalability)
            # Expected: 18 * 10^(5-2) = 18 * 10^3 = 18000
            self.assertEqual(mod.starts_one_ends(5), 18000)

    def test_n_is_ten_extreme_input(self):
            # Test case for a large input (extreme value, checks for potential overflow or performance issues)
            # Expected: 18 * 10^(10-2) = 18 * 10^8 = 1,800,000,000
            self.assertEqual(mod.starts_one_ends(10), 1800000000)

    def test_n_is_two_logic_mutation_check(self):
            # This test specifically targets potential logic mutations like 'and' vs 'or' or missing inclusion-exclusion.
            # For n=2, if the logic was just 'starts with 1' + 'ends with 1' (missing subtraction), it would be 10+9=19.
            # If it was 'starts AND ends with 1', it would be 1.
            # The correct answer is 18.
            self.assertEqual(mod.starts_one_ends(2), 18)

    def test_n_is_three_logic_mutation_check(self):
            # Similar to the previous test, but with larger numbers to ensure the inclusion-exclusion principle is correctly applied.
            # For n=3, if the logic was just 'starts with 1' + 'ends with 1', it would be 100+90=190.
            # If it was 'starts AND ends with 1', it would be 10.
            # The correct answer is 180.
            self.assertEqual(mod.starts_one_ends(3), 180)

    def test_n_is_six_another_typical(self):
            # Another typical input to ensure consistency across different values of n.
            # Expected: 18 * 10^(6-2) = 18 * 10^4 = 180000
            self.assertEqual(mod.starts_one_ends(6), 180000)

    def test_edge_n_1(self):
            # Edge case: n = 1
            # Expected output: 1 (Only '1' is a 1-digit number that starts or ends with 1)
            self.assertEqual(mod.starts_one_ends(1), 1)

    def test_normal_n_2(self):
            # Normal case: n = 2
            # Expected output: 18 (18 * 10^(2-2) = 18 * 10^0 = 18)
            self.assertEqual(mod.starts_one_ends(2), 18)

    def test_normal_n_3(self):
            # Normal case: n = 3
            # Expected output: 180 (18 * 10^(3-2) = 18 * 10^1 = 180)
            self.assertEqual(mod.starts_one_ends(3), 180)

    def test_normal_n_4(self):
            # Normal case: n = 4
            # Expected output: 1800 (18 * 10^(4-2) = 18 * 10^2 = 1800)
            self.assertEqual(mod.starts_one_ends(4), 1800)

    def test_normal_n_5(self):
            # Normal case: n = 5
            # Expected output: 18000 (18 * 10^(5-2) = 18 * 10^3 = 18000)
            self.assertEqual(mod.starts_one_ends(5), 18000)

    def test_error_n_string(self):
            # Error case: n = "abc" (n must be an integer)
            with self.assertRaises(TypeError):
                mod.starts_one_ends("abc")

    def test_error_n_none(self):
            # Error case: n = None (n must be an integer)
            with self.assertRaises(TypeError):
                mod.starts_one_ends(None)

