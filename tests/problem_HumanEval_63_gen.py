import unittest
from sut.problem_HumanEval_63 import fibfib

class TestFibFib(unittest.TestCase):

    def test_fibfib_0(self):
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_1(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_2(self):
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_3(self):
        self.assertEqual(fibfib(3), 1)

    def test_fibfib_4(self):
        self.assertEqual(fibfib(4), 2)

    def test_fibfib_5(self):
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_6(self):
        self.assertEqual(fibfib(6), 7)

    def test_fibfib_7(self):
        self.assertEqual(fibfib(7), 13)

    def test_fibfib_8(self):
        self.assertEqual(fibfib(8), 24)

    def test_fibfib_9(self):
        self.assertEqual(fibfib(9), 44)

if __name__ == '__main__':
    unittest.main()