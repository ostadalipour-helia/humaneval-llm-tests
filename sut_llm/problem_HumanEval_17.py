from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_beats_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual note symbols
    notes = music_string.split(' ')

    # Initialize an empty list to store the beat values
    result = []

    # Iterate through each note symbol and map it to its beat value
    for note_symbol in notes:
        # Retrieve the beat value from the map.
        # Assuming all note_symbols in the input string will be valid keys in note_beats_map.
        beats = note_beats_map[note_symbol]
        result.append(beats)

    return result