def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    balance = 0
    for char in brackets:
        if char == '<':
            balance += 1
        elif char == '>':
            balance -= 1
        
        # If balance ever drops below zero, it means a closing bracket appeared
        # without a corresponding opening bracket.
        if balance < 0:
            return False
            
    # After iterating through all characters, if balance is zero, all brackets
    # are correctly matched. Otherwise, there are unmatched opening brackets.
    return balance == 0