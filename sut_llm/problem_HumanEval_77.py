def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a == 0:
        return True

    # Determine if the original number is negative
    is_negative = False
    if a < 0:
        is_negative = True
        # Work with the absolute value for cube root calculation
        target_a = -a 
    else:
        target_a = a

    # Binary search for the integer cube root of target_a
    low = 0
    # The cube root of N is always less than or equal to N.
    # For N >= 2, the integer cube root is strictly less than N.
    # Using `target_a` as the upper bound for the search space `high`
    # is correct and efficient enough for Python's arbitrary-precision integers,
    # as the number of iterations will be proportional to log(target_a).
    high = target_a

    integer_root = 0
    while low <= high:
        mid = (low + high) // 2
        
        # Calculate mid_cubed. Using `mid * mid * mid` to avoid potential
        # floating point issues with `mid**3` if `mid` were a float.
        # However, `mid` is an integer here, so `mid**3` is also fine.
        mid_cubed = mid * mid * mid

        if mid_cubed == target_a:
            integer_root = mid
            break
        elif mid_cubed < target_a:
            low = mid + 1
        else: # mid_cubed > target_a
            high = mid - 1
    
    # Apply the original sign to the found integer_root
    # If the original number was negative, its cube root must also be negative.
    if is_negative:
        final_root = -integer_root
    else:
        final_root = integer_root
    
    # Check if cubing this final_root yields the original number 'a'.
    return final_root * final_root * final_root == a