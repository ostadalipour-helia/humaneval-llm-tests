import unittest
import sut.problem_HumanEval_41 as mod

class TestHybrid(unittest.TestCase):
    def test_n_zero(self):
            """
            Test with n=0 cars.
            Boundary condition: minimum possible number of cars.
            Expected: 0 collisions.
            """
            self.assertEqual(mod.car_race_collision(0), 0)

    def test_n_one(self):
            """
            Test with n=1 car.
            Boundary condition: single car set.
            Expected: 1 collision (the one L-car collides with the one R-car).
            """
            self.assertEqual(mod.car_race_collision(1), 1)

    def test_n_two(self):
            """
            Test with n=2 cars.
            Typical input, also an off-by-one from n=1.
            Expected: 4 collisions (2 L-cars * 2 R-cars).
            """
            self.assertEqual(mod.car_race_collision(2), 4)

    def test_n_three(self):
            """
            Test with n=3 cars.
            Typical input.
            Expected: 9 collisions (3 L-cars * 3 R-cars).
            """
            self.assertEqual(mod.car_race_collision(3), 9)

    def test_n_five(self):
            """
            Test with n=5 cars.
            Typical input, a mid-range value.
            Expected: 25 collisions (5 L-cars * 5 R-cars).
            """
            self.assertEqual(mod.car_race_collision(5), 25)

    def test_n_ten(self):
            """
            Test with n=10 cars.
            Larger typical input.
            Expected: 100 collisions (10 L-cars * 10 R-cars).
            """
            self.assertEqual(mod.car_race_collision(10), 100)

    def test_n_large_number(self):
            """
            Test with a large number of cars (n=100).
            Extreme input to check scalability and correctness for larger values.
            Expected: 10000 collisions.
            """
            self.assertEqual(mod.car_race_collision(100), 10000)

    def test_n_very_large_number(self):
            """
            Test with a very large number of cars (n=1000).
            Extreme input to stress test the function.
            Expected: 1,000,000 collisions.
            """
            self.assertEqual(mod.car_race_collision(1000), 1000000)

    def test_n_off_by_one_from_typical_lower(self):
            """
            Test with n=4 cars.
            Off-by-one test relative to n=5 (a typical value).
            Expected: 16 collisions.
            """
            self.assertEqual(mod.car_race_collision(4), 16)

    def test_n_off_by_one_from_typical_upper(self):
            """
            Test with n=6 cars.
            Off-by-one test relative to n=5 (a typical value).
            Expected: 36 collisions.
            """
            self.assertEqual(mod.car_race_collision(6), 36)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_one_car(self):
            # Normal case: n=1, expecting 1 collision.
            self.assertEqual(mod.car_race_collision(1), 1)

    def test_normal_two_cars(self):
            # Normal case: n=2, expecting 4 collisions (2*2).
            self.assertEqual(mod.car_race_collision(2), 4)

    def test_normal_five_cars(self):
            # Normal case: n=5, expecting 25 collisions (5*5).
            self.assertEqual(mod.car_race_collision(5), 25)

    def test_edge_no_cars(self):
            # Edge case: n=0, expecting 0 collisions.
            self.assertEqual(mod.car_race_collision(0), 0)

    def test_edge_large_number_of_cars(self):
            # Edge case: n=100, expecting 10000 collisions (100*100).
            self.assertEqual(mod.car_race_collision(100), 10000)

    def test_error_string_n(self):
            # Error case: n is a string, expecting TypeError.
            with self.assertRaises(TypeError):
                mod.car_race_collision("abc")

