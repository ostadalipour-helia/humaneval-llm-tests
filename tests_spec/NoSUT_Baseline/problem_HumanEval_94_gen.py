import unittest
import sut.problem_HumanEval_94 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            # Typical/Expected Input - From docstring example
            lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
            self.assertEqual(mod.skjkasdkd(lst), 10)

    def test_example_two(self):
            # Typical/Expected Input - From docstring example
            lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
            self.assertEqual(mod.skjkasdkd(lst), 25)

    def test_empty_list(self):
            # Edge Case: Empty list. Should return 0 if no primes are found.
            lst = []
            self.assertEqual(mod.skjkasdkd(lst), 0)

    def test_single_smallest_prime(self):
            # Boundary/Edge Case: List with only the smallest prime number.
            lst = [2]
            self.assertEqual(mod.skjkasdkd(lst), 2)

    def test_primes_around_zero_one_two(self):
            # Boundary Testing: Tests 0, 1, 2, 3, 4, 5, 6 to check primality logic around small numbers.
            # Largest prime is 5. Sum of digits = 5.
            lst = [0, 1, 2, 3, 4, 5, 6]
            self.assertEqual(mod.skjkasdkd(lst), 5)

    def test_largest_not_prime_smaller_is_largest_prime(self):
            # Logic Mutation Test: Largest number in list is not prime, but a smaller number is the largest prime.
            # Catches issues if 'and' is swapped with 'or' in prime-finding logic.
            # Largest prime is 97. Sum of digits = 9 + 7 = 16.
            lst = [100, 97, 98, 99, 96]
            self.assertEqual(mod.skjkasdkd(lst), 16)

    def test_very_large_prime(self):
            # Extreme Input: List containing a very large prime number.
            # 999999937 is a prime number. Sum of digits = 9*7 + 3 + 7 = 63 + 3 + 7 = 73.
            lst = [100, 101, 999999937, 200]
            self.assertEqual(mod.skjkasdkd(lst), 73)

    def test_list_with_negative_numbers_and_primes(self):
            # Sign Testing: Negative numbers should be ignored as primes are positive integers > 1.
            # Largest prime is 11. Sum of digits = 1 + 1 = 2.
            lst = [-5, -2, 0, 1, 7, 11, 10, -1]
            self.assertEqual(mod.skjkasdkd(lst), 2)

    def test_all_same_prime_values(self):
            # Edge Case: List where all elements are the same prime number.
            # Largest prime is 7. Sum of digits = 7.
            lst = [7, 7, 7, 7, 7]
            self.assertEqual(mod.skjkasdkd(lst), 7)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_case_largest_prime_181(self):
            lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
            self.assertEqual(mod.skjkasdkd(lst), 10)

    def test_normal_case_largest_prime_4597(self):
            lst = [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]
            self.assertEqual(mod.skjkasdkd(lst), 25)

    def test_normal_case_largest_prime_5107(self):
            lst = [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]
            self.assertEqual(mod.skjkasdkd(lst), 13)

    def test_edge_case_empty_list(self):
            lst = []
            self.assertEqual(mod.skjkasdkd(lst), 0)

    def test_edge_case_single_prime_in_list(self):
            lst = [10, 11, 12, 14]
            self.assertEqual(mod.skjkasdkd(lst), 2)

    def test_edge_case_negative_numbers_ignored(self):
            lst = [-2, -3, 5, 7, -10]
            self.assertEqual(mod.skjkasdkd(lst), 7)

    def test_edge_case_large_prime_number(self):
            lst = [1000000007]
            self.assertEqual(mod.skjkasdkd(lst), 8)

    def test_error_case_input_not_a_list(self):
            lst = "not_a_list"
            with self.assertRaises(TypeError):
                mod.skjkasdkd(lst)

    def test_error_case_list_contains_string(self):
            lst = [1, 2, "three", 4]
            with self.assertRaises(TypeError):
                mod.skjkasdkd(lst)

