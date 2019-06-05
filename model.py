import numpy as np

class Map:

    SPRITE_WIDTH = 20

    @property
    def free_cells(self):
        free_cells_index = np.where(self.skl > 0)
        return list(zip(free_cells_index[0], free_cells_index[1]))

    """arg = csv with 0, 1, 2, 3 with separator ;"""
    def __init__(self, map):
        self.skl = np.genfromtxt(map, delimiter=';')

    def display(cls):
        pass

class Person:
    def __init__(self, type, map, position):
        self.type = type
        a = 1
        if type == 'macgyver':
            a = 2 # PAR CONVENTION
        elif type == 'guardian':
            a = 3 # PAR CONVENTION
        self.position = (np.where(map.skl == a)[0][0], np.where(map.skl == a)[1][0])

    def move(self, pos2):
        (x1, y1) = self.position
        (x2, y2) = pos2
        #SI POS2 EST ACCESSIBLE:
        if ((abs(x1-x2), abs(y1-y2)) in [(1,0), (0,1), (0,0)]):
            self.position = pos2
            print(pos2)
        else:
            print('Error')

class Object:
    """Object type """
    def __init__(self, type, position):
        self.type = type
        self.position = position

    @classmethod
    def initialize(cls):
        pass
