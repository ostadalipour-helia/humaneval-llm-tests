import math

def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Determine the effective integer range within [x, y].
    # math.ceil(x) finds the smallest integer greater than or equal to x.
    # math.floor(y) finds the largest integer less than or equal to y.
    start_int = math.ceil(x)
    end_int = math.floor(y)

    # If the calculated integer range is empty (e.g., x=13.1, y=13.9, or x > y),
    # then no integer exists in the range [x, y], so return -1.
    if start_int > end_int:
        return -1

    # Iterate downwards from the largest possible integer in the range (end_int)
    # to the smallest possible integer in the range (start_int).
    # The `range` function requires integer arguments. math.ceil and math.floor
    # return floats, so they are cast to int.
    # range(stop, start-1, -1) effectively iterates from stop down to start (inclusive).
    for i in range(int(end_int), int(start_int) - 1, -1):
        # Check if the current number is even.
        if i % 2 == 0:
            # If an even number is found, it's the biggest one due to descending iteration.
            return i
    
    # If the loop completes, it means no even number was found in the specified range.
    return -1