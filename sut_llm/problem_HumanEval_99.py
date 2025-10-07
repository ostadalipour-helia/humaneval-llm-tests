import math

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    
    float_val = float(value)

    if float_val >= 0:
        # For positive numbers, "round away from zero" for X.5 means rounding up.
        # This is equivalent to floor(x + 0.5).
        return int(math.floor(float_val + 0.5))
    else:
        # For negative numbers, "round away from zero" for X.5 means rounding down (more negative).
        # This is equivalent to ceil(x - 0.5).
        return int(math.ceil(float_val - 0.5))