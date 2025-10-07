def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    
    # Filter out strings with odd lengths
    # A string 's' has an even length if len(s) % 2 == 0
    filtered_list = [s for s in lst if len(s) % 2 == 0]

    # Sort the filtered list
    # The primary sort key is the length of the string (ascending)
    # The secondary sort key is the string itself (alphabetical, ascending)
    # Python's sorted() function with a key that returns a tuple handles this naturally.
    # It sorts by the first element of the tuple, then by the second if the first are equal, and so on.
    sorted_result = sorted(filtered_list, key=lambda s: (len(s), s))

    return sorted_result