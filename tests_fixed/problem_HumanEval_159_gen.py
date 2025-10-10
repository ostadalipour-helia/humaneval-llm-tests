import unittest
from sut_llm.problem_HumanEval_159 import eat

class TestEatFunction(unittest.TestCase):

    def test_1_typical_enough_carrots(self):
        # Typical case where there are enough remaining carrots.
        # Example from docstring: eat(5, 6, 10) -> [11, 4]
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_2_typical_not_enough_carrots(self):
        # Typical case where there are not enough remaining carrots.
        # Example from docstring: eat(2, 11, 5) -> [7, 0]
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_3_boundary_exactly_enough_carrots(self):
        # Boundary condition: remaining carrots exactly equal to what's needed.
        # This tests the 'remaining >= need' condition at its equality point.
        self.assertEqual(eat(10, 5, 5), [15, 0])

    def test_4_boundary_just_not_enough_carrots(self):
        # Boundary condition: remaining carrots are one less than what's needed.
        # This tests the 'remaining < need' condition just below the equality point.
        self.assertEqual(eat(10, 5, 4), [14, 0])

    def test_5_edge_all_zeros(self):
        # Edge case: all parameters are zero.
        # Tests behavior when number, need, and remaining are at their minimum.
        self.assertEqual(eat(0, 0, 0), [0, 0])

    def test_6_edge_no_remaining_carrots_but_needs_to_eat(self):
        # Edge case: no carrots remaining, but the rabbit still needs to eat.
        # Tests the scenario where 'remaining' is 0 and 'need' is greater than 0.
        self.assertEqual(eat(10, 5, 0), [10, 0])

    def test_7_extreme_max_values_enough_carrots(self):
        # Extreme case: all parameters are large, and there are enough carrots.
        # Tests behavior with values near the upper constraint limit.
        self.assertEqual(eat(1000, 500, 1000), [1500, 500])

    def test_8_extreme_max_values_not_enough_carrots(self):
        # Extreme case: all parameters are large, but not enough carrots.
        # Tests behavior with values near the upper constraint limit, triggering the "not enough" path.
        self.assertEqual(eat(1000, 1000, 500), [1500, 0])

    def test_9_specific_rabbit_does_not_need_to_eat(self):
        # Specific case: the rabbit needs 0 carrots.
        # Tests the 'need = 0' scenario, which should result in no change to eaten or remaining.
        self.assertEqual(eat(50, 0, 100), [50, 100])

    def test_10_boundary_just_enough_carrots_large_need(self):
        # Boundary condition: 'need' is large, and 'remaining' is just one more than 'need'.
        # This tests an off-by-one scenario for the 'remaining - need' calculation.
        self.assertEqual(eat(1, 999, 1000), [1000, 1])

if __name__ == '__main__':
    unittest.main()