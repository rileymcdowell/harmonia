import numpy as np

NAME_TO_RAW_NOTE = { 'A' : 0
                   , 'A#': 1
                   , 'Bb': 1
                   , 'B' : 2
                   , 'C' : 3
                   , 'C#': 4
                   , 'Db': 4
                   , 'D' : 5
                   , 'D#': 6
                   , 'Eb': 6
                   , 'E' : 7
                   , 'F' : 8
                   , 'F#': 9
                   , 'Gb': 9
                   , 'G' : 10 
                   , 'G#': 11
                   , 'Ab': 11
                   }

RAW_NOTE_TO_NAME = { 0: 'A'
                   , 1: 'Bb'
                   , 2: 'B'
                   , 3: 'C'
                   , 4: 'Db'
                   , 5: 'D'
                   , 6: 'Eb'
                   , 7: 'E'
                   , 8: 'F'
                   , 9: 'Gb'
                   , 10: 'G'
                   , 11: 'Ab'
                   }

# Encode chord intervals relative to the root.
maj  = np.array([0,  4,  7])
min  = np.array([0,  3,  7])
b5   = np.array([0,  4,  6])
dim  = np.array([0,  3,  6])
aug  = np.array([0,  4,  8])
_7   = np.array([0,  4,  7, 10])
m7   = np.array([0,  3,  7, 10])
dim7 = np.array([0,  3,  6,  9])
maj7 = np.array([0,  4,  7, 11])
aug7 = np.array([0,  4,  8, 10])

NAME_TO_INTERVALS = { '': maj, 'maj': maj # Major
                    , 'm': min, 'min': min # Minor
                    , 'b5': b5, 'dim': dim # Diminished
                    , '7': _7, 'min7': m7, 'm7': m7, 'M7': maj7, 'maj7': maj7 # The 7s
                    , 'dim7': dim7, 'aug': aug, 'aug7': aug # The wierdos
                    }

NUM_NOTES = 12
RAW_NOTES = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

IONIAN     = np.array([0, 2, 4, 5, 7, 9, 11])
DORIAN     = np.array([0, 2, 3, 5, 7, 9, 10])
PHRYGIAN   = np.array([0, 1, 3, 5, 7, 8, 10])
LYDIAN     = np.array([0, 2, 4, 6, 7, 9, 11])
MIXOLYDIAN = np.array([0, 2, 4, 5, 7, 9, 10])
AEOLIAN    = np.array([0, 2, 3, 5, 7, 8, 10])
LOCRIAN    = np.array([0, 1, 3, 5, 6, 8, 10])


