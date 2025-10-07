import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Step 1: Replace sequences of 3 or more consecutive spaces with a single hyphen.
    # This handles the specific rule for "more than 2 consecutive spaces".
    # The regex r' {3,}' matches 3 or more literal space characters.
    processed_text = re.sub(r' {3,}', '-', text)

    # Step 2: Replace any remaining single spaces (which includes any original single spaces
    # and any original double spaces that were not affected by the first regex) with an underscore.
    # This covers the general rule "replace all spaces in it with underscores".
    final_text = re.sub(r' ', '_', processed_text)
    
    return final_text