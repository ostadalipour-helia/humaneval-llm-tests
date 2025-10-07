import unittest
from sut_llm.problem_HumanEval_53 import add

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers_1(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_numbers_2(self):
        self.assertEqual(add(5, 7), 12)

    def test_add_zero_to_number(self):
        self.assertEqual(add(10, 0), 10)

    def test_add_number_to_zero(self):
        self.assertEqual(add(0, 15), 15)

    def test_add_two_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_positive_and_negative_1(self):
        self.assertEqual(add(10, -3), 7)

    def test_add_positive_and_negative_2(self):
        self.assertEqual(add(-10, 3), -7)

    def test_add_positive_and_negative_resulting_zero(self):
        self.assertEqual(add(-7, 7), 0)

    def test_add_large_positive_numbers(self):
        self.assertEqual(add(1000, 2000), 3000)

if __name__ == '__main__':
    unittest.main()