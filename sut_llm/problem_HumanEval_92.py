def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    # First, check if all three numbers are integers.
    # The problem statement specifies "all numbers are integers".
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    # If they are all integers, then check if one number is the sum of the other two.
    # This can be checked with three possible conditions.
    if (x == y + z) or (y == x + z) or (z == x + y):
        return True
    else:
        # If all are integers but the sum condition is not met.
        return False