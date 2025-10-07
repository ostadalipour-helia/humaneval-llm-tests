def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string into a list of words using a single space as the delimiter.
    # This approach is crucial because it preserves the original spacing structure:
    # - Multiple spaces between words will result in empty strings in the list.
    #   Example: "a  b".split(' ') -> ['a', '', 'b']
    # - Leading/trailing spaces will also result in empty strings at the start/end.
    #   Example: " hi ".split(' ') -> ['', 'hi', '']
    words = s.split(' ')

    processed_words = []
    for word in words:
        if word:  # Check if the word is not an empty string
            # Sort the characters of the word based on their ASCII values.
            # The sorted() function returns a list of characters.
            sorted_chars = sorted(word)
            # Join the sorted characters back into a single string.
            processed_word = "".join(sorted_chars)
            processed_words.append(processed_word)
        else:
            # If the "word" is an empty string (representing one or more spaces
            # between actual words or at the start/end of the sentence),
            # append an empty string to maintain the spacing structure.
            processed_words.append("")

    # Join the processed words back together using a single space.
    # This reconstructs the original spacing pattern correctly.
    # Example: ['Hello', '', 'World'] joined by ' ' -> 'Hello  World'
    return ' '.join(processed_words)