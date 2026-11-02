import numpy as np

class UniformModel:
    def get_probabilities(self, _):
        return np.ones(4) / 4

class Model:
    def __init__(self):
        self._table = {}
        self._increment = 10

    def get_probabilities(self, pattern):
        if pattern not in self._table:
            self._table[pattern] = np.ones(4)

        return self._table[pattern] / np.sum(self._table[pattern])
    
    def update(self, path):
        pass