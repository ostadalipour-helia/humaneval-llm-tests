import unittest
from sut_llm.problem_HumanEval_94 import skjkasdkd

class TestSkjkasdkd(unittest.TestCase):

    def test_example_1(self):
        lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
        self.assertEqual(skjkasdkd(lst), 10)

    def test_example_2(self):
        lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
        self.assertEqual(skjkasdkd(lst), 25)

    def test_example_3(self):
        lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
        self.assertEqual(skjkasdkd(lst), 13)

    def test_example_4(self):
        lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
        self.assertEqual(skjkasdkd(lst), 11)

    def test_example_5(self):
        lst = [0,81,12,3,1,21]
        self.assertEqual(skjkasdkd(lst), 3)

    def test_example_6(self):
        lst = [0,8,1,2,1,7]
        self.assertEqual(skjkasdkd(lst), 7)

    def test_single_prime_in_list(self):
        lst = [10, 12, 13, 14, 15]
        self.assertEqual(skjkasdkd(lst), 4) # 13 -> 1+3=4

    def test_largest_prime_is_only_prime(self):
        lst = [4, 6, 8, 10, 11, 12]
        self.assertEqual(skjkasdkd(lst), 2) # 11 -> 1+1=2

    def test_primes_at_various_positions(self):
        lst = [2, 100, 101, 102, 3]
        self.assertEqual(skjkasdkd(lst), 2) # 101 -> 1+0+1=2

    def test_large_prime_among_others(self):
        lst = [1000, 997, 1001, 1003, 1009]
        self.assertEqual(skjkasdkd(lst), 10) # 1009 -> 1+0+0+9=10

if __name__ == '__main__':
    unittest.main()