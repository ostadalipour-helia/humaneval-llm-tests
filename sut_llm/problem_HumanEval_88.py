def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array or len(array) == 1:
        # For empty or single-element arrays, return a copy of the array itself.
        # The sum condition doesn't apply or is trivial.
        return list(array)

    first_val = array[0]
    last_val = array[-1]
    
    total_sum = first_val + last_val

    if total_sum % 2 == 1:
        # Sum is odd, sort in ascending order
        return sorted(array)
    else:
        # Sum is even, sort in descending order
        return sorted(array, reverse=True)