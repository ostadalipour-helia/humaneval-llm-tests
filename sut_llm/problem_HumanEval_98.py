def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}
    
    for i, char in enumerate(s):
        if i % 2 == 0:  # Check if the index is even
            if char in uppercase_vowels:  # Check if the character is an uppercase vowel
                count += 1
                
    return count