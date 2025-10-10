import unittest
from sut_llm.problem_HumanEval_36 import fizz_buzz

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
        # ..., 66, 77 (contains '7' twice), 78 (divisible by 13, contains '7' once)
        # Compared to fizz_buzz(78), the number 78 is now included in the range.
        # 77 contributes 2 '7's.
        # 78 contributes 1 '7'.
        # Total = 2 + 1 = 3.
        self.assertEqual(fizz_buzz(79), 3)

    def test_n_up_to_100(self):
        # Numbers < 100 divisible by 11 or 13:
        # 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66, 77, 78, 88, 91, 99
        # 77 contributes 2 '7's.
        # 78 contributes 1 '7'.
        # Total '7's = 2 + 1 = 3.
        self.assertEqual(fizz_buzz(100), 3)

    def test_n_includes_second_seven_occurrence(self):
        # Numbers < 130 divisible by 11 or 13:
        # ..., 77 (2 '7's), 78 (1 '7'), ..., 117 (1 '7')
        # Total '7's: 2 (from 77) + 1 (from 78) + 1 (from 117) = 4
        self.assertEqual(fizz_buzz(130), 4)

    def test_n_up_to_150(self):
        # Numbers < 150 divisible by 11 or 13:
        # 77 (2 '7's), 78 (1 '7'), 117 (1 '7')
        # Total '7's: 2 + 1 + 1 = 4
        self.assertEqual(fizz_buzz(150), 4)

    def test_n_large_value(self):
        # Numbers < 200 divisible by 11 or 13 that contain the digit '7':
        # 77 (divisible by 11): contains '7' twice (count = 2)
        # 78 (divisible by 13): contains '7' once (count = 1)
        # 117 (divisible by 13): contains '7' once (count = 1)
        # 176 (divisible by 11): contains '7' once (count = 1)
        # 187 (divisible by 11): contains '7' once (count = 1)
        # Total count = 2 + 1 + 1 + 1 + 1 = 6
        self.assertEqual(fizz_buzz(200), 6)

if __name__ == '__main__':
    unittest.main()