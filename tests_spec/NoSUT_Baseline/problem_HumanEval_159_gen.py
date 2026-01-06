import unittest
import sut.problem_HumanEval_159 as mod

class TestHybrid(unittest.TestCase):
    def test_1_typical_enough_carrots(self):
            # Typical case where there are enough remaining carrots.
            # Example from docstring: mod.eat(5, 6, 10) -> [11, 4]
            self.assertEqual(mod.eat(5, 6, 10), [11, 4])

    def test_2_typical_not_enough_carrots(self):
            # Typical case where there are not enough remaining carrots.
            # Example from docstring: mod.eat(2, 11, 5) -> [7, 0]
            self.assertEqual(mod.eat(2, 11, 5), [7, 0])

    def test_3_boundary_exactly_enough_carrots(self):
            # Boundary condition: remaining carrots exactly equal to what's needed.
            # This tests the 'remaining >= need' condition at its equality point.
            self.assertEqual(mod.eat(10, 5, 5), [15, 0])

    def test_4_boundary_just_not_enough_carrots(self):
            # Boundary condition: remaining carrots are one less than what's needed.
            # This tests the 'remaining < need' condition just below the equality point.
            self.assertEqual(mod.eat(10, 5, 4), [14, 0])

    def test_5_edge_all_zeros(self):
            # Edge case: all parameters are zero.
            # Tests behavior when number, need, and remaining are at their minimum.
            self.assertEqual(mod.eat(0, 0, 0), [0, 0])

    def test_7_extreme_max_values_enough_carrots(self):
            # Extreme case: all parameters are large, and there are enough carrots.
            # Tests behavior with values near the upper constraint limit.
            self.assertEqual(mod.eat(1000, 500, 1000), [1500, 500])

    def test_8_extreme_max_values_not_enough_carrots(self):
            # Extreme case: all parameters are large, but not enough carrots.
            # Tests behavior with values near the upper constraint limit, triggering the "not enough" path.
            self.assertEqual(mod.eat(1000, 1000, 500), [1500, 0])

    def test_10_boundary_just_enough_carrots_large_need(self):
            # Boundary condition: 'need' is large, and 'remaining' is just one more than 'need'.
            # This tests an off-by-one scenario for the 'remaining - need' calculation.
            self.assertEqual(mod.eat(1, 999, 1000), [1000, 1])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_enough_carrots(self):
            # Description: Enough carrots are available to satisfy the need.
            number = 5
            need = 6
            remaining = 10
            expected_output = [11, 4]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_normal_some_left_over(self):
            # Description: Enough carrots are available, with some left over.
            number = 4
            need = 8
            remaining = 9
            expected_output = [12, 1]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_normal_initial_zero(self):
            # Description: Initial eaten carrots is zero, enough remaining.
            number = 0
            need = 5
            remaining = 10
            expected_output = [5, 5]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_exactly_enough(self):
            # Description: Exactly enough carrots are available to satisfy the need, leaving zero.
            number = 1
            need = 10
            remaining = 10
            expected_output = [11, 0]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_not_enough_all_eaten(self):
            # Description: Not enough carrots are available; all remaining carrots are eaten, leaving zero.
            number = 2
            need = 11
            remaining = 5
            expected_output = [7, 0]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_all_zeros(self):
            # Description: All input parameters are zero.
            number = 0
            need = 0
            remaining = 0
            expected_output = [0, 0]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_max_values(self):
            # Description: All input parameters are at their maximum allowed value, exactly enough remaining.
            number = 1000
            need = 1000
            remaining = 1000
            expected_output = [2000, 0]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_need_zero(self):
            # Description: The rabbit needs to eat zero additional carrots.
            number = 10
            need = 0
            remaining = 5
            expected_output = [10, 5]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_edge_remaining_zero(self):
            # Description: There are zero remaining carrots.
            number = 10
            need = 5
            remaining = 0
            expected_output = [10, 0]
            self.assertEqual(mod.eat(number, need, remaining), expected_output)

    def test_error_remaining_not_int(self):
            # Description: Input 'remaining' is not an integer, violating type constraints.
            with self.assertRaises(TypeError):
                mod.eat(5, 5, "ten")

