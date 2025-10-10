import unittest
from sut_llm.problem_HumanEval_41 import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_n_is_zero(self):
        self.assertEqual(car_race_collision(0), 0)

    def test_n_is_one(self):
        self.assertEqual(car_race_collision(1), 1)

    def test_n_is_two(self):
        self.assertEqual(car_race_collision(2), 4)

    def test_n_is_three(self):
        self.assertEqual(car_race_collision(3), 9)

    def test_n_is_four(self):
        self.assertEqual(car_race_collision(4), 16)

    def test_n_is_five(self):
        self.assertEqual(car_race_collision(5), 25)

    def test_n_is_seven(self):
        self.assertEqual(car_race_collision(7), 49)

    def test_n_is_ten(self):
        self.assertEqual(car_race_collision(10), 100)

    def test_n_is_thirteen(self):
        self.assertEqual(car_race_collision(13), 169)

    def test_n_is_one_hundred(self):
        self.assertEqual(car_race_collision(100), 10000)