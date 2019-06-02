import numpy as np

class Map:
    """arg = csv with 0, 1, 2, 3 with separator ;"""
    def __init__(self, map, tile_size):
        #empty list
        self.skl = np.genfromtxt(map, delimiter=';')
        self.tile_size = tile_size

    @classmethod
    def display(cls):
        pass

class Object:
    """Object type """
    def __init__(self, type, position):
        self.type = type
        self.position = position

    @classmethod
    def taken(cls):
        pass

class Person:
    def __init__(self, type, position, dress, map):
        self.type = type
        self.position = position
        self.dress = dress

    @classmethod
    def initialize(cls):
        #position
        #dress
        pass

    def move(cls):
        #wounded/die
        #take
        pass
