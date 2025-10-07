def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    if not substring:
        # An empty substring is a special case.
        # If it's considered to occur at every possible position (e.g., before/after every character),
        # it would lead to string_length + 1 occurrences.
        # However, for typical "find how many times a substring can be found" problems,
        # an empty substring is often considered to not 'exist' as an occurrence,
        # or the problem implies non-empty substrings.
        # Following a conservative interpretation when not explicitly defined, we return 0.
        return 0

    if len(substring) > len(string):
        return 0

    for i in range(len(string)):
        if string.startswith(substring, i):
            count += 1
    return count