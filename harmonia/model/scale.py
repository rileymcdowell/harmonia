import numpy as np

class Scale(object):
    def __init__(self, notes=None):
        self.notes = set() if notes is None else notes
        assert isinstance(notes, set)

    def __add__(self, other):
        both = self.notes.union(other.notes)
        return Scale(both)

    def to_scale(self):
        """ Useful for base classes to override """
        return self 

    def __repr__(self):
        return "<Scale({})>".format(np.array(self.notes))
