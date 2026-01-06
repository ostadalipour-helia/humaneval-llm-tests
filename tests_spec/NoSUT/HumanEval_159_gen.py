import unittest
from sut.problem_HumanEval_159 import eat

class Test_eat(unittest.TestCase):
    def test_normal_enough_carrots(self):
        # Description: Enough carrots are available to satisfy the need.
        number = 5
        need = 6
        remaining = 10
        expected_output = [11, 4]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_normal_some_left_over(self):
        # Description: Enough carrots are available, with some left over.
        number = 4
        need = 8
        remaining = 9
        expected_output = [12, 1]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_normal_initial_zero(self):
        # Description: Initial eaten carrots is zero, enough remaining.
        number = 0
        need = 5
        remaining = 10
        expected_output = [5, 5]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_exactly_enough(self):
        # Description: Exactly enough carrots are available to satisfy the need, leaving zero.
        number = 1
        need = 10
        remaining = 10
        expected_output = [11, 0]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_not_enough_all_eaten(self):
        # Description: Not enough carrots are available; all remaining carrots are eaten, leaving zero.
        number = 2
        need = 11
        remaining = 5
        expected_output = [7, 0]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_all_zeros(self):
        # Description: All input parameters are zero.
        number = 0
        need = 0
        remaining = 0
        expected_output = [0, 0]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_max_values(self):
        # Description: All input parameters are at their maximum allowed value, exactly enough remaining.
        number = 1000
        need = 1000
        remaining = 1000
        expected_output = [2000, 0]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_need_zero(self):
        # Description: The rabbit needs to eat zero additional carrots.
        number = 10
        need = 0
        remaining = 5
        expected_output = [10, 5]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_edge_remaining_zero(self):
        # Description: There are zero remaining carrots.
        number = 10
        need = 5
        remaining = 0
        expected_output = [10, 0]
        self.assertEqual(eat(number, need, remaining), expected_output)

    def test_error_number_negative(self):
        # Description: Input 'number' is negative, violating constraints.
        with self.assertRaises(ValueError):
            eat(-1, 5, 10)

    def test_error_need_too_high(self):
        # Description: Input 'need' exceeds the maximum allowed value, violating constraints.
        with self.assertRaises(ValueError):
            eat(5, 1001, 10)

    def test_error_remaining_not_int(self):
        # Description: Input 'remaining' is not an integer, violating type constraints.
        with self.assertRaises(TypeError):
            eat(5, 5, "ten")