import collections

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    
    # Use collections.Counter to get frequencies of all numbers in the list
    counts = collections.Counter(lst)
    
    # Initialize a list to store numbers that satisfy the condition
    candidates = []
    
    # Iterate through the unique numbers in the list
    # The problem states positive integers, so we don't need to check num > 0 explicitly
    for num, freq in counts.items():
        # Check if the frequency of the number is greater than or equal to its value
        if freq >= num:
            candidates.append(num)
            
    # If there are no candidates, return -1
    if not candidates:
        return -1
    # Otherwise, return the greatest number among the candidates
    else:
        return max(candidates)