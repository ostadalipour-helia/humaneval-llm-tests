def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    word_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    int_to_word = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
    ]

    # Split the input string into a list of number words
    number_words = numbers.split()

    # Convert words to their integer equivalents
    integer_numbers = [word_to_int[word] for word in number_words]

    # Sort the list of integers
    integer_numbers.sort()

    # Convert the sorted integers back to number words
    sorted_number_words = [int_to_word[num] for num in integer_numbers]

    # Join the sorted number words back into a space-delimited string
    return ' '.join(sorted_number_words)