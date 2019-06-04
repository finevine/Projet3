import numpy as np

class Map:

    SPRITE_WIDTH = 20

    """arg = csv with 0, 1, 2, 3 with separator ;"""
    def __init__(self, map):
        self.skl = np.genfromtxt(map, delimiter=';')

    def display(cls):
        pass

class Person:
    def __init__(self, type, map, position):
        self.type = type
        if type == 'macgyver':
            self.position = np.where(map.skl == 2)
        elif type == 'guardian':
            self.position = np.where(map.skl == 3)

    def move(self, pos2):
        x1 = self.position[0]
        y1 = self.position[1]
        x2 = pos2[0]
        y2 = pos2[1]
        if (abs(x1-x2), abs(y1-y2)) in [(1,0), (0,1), (0,0)]:
            print(self.position)
        else:
            print('Error')
        #SI POS2 EST ACCESSIBLE:
            #SELF.POSITION = POS2
        #ELSE:
            #PASS

class Object:
    """Object type """
    def __init__(self, type, position):
        self.type = type
        self.position = position

    @classmethod
    def initialize(cls):
        pass
