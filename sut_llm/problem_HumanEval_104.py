def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    
    filtered_numbers = []
    for num in x:
        # Convert the number to a string to iterate through its digits
        s_num = str(num)
        
        # Check if all digits are odd (i.e., none are even)
        # We use a flag to keep track if an even digit is found
        has_even = False
        for digit_char in s_num:
            digit = int(digit_char)
            if digit % 2 == 0:
                has_even = True
                break # Found an even digit, no need to check further for this number
        
        # If no even digits were found, add the number to our list
        if not has_even:
            filtered_numbers.append(num)
            
    # Sort the collected numbers in increasing order as required
    filtered_numbers.sort()
    
    return filtered_numbers