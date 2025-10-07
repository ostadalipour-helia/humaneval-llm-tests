import collections

def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # An empty list or a list with one element is considered sorted
    # and cannot have more than one duplicate of any number.
    if len(lst) <= 1:
        return True

    # Check for the duplicate constraint: no more than one duplicate of the same number.
    # This means each number can appear at most twice.
    counts = collections.Counter(lst)
    for count in counts.values():
        if count > 2:
            return False

    # Check for ascending order.
    # Iterate from the second element to compare with the previous one.
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False

    # If both checks pass, the list is sorted according to the rules.
    return True