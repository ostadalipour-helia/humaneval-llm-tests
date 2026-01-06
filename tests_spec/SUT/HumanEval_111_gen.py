import unittest
from sut.problem_HumanEval_111 import histogram

class Test_histogram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(histogram("a b c"), {'a': 1, 'b': 1, 'c': 1})

    def test_case_2(self):
        self.assertEqual(histogram("a b b a"), {'a': 2, 'b': 2})

    def test_case_3(self):
        self.assertEqual(histogram("a b c a b"), {'a': 2, 'b': 2})

    def test_case_4(self):
        self.assertEqual(histogram("b b b b a"), {'b': 4})

    def test_case_5(self):
        self.assertEqual(histogram("x y z x y x"), {'x': 3})

    def test_case_6(self):
        self.assertEqual(histogram("m n o p m n o m"), {'m': 3})

    def test_case_7(self):
        self.assertEqual(histogram(""), {})

    def test_case_8(self):
        self.assertEqual(histogram("a"), {'a': 1})

    def test_case_9(self):
        self.assertEqual(histogram("a a a a a"), {'a': 5})

    def test_case_10(self):
        self.assertEqual(histogram("z"), {'z': 1})