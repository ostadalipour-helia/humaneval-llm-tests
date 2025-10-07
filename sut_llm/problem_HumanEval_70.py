def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []

    # Sort the list to easily access the current minimum (from the left)
    # and the current maximum (from the right) of the remaining elements.
    sorted_lst = sorted(lst)
    
    result = []
    left = 0
    right = len(sorted_lst) - 1
    
    # Flag to alternate between taking the minimum and maximum
    take_min_turn = True 
    
    while left <= right:
        if take_min_turn:
            # Take the current minimum
            result.append(sorted_lst[left])
            left += 1
        else:
            # Take the current maximum
            result.append(sorted_lst[right])
            right -= 1
        
        # Toggle the turn for the next iteration
        take_min_turn = not take_min_turn 
        
    return result