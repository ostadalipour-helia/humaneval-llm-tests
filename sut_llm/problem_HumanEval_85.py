def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total_sum = 0
    for i, num in enumerate(lst):
        # Check if the index is odd
        if i % 2 != 0:
            # Check if the element at this odd index is even
            if num % 2 == 0:
                total_sum += num
    return total_sum