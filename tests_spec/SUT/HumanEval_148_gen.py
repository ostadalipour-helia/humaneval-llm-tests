import unittest
from sut.problem_HumanEval_148 import bf

class Test_bf(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ('Saturn', 'Uranus'))

    def test_case_2(self):
        self.assertEqual(bf("Earth", "Mercury"), ('Venus',))

    def test_case_3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

    def test_case_4(self):
        self.assertEqual(bf("Mercury", "Venus"), ())

    def test_case_5(self):
        self.assertEqual(bf("Venus", "Mercury"), ())

    def test_case_6(self):
        self.assertEqual(bf("Earth", "Earth"), ())

    def test_case_7(self):
        self.assertEqual(bf("Mercury", "Neptune"), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'))

    def test_case_8(self):
        self.assertEqual(bf("Neptune", "Mercury"), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'))

    def test_case_9(self):
        self.assertEqual(bf("Pluto", "Earth"), ())

    def test_case_10(self):
        self.assertEqual(bf("Earth", "Sun"), ())