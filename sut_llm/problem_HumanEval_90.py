def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if not lst:
        return None

    # Convert to a set to remove duplicates, then convert back to a list
    # and sort it.
    unique_sorted_lst = sorted(list(set(lst)))

    # If the length of the unique sorted list is less than 2,
    # there is no 2nd smallest unique element.
    if len(unique_sorted_lst) < 2:
        return None
    else:
        # The 2nd smallest element will be at index 1 (0-indexed)
        return unique_sorted_lst[1]