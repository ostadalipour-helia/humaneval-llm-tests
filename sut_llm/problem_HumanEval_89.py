def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_chars = []
    
    # The shift amount is "two multiplied to two places" = 2 * 2 = 4
    shift_amount = 4

    for char in s:
        if 'a' <= char <= 'z':
            # Calculate the 0-indexed position of the character (0 for 'a', 25 for 'z')
            current_pos = ord(char) - ord('a')
            
            # Apply the shift and ensure it wraps around the alphabet (0-25)
            new_pos = (current_pos + shift_amount) % 26
            
            # Convert the new 0-indexed position back to a character
            encrypted_char = chr(ord('a') + new_pos)
            encrypted_chars.append(encrypted_char)
        else:
            # If the character is not a lowercase letter (e.g., uppercase, digit, symbol, space),
            # leave it unchanged as per common Caesar cipher implementations when not specified.
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)