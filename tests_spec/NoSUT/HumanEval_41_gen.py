import unittest
from sut.problem_HumanEval_41 import car_race_collision

class Test_car_race_collision(unittest.TestCase):

    def test_normal_one_car(self):
        # Normal case: n=1, expecting 1 collision.
        self.assertEqual(car_race_collision(1), 1)

    def test_normal_two_cars(self):
        # Normal case: n=2, expecting 4 collisions (2*2).
        self.assertEqual(car_race_collision(2), 4)

    def test_normal_five_cars(self):
        # Normal case: n=5, expecting 25 collisions (5*5).
        self.assertEqual(car_race_collision(5), 25)

    def test_edge_no_cars(self):
        # Edge case: n=0, expecting 0 collisions.
        self.assertEqual(car_race_collision(0), 0)

    def test_edge_large_number_of_cars(self):
        # Edge case: n=100, expecting 10000 collisions (100*100).
        self.assertEqual(car_race_collision(100), 10000)

    def test_error_negative_n(self):
        # Error case: n is negative, expecting ValueError.
        with self.assertRaises(ValueError):
            car_race_collision(-1)

    def test_error_float_n(self):
        # Error case: n is a float, expecting TypeError.
        with self.assertRaises(TypeError):
            car_race_collision(3.14)

    def test_error_string_n(self):
        # Error case: n is a string, expecting TypeError.
        with self.assertRaises(TypeError):
            car_race_collision("abc")