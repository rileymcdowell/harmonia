
from harmonia.model.chord import Chord
from harmonia.model.scale import Scale
from harmonia.analysis.scale_finder import find_scales

def generate_report(chords, scales):
    _0 = "Analysis Report"
    _1 = "==============="
    _2 = "Chords:"
    _3 = " -> ".join([c.name for c in chords])
    _4 = "==============="

    rest = []
    for note, mode in scales:
        rest.append("Scale: {} {}".format(note, mode))
        rest.append("===============")

    report = [_0, _1, _2, _3]

    return '\n'.join(report + rest)

def conduct_analysis(input_tokens):
    chords = [Chord(x) for x in input_tokens]
    scales = find_scales(chords)
    return generate_report(chords, scales)

