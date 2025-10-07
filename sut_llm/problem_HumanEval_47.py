def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Input list cannot be empty for median calculation.")

    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # Odd number of elements, median is the middle element
        return sorted_l[n // 2]
    else:
        # Even number of elements, median is the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2.0