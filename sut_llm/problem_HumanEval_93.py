def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    encoded_message = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    for char in message:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in vowels:
                # If it's a vowel, replace with the letter 2 places ahead.
                # The examples show that replaced vowels are always uppercase.
                new_char_ord = ord(char_lower) + 2
                new_char = chr(new_char_ord).upper()
                encoded_message.append(new_char)
            else:
                # If it's a consonant, swap its case.
                encoded_message.append(char.swapcase())
        else:
            # If it's not an alphabetic character (e.g., space), preserve it.
            encoded_message.append(char)
            
    return "".join(encoded_message)