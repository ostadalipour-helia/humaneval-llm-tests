def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    
    # Initialize the result to -1, which will be returned if no such element is found.
    result_index = -1

    # Iterate through the array starting from the second element (index 1).
    # We compare each element with its predecessor.
    for i in range(1, len(arr)):
        # Check if the current element is NOT greater than or equal to the preceding element.
        # This means arr[i] < arr[i-1].
        if arr[i] < arr[i-1]:
            # If this condition is met, update result_index to the current index i.
            # Since we iterate from left to right, the last update will naturally
            # be the largest index satisfying the condition.
            result_index = i
            
    return result_index