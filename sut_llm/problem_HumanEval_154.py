def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not b:
        # An empty string is considered a substring of any string (including an empty string).
        # Its only rotation is itself.
        return True

    len_a = len(a)
    len_b = len(b)

    # If the second word (b) is longer than the first word (a),
    # no rotation of b can be a substring of a.
    # This check is only relevant if b is not empty (handled above).
    if len_b > len_a:
        return False

    # Generate all rotations of b
    for i in range(len_b):
        # Create a rotation: move the prefix of length i to the end
        rotation_b = b[i:] + b[:i]
        
        # Check if this rotation is a substring of a
        if rotation_b in a:
            return True
            
    # If no rotation was found as a substring, return False
    return False