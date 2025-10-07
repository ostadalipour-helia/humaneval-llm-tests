import unittest
from sut_llm.problem_HumanEval_96 import count_up_to

class TestCountUpTo(unittest.TestCase):

    def test_example_5(self):
        self.assertListEqual(count_up_to(5), [2, 3])

    def test_example_11(self):
        self.assertListEqual(count_up_to(11), [2, 3, 5, 7])

    def test_example_0(self):
        self.assertListEqual(count_up_to(0), [])

    def test_example_20(self):
        self.assertListEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_example_1(self):
        self.assertListEqual(count_up_to(1), [])

    def test_example_18(self):
        self.assertListEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

    def test_edge_case_2(self):
        # Primes less than 2: none
        self.assertListEqual(count_up_to(2), [])

    def test_small_prime_limit_3(self):
        # Primes less than 3: [2]
        self.assertListEqual(count_up_to(3), [2])

    def test_small_composite_limit_4(self):
        # Primes less than 4: [2, 3]
        self.assertListEqual(count_up_to(4), [2, 3])

    def test_prime_limit_7(self):
        # Primes less than 7: [2, 3, 5]
        self.assertListEqual(count_up_to(7), [2, 3, 5])

    def test_covers_even_non_prime_check(self):
        # This test case will cause is_prime(4) to be called within count_up_to(5).
        # Inside is_prime(4), the condition 'if num % 2 == 0' (line 21) will be true,
        # covering the specified line.
        result = count_up_to(5)
        self.assertEqual(result, [2, 3])

if __name__ == '__main__':
    unittest.main()