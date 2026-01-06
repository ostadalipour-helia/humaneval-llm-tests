import unittest
import sut.problem_HumanEval_148 as mod

class TestHybrid(unittest.TestCase):
    def test_1_basic_valid_standard_order(self):
            # Test a typical case with planets in standard order (planet1 closer to Sun)
            # Covers: Typical input, exact output.
            self.assertEqual(mod.bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_2_basic_valid_reverse_order(self):
            # Test a typical case with planets in reverse order (planet2 closer to Sun)
            # Covers: Typical input, reverse order handling, single element output.
            self.assertEqual(mod.bf("Earth", "Mercury"), ("Venus",))

    def test_3_max_range_standard_order(self):
            # Test the widest possible range of planets in standard order
            # Covers: Extreme input, boundary (first and last planet), multiple elements.
            self.assertEqual(mod.bf("Mercury", "Neptune"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_4_max_range_reverse_order(self):
            # Test the widest possible range of planets in reverse order
            # Covers: Extreme input, boundary (first and last planet, reversed), multiple elements.
            self.assertEqual(mod.bf("Neptune", "Mercury"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_5_adjacent_planets_standard_order(self):
            # Test two adjacent planets in standard order, expecting an empty tuple
            # Covers: Boundary (no planets in between), off-by-one (should not include Earth or Mars), empty tuple return.
            self.assertEqual(mod.bf("Earth", "Mars"), ())

    def test_6_adjacent_planets_reverse_order(self):
            # Test two adjacent planets in reverse order, expecting an empty tuple
            # Covers: Boundary (no planets in between, reversed), off-by-one, empty tuple return.
            self.assertEqual(mod.bf("Mars", "Earth"), ())

    def test_7_same_planet_names(self):
            # Test when both planet names are identical
            # Covers: Edge case (duplicate input), empty tuple return.
            self.assertEqual(mod.bf("Earth", "Earth"), ())

    def test_8_one_invalid_planet1(self):
            # Test with one invalid planet name as planet1
            # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
            self.assertEqual(mod.bf("Pluto", "Earth"), ())

    def test_9_one_invalid_planet2(self):
            # Test with one invalid planet name as planet2
            # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
            self.assertEqual(mod.bf("Earth", "Krypton"), ())

    def test_10_both_invalid_planets(self):
            # Test with both planet names being invalid
            # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
            self.assertEqual(mod.bf("Pluto", "Krypton"), ())
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_jupiter_neptune(self):
            # Normal case: planets between Jupiter and Neptune
            planet1 = "Jupiter"
            planet2 = "Neptune"
            expected_output = ("Saturn", "Uranus")
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_normal_earth_mercury_reversed(self):
            # Normal case: planets between Earth and Mercury (reversed order)
            planet1 = "Earth"
            planet2 = "Mercury"
            expected_output = ("Venus",)
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_normal_mercury_uranus(self):
            # Normal case: multiple planets between Mercury and Uranus
            planet1 = "Mercury"
            planet2 = "Uranus"
            expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_adjacent_mercury_venus(self):
            # Edge case: adjacent planets, no planets strictly between
            planet1 = "Mercury"
            planet2 = "Venus"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_adjacent_venus_mercury_reversed(self):
            # Edge case: adjacent planets, reversed order
            planet1 = "Venus"
            planet2 = "Mercury"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_same_planet(self):
            # Edge case: same planet, no planets strictly between
            planet1 = "Earth"
            planet2 = "Earth"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_all_planets_between_mercury_neptune(self):
            # Edge case: all intermediate planets
            planet1 = "Mercury"
            planet2 = "Neptune"
            expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_all_planets_between_neptune_mercury_reversed(self):
            # Edge case: all intermediate planets, reversed order
            planet1 = "Neptune"
            planet2 = "Mercury"
            expected_output = ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_name_pluto(self):
            # Edge case: one invalid planet name (not in recognized list)
            planet1 = "Pluto"
            planet2 = "Earth"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_name_sun(self):
            # Edge case: another invalid planet name
            planet1 = "Earth"
            planet2 = "Sun"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_type_int(self):
            # Edge case: invalid planet type (integer)
            planet1 = 123
            planet2 = "Earth"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_invalid_planet_type_none(self):
            # Edge case: invalid planet type (None)
            planet1 = "Earth"
            planet2 = None
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

    def test_edge_case_sensitivity(self):
            # Edge case: planet name with incorrect casing
            planet1 = "Mars"
            planet2 = "mars"
            expected_output = ()
            self.assertEqual(mod.bf(planet1, planet2), expected_output)

