def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    if not s:
        return []

    # Define a set of lowercase vowels for efficient lookup
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []

    # Split the string into words.
    # The split() method without arguments handles multiple spaces and leading/trailing spaces correctly.
    words = s.split()

    for word in words:
        consonant_count = 0
        for char in word:
            # Convert character to lowercase for case-insensitive comparison
            # The problem states the input contains only letters and spaces,
            # so we don't need to check char.isalpha() explicitly within a word.
            if char.lower() not in vowels:
                consonant_count += 1
        
        # If the word has exactly n consonants, add it to the result list
        if consonant_count == n:
            result.append(word)
            
    return result