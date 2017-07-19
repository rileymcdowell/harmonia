import numpy
from harmonia.model.scale import Scale
from harmonia.constants import NUM_NOTES
from harmonia.constants import NAME_TO_INTERVALS, NAME_TO_RAW_NOTE

class Chord(Scale):
    def __init__(self, name):
        # Split the chord into tokens
        tokens = list(name)
        # Get the base of the note.
        base = tokens[0]
        # Check for flat/sharp notes.
        modifier = ''
        has_modifier = False
        if len(tokens) > 1 and tokens[1] in ('b', '#'):
            modifier = name[1]
            has_modifier = True

        # Grab the chord suffix without the note (the type of chord)
        start_idx = 2 if has_modifier else 1
        end_tokens = tokens[start_idx:]
        suffix = ''.join(end_tokens)

        # Save what we learned.
        self.name = name
        self.note = NAME_TO_RAW_NOTE[base + modifier]
        self.kind = NAME_TO_INTERVALS[suffix]
        # Also act like a scale keeping notes between 0 and 11 (12 note scale)
        self.notes = set((self.note + self.kind) % NUM_NOTES)

    def name(self):
        return name

    def to_scale(self):
        return Scale(self.notes)

    def __repr__(self):
        return '<Chord({}={}+{})>'.format(self.name, self.note, self.kind)
