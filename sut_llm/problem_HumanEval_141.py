def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    
    # Condition 2: The file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    prefix = parts[0]
    suffix = parts[1]

    # Condition 3: The substring before the dot should not be empty
    if not prefix:
        return 'No'
    
    # Condition 3: ...and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z').
    if not prefix[0].isalpha():
        return 'No'

    # Condition 4: The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    valid_extensions = ['txt', 'exe', 'dll']
    if suffix not in valid_extensions:
        return 'No'

    # Condition 1: There should not be more than three digits ('0'-'9') in the file's name.
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
    
    if digit_count > 3:
        return 'No'

    # If all conditions are met
    return 'Yes'