def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # First, replace all commas with spaces.
    # This ensures that all delimiters are spaces.
    s_modified = s.replace(",", " ")
    
    # Then, split the string by spaces.
    # The `split()` method without arguments splits by any whitespace
    # and handles multiple spaces between words correctly,
    # effectively removing any empty strings that might result from
    # consecutive spaces (e.g., from "Hi, my" becoming "Hi  my").
    words = s_modified.split()
    
    return words