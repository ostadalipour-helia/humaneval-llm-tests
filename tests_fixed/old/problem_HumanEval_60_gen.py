import unittest
from sut_llm.problem_HumanEval_60 import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_example_30(self):
        self.assertEqual(sum_to_n(30), 465)

    def test_example_100(self):
        self.assertEqual(sum_to_n(100), 5050)

    def test_example_5(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_example_10(self):
        self.assertEqual(sum_to_n(10), 55)

    def test_example_1(self):
        self.assertEqual(sum_to_n(1), 1)

    def test_zero_input(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_small_positive_2(self):
        self.assertEqual(sum_to_n(2), 3)

    def test_small_positive_7(self):
        self.assertEqual(sum_to_n(7), 28)

    def test_medium_positive_15(self):
        self.assertEqual(sum_to_n(15), 120)

    def test_larger_positive_50(self):
        self.assertEqual(sum_to_n(50), 1275)

if __name__ == '__main__':
    unittest.main()