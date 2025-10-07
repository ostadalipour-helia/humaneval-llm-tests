import unittest
from sut_llm.problem_HumanEval_139 import special_factorial

class TestSpecialFactorial(unittest.TestCase):

    def test_special_factorial_1(self):
        self.assertEqual(special_factorial(1), 1)

    def test_special_factorial_2(self):
        self.assertEqual(special_factorial(2), 2)

    def test_special_factorial_3(self):
        self.assertEqual(special_factorial(3), 12)

    def test_special_factorial_4(self):
        self.assertEqual(special_factorial(4), 288)

    def test_special_factorial_5(self):
        self.assertEqual(special_factorial(5), 34560)

    def test_special_factorial_6(self):
        self.assertEqual(special_factorial(6), 24883200)

    def test_special_factorial_7(self):
        self.assertEqual(special_factorial(7), 125411328000)

    def test_special_factorial_8(self):
        self.assertEqual(special_factorial(8), 5056584744960000)

    def test_special_factorial_9(self):
        self.assertEqual(special_factorial(9), 1834933472251084800000)

    def test_special_factorial_10(self):
        self.assertEqual(special_factorial(10), 6658606584104736522240000000)

if __name__ == '__main__':
    unittest.main()