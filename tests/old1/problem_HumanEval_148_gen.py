import unittest
from sut.problem_HumanEval_148 import bf

class TestBf(unittest.TestCase):

    def test_example_1_jupiter_neptune(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_example_2_earth_mercury(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_example_3_mercury_uranus(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test_adjacent_planets_forward(self):
        self.assertEqual(bf("Mercury", "Venus"), ())

    def test_adjacent_planets_backward(self):
        self.assertEqual(bf("Neptune", "Uranus"), ())

    def test_same_planet_names(self):
        self.assertEqual(bf("Earth", "Earth"), ())

    def test_invalid_planet_1(self):
        self.assertEqual(bf("Pluto", "Earth"), ())

    def test_invalid_planet_2(self):
        self.assertEqual(bf("Earth", "Pluto"), ())

    def test_both_invalid_planets(self):
        self.assertEqual(bf("Pluto", "Xenon"), ())

    def test_all_planets_between_outermost(self):
        self.assertEqual(bf("Mercury", "Neptune"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

if __name__ == '__main__':
    unittest.main()