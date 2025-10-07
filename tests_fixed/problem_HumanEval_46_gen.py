import unittest
from sut_llm.problem_HumanEval_46 import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_0(self):
        self.assertEqual(fib4(0), 0)

    def test_fib4_1(self):
        self.assertEqual(fib4(1), 0)

    def test_fib4_2(self):
        self.assertEqual(fib4(2), 2)

    def test_fib4_3(self):
        self.assertEqual(fib4(3), 0)

    def test_fib4_4(self):
        # fib4(4) = fib4(3) + fib4(2) + fib4(1) + fib4(0) = 0 + 2 + 0 + 0 = 2
        self.assertEqual(fib4(4), 2)

    def test_fib4_5(self):
        # fib4(5) = fib4(4) + fib4(3) + fib4(2) + fib4(1) = 2 + 0 + 2 + 0 = 4
        self.assertEqual(fib4(5), 4)

    def test_fib4_6(self):
        # fib4(6) = fib4(5) + fib4(4) + fib4(3) + fib4(2) = 4 + 2 + 0 + 2 = 8
        self.assertEqual(fib4(6), 8)

    def test_fib4_7(self):
        # fib4(7) = fib4(6) + fib4(5) + fib4(4) + fib4(3) = 8 + 4 + 2 + 0 = 14
        self.assertEqual(fib4(7), 14)

    def test_fib4_8(self):
        # fib4(8) = fib4(7) + fib4(6) + fib4(5) + fib4(4) = 14 + 8 + 4 + 2 = 28
        self.assertEqual(fib4(8), 28)

    def test_fib4_9(self):
        # fib4(9) = fib4(8) + fib4(7) + fib4(6) + fib4(5) = 28 + 14 + 8 + 4 = 54
        self.assertEqual(fib4(9), 54)

if __name__ == '__main__':
    unittest.main()