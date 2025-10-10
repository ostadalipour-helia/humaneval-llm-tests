import unittest
from sut.problem_HumanEval_148 import bf

class TestBfFunction(unittest.TestCase):

    def test_1_basic_valid_standard_order(self):
        # Test a typical case with planets in standard order (planet1 closer to Sun)
        # Covers: Typical input, exact output.
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test_2_basic_valid_reverse_order(self):
        # Test a typical case with planets in reverse order (planet2 closer to Sun)
        # Covers: Typical input, reverse order handling, single element output.
        self.assertEqual(bf("Earth", "Mercury"), ("Venus",))

    def test_3_max_range_standard_order(self):
        # Test the widest possible range of planets in standard order
        # Covers: Extreme input, boundary (first and last planet), multiple elements.
        self.assertEqual(bf("Mercury", "Neptune"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_4_max_range_reverse_order(self):
        # Test the widest possible range of planets in reverse order
        # Covers: Extreme input, boundary (first and last planet, reversed), multiple elements.
        self.assertEqual(bf("Neptune", "Mercury"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus"))

    def test_5_adjacent_planets_standard_order(self):
        # Test two adjacent planets in standard order, expecting an empty tuple
        # Covers: Boundary (no planets in between), off-by-one (should not include Earth or Mars), empty tuple return.
        self.assertEqual(bf("Earth", "Mars"), ())

    def test_6_adjacent_planets_reverse_order(self):
        # Test two adjacent planets in reverse order, expecting an empty tuple
        # Covers: Boundary (no planets in between, reversed), off-by-one, empty tuple return.
        self.assertEqual(bf("Mars", "Earth"), ())

    def test_7_same_planet_names(self):
        # Test when both planet names are identical
        # Covers: Edge case (duplicate input), empty tuple return.
        self.assertEqual(bf("Earth", "Earth"), ())

    def test_8_one_invalid_planet1(self):
        # Test with one invalid planet name as planet1
        # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
        self.assertEqual(bf("Pluto", "Earth"), ())

    def test_9_one_invalid_planet2(self):
        # Test with one invalid planet name as planet2
        # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
        self.assertEqual(bf("Earth", "Krypton"), ())

    def test_10_both_invalid_planets(self):
        # Test with both planet names being invalid
        # Covers: Invalid input, empty tuple return, logic mutation (checking validity of both inputs).
        self.assertEqual(bf("Pluto", "Krypton"), ())

if __name__ == '__main__':
    unittest.main()