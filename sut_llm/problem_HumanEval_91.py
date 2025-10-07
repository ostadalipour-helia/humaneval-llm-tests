import re

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    count = 0
    # Split the string into potential sentence fragments using the specified delimiters.
    # re.split will return a list of strings. It can produce empty strings
    # if delimiters are at the start/end or are consecutive (e.g., "Hello!!World").
    sentences = re.split(r'[.?!]', S)

    for sentence_fragment in sentences:
        # Clean up leading/trailing whitespace from the fragment.
        trimmed_sentence = sentence_fragment.strip()

        # If the trimmed fragment is empty, it's not a valid sentence, so skip it.
        if not trimmed_sentence:
            continue

        # Split the trimmed sentence into words.
        # str.split() without arguments splits by any whitespace and handles multiple spaces
        # correctly (e.g., "  I  am" becomes ['I', 'am']).
        words = trimmed_sentence.split()

        # Check if there are any words in the sentence and if the first word is exactly "I".
        # The problem specifies "starts with the word 'I'", implying case-sensitive match.
        if words and words[0] == "I":
            count += 1
            
    return count