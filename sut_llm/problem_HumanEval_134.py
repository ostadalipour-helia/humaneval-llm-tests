def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    # An empty string or a string with only one character cannot satisfy the conditions
    # because we need to check the character before the last one.
    if len(txt) < 2:
        return False

    last_char = txt[-1]
    second_to_last_char = txt[-2]

    # The last character must be an alphabetical character.
    # It must also not be part of a word, which, based on the examples,
    # implies it must be preceded by a space.
    # E.g., "apple pi e" -> 'e' is a letter, and ' ' precedes it.
    # E.g., "apple pie" -> 'e' is a letter, but 'i' precedes it, meaning 'e' is part of "pie".
    if last_char.isalpha() and second_to_last_char == ' ':
        return True
    else:
        return False