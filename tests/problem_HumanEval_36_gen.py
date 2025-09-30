import unittest
from sut.problem_HumanEval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_example_50(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_example_78(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_n_is_1(self):
        self.assertEqual(fizz_buzz(1), 0)

    def test_n_just_before_first_seven(self):
        # Numbers < 77 that are divisible by 11 or 13:
        # 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66
        # None of these contain the digit 7.
        self.assertEqual(fizz_buzz(77), 0)

    def test_n_includes_first_seven_occurrence(self):
        # Numbers < 78 that are divisible by 11 or 13:
        # ..., 66, 77 (contains '7' twice)
        self.assertEqual(fizz_buzz(78), 2)

    def test_n_just_after_first_seven_occurrence(self):
        # Numbers < 79 that are divisible by 11 or 13:
        # ..., 66, 77 (contains '7' twice)
        # No new numbers are added compared to fizz_buzz(78)
        self.assertEqual(fizz_buzz(79), 2)

    def test_n_up_to_100(self):
        # Numbers < 100 divisible by 11 or 13:
        # ..., 77 (2 '7's), 88, 91, 99
        # Only 77 contributes '7's.
        self.assertEqual(fizz_buzz(100), 2)

    def test_n_includes_second_seven_occurrence(self):
        # Numbers < 130 divisible by 11 or 13:
        # ..., 77 (2 '7's), ..., 117 (1 '7')
        self.assertEqual(fizz_buzz(130), 3)

    def test_n_up_to_150(self):
        # Numbers < 150 divisible by 11 or 13:
        # ..., 77 (2 '7's), ..., 117 (1 '7'), ..., 143
        # No new numbers with '7's are added.
        self.assertEqual(fizz_buzz(150), 3)

    def test_n_large_value(self):
        # Numbers < 200 divisible by 11 or 13:
        # ..., 77 (2 '7's), ..., 117 (1 '7'), ..., 170 (no '7'), ..., 182 (no '7'), ..., 195 (no '7')
        # No new numbers with '7's are added in this range.
        self.assertEqual(fizz_buzz(200), 3)

if __name__ == '__main__':
    unittest.main()