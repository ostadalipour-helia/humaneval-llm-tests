import collections

def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # Use split() without arguments to handle multiple spaces and empty strings correctly.
    # It splits by any whitespace and removes empty strings from the result.
    letters = test.split()

    # Use collections.Counter to efficiently count occurrences of each letter.
    counts = collections.Counter(letters)

    # If the counter is empty (e.g., the input string was '' or only contained spaces),
    # return an empty dictionary as per the example.
    if not counts:
        return {}

    # Find the maximum count among all letters.
    # This is safe because we've already checked that 'counts' is not empty.
    max_count = max(counts.values())

    # Build the result dictionary, including only letters that have the maximum count.
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count
            
    return result