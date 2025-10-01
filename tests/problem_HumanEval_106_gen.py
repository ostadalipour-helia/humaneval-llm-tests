import unittest
from sut.problem_HumanEval_106 import f

class TestF(unittest.TestCase):

    def test_f_0(self):
        self.assertEqual(f(0), [])

    def test_f_1(self):
        self.assertEqual(f(1), [1])

    def test_f_2(self):
        self.assertEqual(f(2), [1, 2])

    def test_f_3(self):
        self.assertEqual(f(3), [1, 2, 6])

    def test_f_4(self):
        self.assertEqual(f(4), [1, 2, 6, 24])

    def test_f_5_example(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_f_6(self):
        self.assertEqual(f(6), [1, 2, 6, 24, 15, 720])

    def test_f_7(self):
        self.assertEqual(f(7), [1, 2, 6, 24, 15, 720, 28])

    def test_f_8(self):
        self.assertEqual(f(8), [1, 2, 6, 24, 15, 720, 28, 40320])

    def test_f_9(self):
        self.assertEqual(f(9), [1, 2, 6, 24, 15, 720, 28, 40320, 45])

if __name__ == '__main__':
    unittest.main()