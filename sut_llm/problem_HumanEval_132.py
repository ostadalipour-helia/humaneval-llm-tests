def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    
    # For a subsequence of brackets to be considered "nested", it must contain 
    # a structure where one pair of brackets encloses another non-empty valid 
    # bracket sequence. The simplest such structure is '[[]]'.
    # If we can form '[[]]' as a subsequence from the input string, 
    # then the condition is met.
    # To form '[[]]' as a subsequence, we need to find four characters in the 
    # string at increasing indices i < j < k < l such that:
    # string[i] == '['
    # string[j] == '['
    # string[k] == ']'
    # string[l] == ']'

    # Step 1: Find the first opening bracket '['
    idx1 = string.find('[', 0)
    if idx1 == -1:
        return False  # No opening bracket found

    # Step 2: Find a second opening bracket '[' after the first one
    idx2 = string.find('[', idx1 + 1)
    if idx2 == -1:
        return False  # No second opening bracket found

    # Step 3: Find a closing bracket ']' after the second opening bracket
    idx3 = string.find(']', idx2 + 1)
    if idx3 == -1:
        return False  # No closing bracket found after the second '['

    # Step 4: Find a second closing bracket ']' after the first closing bracket
    idx4 = string.find(']', idx3 + 1)
    if idx4 == -1:
        return False  # No second closing bracket found

    # If all four indices are found in the correct order, it means we can form 
    # the subsequence '[[]]', which is a valid bracket sequence with a nested pair.
    return True