import numpy as np

class Map:

    SPRITE_WIDTH = 20

    """arg = csv with 0, 1, 2, 3 with separator ;"""
    def __init__(self, map, tile_size):
        #empty list
        self.skl = np.genfromtxt(map, delimiter=';')
        self.tile_size = tile_size

    @classmethod
    def display(cls):
        pass

class Person:
    def __init__(self, type, map):
        self.type = type
        self.position = position
        if type == mcgyver:
            self.position = np.where(map.skl == 2)
        elif type == guardian:
            self.position = np.where(map.skl == 3)

    @classmethod
    def initialize(cls):
        #position
        pass

    def move(cls):
        #die
        #take
        pass

class Object:
    """Object type """
    def __init__(self, type, position):
        self.type = type
        self.position = position

    @classmethod
    def taken(cls):
        pass
