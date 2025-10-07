def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ""

    # This variable will store the starting index of the longest palindromic postfix.
    # For example, if string is 'cata' and 'ata' is the longest palindromic postfix,
    # then longest_palindromic_postfix_start_index will be 1 (because 'ata' starts at index 1).
    longest_palindromic_postfix_start_index = 0

    # Iterate through the string to find the longest palindromic postfix.
    # We check postfixes starting from the full string (index 0) down to single characters.
    # The first one we find that is a palindrome will be the longest one.
    for i in range(len(string)):
        postfix = string[i:]
        if is_palindrome(postfix):
            longest_palindromic_postfix_start_index = i
            break  # Found the longest palindromic postfix, exit loop

    # The prefix that needs to be reversed and appended is the part of the string
    # that comes before the longest palindromic postfix.
    prefix_to_reverse = string[:longest_palindromic_postfix_start_index]

    # Reverse this prefix
    reversed_prefix = prefix_to_reverse[::-1]

    # Append the reversed prefix to the original string to form the shortest palindrome
    return string + reversed_prefix