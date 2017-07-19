from operator import add
from functools import reduce

from harmonia.constants import IONIAN, DORIAN, PHRYGIAN, LYDIAN, MIXOLYDIAN, AEOLIAN, LOCRIAN
from harmonia.constants import RAW_NOTES, RAW_NOTE_TO_NAME, NUM_NOTES

MODES = [IONIAN, DORIAN, PHRYGIAN, LYDIAN, MIXOLYDIAN, AEOLIAN, LOCRIAN]
MODE_NAMES = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']

def find_scales(chords):
    this_scale = reduce(add, chords)

    to_return = []

    # Identify the scales containing those notes.
    for note in RAW_NOTES:
        for mode_name, mode_intervals in zip(MODE_NAMES, MODES):
            mode_scale = (mode_intervals + note) % NUM_NOTES
            if this_scale.notes.issubset(mode_scale):
                # We've found a candidate scale for the notes.
                root_name = RAW_NOTE_TO_NAME[note]
                to_return.append((root_name, mode_name))

   
    return to_return

