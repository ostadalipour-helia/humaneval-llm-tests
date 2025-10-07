def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    
    # Convert string c to a set for efficient character lookup (O(1) average time complexity)
    chars_to_delete = set(c)
    
    # Build the new string by filtering characters from s
    result_chars = []
    for char_s in s:
        if char_s not in chars_to_delete:
            result_chars.append(char_s)
            
    result_string = "".join(result_chars)
    
    # Check if the resulting string is a palindrome
    is_palindrome = (result_string == result_string[::-1])
    
    # Return the tuple containing the result string and the palindrome check result
    return (result_string, is_palindrome)