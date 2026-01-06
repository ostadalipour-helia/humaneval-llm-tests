import unittest
import sut.problem_HumanEval_69 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            # Typical input, multiple candidates, verifies exact output
            # 1: freq=2 (2>=1 True), 2: freq=2 (2>=2 True), 3: freq=1 (1>=3 False), 4: freq=1 (1>=4 False)
            # Greatest satisfying is 2.
            self.assertEqual(mod.search([4, 1, 2, 2, 3, 1]), 2)

    def test_example_two(self):
            # Typical input, multiple candidates, verifies exact output
            # 1: freq=1 (1>=1 True), 2: freq=2 (2>=2 True), 3: freq=3 (3>=3 True), 4: freq=3 (3>=4 False)
            # Greatest satisfying is 3.
            self.assertEqual(mod.search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_example_three_no_satisfying_value(self):
            # Typical input, no satisfying value, verifies -1 return
            # 4: freq=3 (3>=4 False), 5: freq=2 (2>=5 False)
            self.assertEqual(mod.search([5, 5, 4, 4, 4]), -1)

    def test_boundary_exact_match_for_greatest(self):
            # Boundary condition: The greatest number satisfies freq == value, others might or might not.
            # 1: freq=1 (1>=1 True), 2: freq=1 (1>=2 False), 3: freq=3 (3>=3 True)
            # Greatest satisfying is 3.
            self.assertEqual(mod.search([3, 3, 3, 1, 2]), 3)

    def test_boundary_all_fail_by_one(self):
            # Boundary condition: All numbers have frequency less than their value (e.g., freq = value - 1).
            # 5: freq=4 (4>=5 False), 6: freq=5 (5>=6 False)
            self.assertEqual(mod.search([6, 6, 6, 6, 6, 5, 5, 5, 5]), -1)

    def test_edge_single_element_satisfies(self):
            # Edge case: Single element list, where the element satisfies the condition.
            # 1: freq=1 (1>=1 True)
            self.assertEqual(mod.search([1]), 1)

    def test_edge_all_same_elements_satisfy(self):
            # Edge case: List with all same values, and they satisfy the condition.
            # 3: freq=3 (3>=3 True)
            self.assertEqual(mod.search([3, 3, 3]), 3)

    def test_extreme_large_number_satisfies(self):
            # Extreme input: A large number is the greatest satisfying value, with other smaller candidates.
            # 1: freq=1 (1>=1 True), 2-9: freq=1 (1>=x False), 10: freq=10 (10>=10 True)
            # Greatest satisfying is 10.
            self.assertEqual(mod.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)

    def test_extreme_many_distinct_none_satisfy(self):
            # Extreme input: Many distinct large numbers, none satisfy the condition.
            # All numbers have freq=1. Since all are > 1, 1 >= x is always False.
            self.assertEqual(mod.search([100, 200, 300, 400, 500]), -1)

    def test_logic_mutation_smaller_satisfies_larger_almost(self):
            # Logic mutation: A smaller number satisfies, but a larger number almost satisfies (freq = value - 1).
            # Ensures the "greatest" condition is correctly applied.
            # 1: freq=3 (3>=1 True), 2: freq=2 (2>=2 True), 3: freq=2 (2>=3 False)
            # Greatest satisfying is 2.
            self.assertEqual(mod.search([2, 2, 1, 1, 1, 3, 3]), 2)

    def test_normal_case_1(self):
            self.assertEqual(mod.search([4, 1, 2, 2, 3, 1]), 2)

    def test_normal_case_2(self):
            self.assertEqual(mod.search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_normal_case_3(self):
            self.assertEqual(mod.search([1, 1, 1, 1, 1]), 1)

    def test_normal_case_4(self):
            self.assertEqual(mod.search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10)
    
        # Edge Cases

    def test_edge_case_single_element_satisfying(self):
            self.assertEqual(mod.search([1]), 1)

    def test_edge_case_single_element_not_satisfying(self):
            self.assertEqual(mod.search([2]), -1)

    def test_edge_case_no_elements_satisfying(self):
            self.assertEqual(mod.search([5, 5, 4, 4, 4]), -1)

    def test_edge_case_only_one_satisfying_among_many(self):
            self.assertEqual(mod.search([1, 2, 3, 4, 5]), 1)

    def test_edge_case_multiple_satisfying_with_non_satisfying(self):
            self.assertEqual(mod.search([1, 1, 2, 2, 3, 3]), 2)
    
        # Error Cases

    def test_error_empty_list(self):
            with self.assertRaises((ValueError, AssertionError)):
                mod.search([])

    def test_error_float_in_list(self):
            with self.assertRaises((TypeError, ValueError, AssertionError)):
                mod.search([1, 2.5, 3])

    def test_error_string_in_list(self):
            with self.assertRaises((TypeError, ValueError, AssertionError)):
                mod.search([1, 'a', 3])

    def test_error_none_as_input(self):
            with self.assertRaises(TypeError):
                mod.search(None)

