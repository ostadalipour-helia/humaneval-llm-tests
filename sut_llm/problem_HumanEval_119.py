def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
    def is_balanced(s):
        """
        Checks if a given string of parentheses is balanced.
        A string is balanced if:
        1. The total number of '(' equals the total number of ')'.
        2. For any prefix of the string, the number of '(' is greater than or equal to the number of ')'.
        """
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                balance -= 1
            if balance < 0:
                return False  # More closing than opening at some point
        return balance == 0  # Final balance must be zero

    s1 = lst[0]
    s2 = lst[1]

    # Check the first possible concatenation order: s1 + s2
    if is_balanced(s1 + s2):
        return 'Yes'

    # Check the second possible concatenation order: s2 + s1
    if is_balanced(s2 + s1):
        return 'Yes'

    # If neither concatenation results in a balanced string
    return 'No'