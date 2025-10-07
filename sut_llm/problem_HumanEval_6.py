from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result_levels = []
    
    # Split the input string into individual groups of parentheses
    # Using .split() without arguments handles multiple spaces and leading/trailing spaces correctly
    groups = paren_string.split()
    
    for group in groups:
        current_level = 0
        max_level = 0
        
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                # Assuming valid parentheses, current_level will not go negative.
                current_level -= 1
        
        result_levels.append(max_level)
        
    return result_levels