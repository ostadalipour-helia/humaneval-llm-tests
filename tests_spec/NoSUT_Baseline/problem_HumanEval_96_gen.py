import unittest
import sut.problem_HumanEval_96 as mod

class TestHybrid(unittest.TestCase):
    def test_n_is_zero_edge_case(self):
            """Test with n=0, an edge case for non-negative input."""
            self.assertListEqual(mod.count_up_to(0), [])

    def test_n_is_one_edge_case(self):
            """Test with n=1, another edge case where no primes are less than 1."""
            self.assertListEqual(mod.count_up_to(1), [])

    def test_n_is_two_boundary(self):
            """Test the boundary n=2. No primes are less than 2.
            Catches 'less than' vs 'less than or equal to' for the smallest prime."""
            self.assertListEqual(mod.count_up_to(2), [])

    def test_n_is_three_boundary(self):
            """Test the boundary n=3. Only prime 2 is less than 3.
            Catches 'less than' vs 'less than or equal to' for the first prime."""
            self.assertListEqual(mod.count_up_to(3), [2])

    def test_n_is_four_off_by_one_and_boundary(self):
            """Test n=4. Primes less than 4 are 2, 3.
            Checks inclusion of n-1 (which is prime) and exclusion of n (which is composite)."""
            self.assertListEqual(mod.count_up_to(4), [2, 3])

    def test_n_is_five_typical_and_boundary(self):
            """Test n=5, a typical input from docstring. Primes less than 5 are 2, 3.
            Crucially, 5 itself is prime but should not be included (due to '< n' condition).
            This tests the strict inequality boundary."""
            self.assertListEqual(mod.count_up_to(5), [2, 3])

    def test_n_is_six_off_by_one_and_boundary(self):
            """Test n=6. Primes less than 6 are 2, 3, 5.
            Checks inclusion of n-1 (which is prime) and exclusion of n (which is composite)."""
            self.assertListEqual(mod.count_up_to(6), [2, 3, 5])

    def test_n_is_eleven_typical(self):
            """Test n=11, a typical input from docstring. Primes less than 11 are 2, 3, 5, 7.
            11 itself is prime but should not be included."""
            self.assertListEqual(mod.count_up_to(11), [2, 3, 5, 7])

    def test_n_is_twenty_extreme(self):
            """Test n=20, a larger input from docstring, covering more primes."""
            self.assertListEqual(mod.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_n_is_large_number_extreme(self):
            """Test with a larger number (n=30) to ensure correctness for a longer sequence of primes."""
            self.assertListEqual(mod.count_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_case_five(self):
            self.assertEqual(mod.count_up_to(5), [2, 3])

    def test_normal_case_eleven(self):
            self.assertEqual(mod.count_up_to(11), [2, 3, 5, 7])

    def test_normal_case_twenty(self):
            self.assertEqual(mod.count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_edge_case_zero(self):
            self.assertEqual(mod.count_up_to(0), [])

    def test_edge_case_one(self):
            self.assertEqual(mod.count_up_to(1), [])

    def test_edge_case_two(self):
            self.assertEqual(mod.count_up_to(2), [])

    def test_edge_case_three(self):
            self.assertEqual(mod.count_up_to(3), [2])

    def test_edge_case_four(self):
            self.assertEqual(mod.count_up_to(4), [2, 3])

