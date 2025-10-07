def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None

    product_of_signs = 1
    sum_of_magnitudes = 0

    for num in arr:
        sum_of_magnitudes += abs(num)

        if num == 0:
            product_of_signs = 0
            # If any number is 0, the product of signs will be 0.
            # We can stop evaluating the sign product, but still need
            # to sum magnitudes for the rest of the array.
            # The final multiplication by 0 will correctly yield 0.
        elif num < 0:
            product_of_signs *= -1
        # If num > 0, product_of_signs remains unchanged (effectively multiplied by 1).

    return sum_of_magnitudes * product_of_signs