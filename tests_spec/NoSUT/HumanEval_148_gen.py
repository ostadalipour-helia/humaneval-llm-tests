import unittest
from sut.problem_HumanEval_148 import bf

class Test_bf(unittest.TestCase):

    def test_normal_jupiter_neptune(self):
        # Normal case: planets between Jupiter and Neptune
        planet1 = "Jupiter"
        planet2 = "Neptune"
        expected_output = ("Saturn", "Uranus")
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_normal_earth_mercury_reversed(self):
        # Normal case: planets between Earth and Mercury (reversed order)
        planet1 = "Earth"
        planet2 = "Mercury"
        expected_output = ("Venus",)
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_normal_mercury_uranus(self):
        # Normal case: multiple planets between Mercury and Uranus
        planet1 = "Mercury"
        planet2 = "Uranus"
        expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_adjacent_mercury_venus(self):
        # Edge case: adjacent planets, no planets strictly between
        planet1 = "Mercury"
        planet2 = "Venus"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_adjacent_venus_mercury_reversed(self):
        # Edge case: adjacent planets, reversed order
        planet1 = "Venus"
        planet2 = "Mercury"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_same_planet(self):
        # Edge case: same planet, no planets strictly between
        planet1 = "Earth"
        planet2 = "Earth"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_all_planets_between_mercury_neptune(self):
        # Edge case: all intermediate planets
        planet1 = "Mercury"
        planet2 = "Neptune"
        expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_all_planets_between_neptune_mercury_reversed(self):
        # Edge case: all intermediate planets, reversed order
        planet1 = "Neptune"
        planet2 = "Mercury"
        expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_name_pluto(self):
        # Edge case: one invalid planet name (not in recognized list)
        planet1 = "Pluto"
        planet2 = "Earth"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_name_sun(self):
        # Edge case: another invalid planet name
        planet1 = "Earth"
        planet2 = "Sun"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_type_int(self):
        # Edge case: invalid planet type (integer)
        planet1 = 123
        planet2 = "Earth"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_type_none(self):
        # Edge case: invalid planet type (None)
        planet1 = "Earth"
        planet2 = None
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)

    def test_edge_case_sensitivity(self):
        # Edge case: planet name with incorrect casing
        planet1 = "Mars"
        planet2 = "mars"
        expected_output = ()
        self.assertEqual(bf(planet1, planet2), expected_output)