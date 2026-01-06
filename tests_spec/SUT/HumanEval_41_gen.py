import unittest
from sut.problem_HumanEval_41 import car_race_collision

class Test_car_race_collision(unittest.TestCase):

    def test_normal_case_one_car(self):
        self.assertEqual(car_race_collision(n=1), 1)

    def test_normal_case_two_cars(self):
        self.assertEqual(car_race_collision(n=2), 4)

    def test_normal_case_five_cars(self):
        self.assertEqual(car_race_collision(n=5), 25)

    def test_edge_case_no_cars(self):
        self.assertEqual(car_race_collision(n=0), 0)

    def test_edge_case_large_number(self):
        self.assertEqual(car_race_collision(n=100), 10000)

    def test_normal_case_one_car_repeat(self):
        self.assertEqual(car_race_collision(n=1), 1)

    def test_normal_case_two_cars_repeat(self):
        self.assertEqual(car_race_collision(n=2), 4)

    def test_normal_case_five_cars_repeat(self):
        self.assertEqual(car_race_collision(n=5), 25)

    def test_edge_case_no_cars_repeat(self):
        self.assertEqual(car_race_collision(n=0), 0)

    def test_edge_case_large_number_repeat(self):
        self.assertEqual(car_race_collision(n=100), 10000)