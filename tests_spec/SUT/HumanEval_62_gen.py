import unittest
from sut.problem_HumanEval_62 import derivative

class Test_derivative(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), ['3', ',,', '   ', '1111', ',,,,,', '      ', '2222222', ',,,,,,,,', '         ', '4444444444', ',,,,,,,,,,,', '            ', '5555555555555', ']]]]]]]]]]]]]]'])

    def test_case_1(self):
        self.assertEqual(derivative([1, 2, 3]), ['1', ',,', '   ', '2222', ',,,,,', '      ', '3333333', ']]]]]]]]'])

    def test_case_2(self):
        self.assertEqual(derivative([0, 0, 0, 0]), ['0', ',,', '   ', '0000', ',,,,,', '      ', '0000000', ',,,,,,,,', '         ', '0000000000', ']]]]]]]]]]]'])

    def test_case_3(self):
        self.assertEqual(derivative([1.0, 2.5, 3.0, 0.5]), ['1', '..', '000', ',,,,', '     ', '222222', '.......', '55555555', ',,,,,,,,,', '          ', '33333333333', '............', '0000000000000', ',,,,,,,,,,,,,,', '               ', '0000000000000000', '.................', '555555555555555555', ']]]]]]]]]]]]]]]]]]]'])

    def test_case_4(self):
        self.assertEqual(derivative([5]), ['5', ']]'])

    def test_case_5(self):
        self.assertEqual(derivative([0]), ['0', ']]'])

    def test_case_6(self):
        self.assertEqual(derivative([]), [']'])

    def test_case_7(self):
        self.assertEqual(derivative([1, 0, 0]), ['1', ',,', '   ', '0000', ',,,,,', '      ', '0000000', ']]]]]]]]'])

    def test_case_8(self):
        self.assertEqual(derivative([]), [']'])

    def test_case_9(self):
        self.assertEqual(derivative([1, 0, 0]), ['1', ',,', '   ', '0000', ',,,,,', '      ', '0000000', ']]]]]]]]'])