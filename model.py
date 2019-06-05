import numpy as np
import pygame
import random

class Map:
    '''ARG = CSV WITH 0, 1, 2, 3 WITH SEPARATOR ;'''

    SPRITE_WIDTH = 20

    def __init__(self, map):
        self.skl = np.genfromtxt(map, delimiter=';')

    @property
    def free_cells(self):
        free_cells_index = np.where(self.skl > 0)
        return list(zip(free_cells_index[0], free_cells_index[1]))

    @property
    def classic_cells(self):
        classic_cells_index = np.where(self.skl == 1)
        return list(zip(classic_cells_index[0], classic_cells_index[1]))

class Person:
    ''' POSITION OF THE PERSON DEPEND OF ITS TYPE BY CONSTRUCTION OF THE MAP '''

    def __init__(self, type, map, position):
        self.type = type
        a = 1
        if type == 'macgyver':
            a = 2 # PAR CONVENTION
        elif type == 'guardian':
            a = 3 # PAR CONVENTION
        self.position = (np.where(map.skl == a)[0][0], np.where(map.skl == a)[1][0])
        self.image = pygame.transform.scale(pygame.image.load('ressource/'+type+'.png'),(map.SPRITE_WIDTH, map.SPRITE_WIDTH))

    def move(self, pos2):
        (x1, y1) = self.position
        (x2, y2) = pos2
        #SI POS2 EST ACCESSIBLE:
        if ((abs(x1-x2), abs(y1-y2)) in [(1,0), (0,1), (0,0)]):
            self.position = pos2
            # FOR TESTING print(pos2)
        else:
            print('Error')

class Object:

    def __init__(self, type, position, image):
        self.type = type
        self.position = position
        self.image = image

class Objects:
    '''OBJECT TYPE HAS AN ATTRIBUTE LIST OF OBJECTS THAT DEPEND ON THE MAP GIVEN IN ARGUMENT '''

    TYPES = ['ether', 'needle', 'plastictube', 'sting']

    def __init__(self, map):
        list = []
        for type in self.TYPES:
            classic_cells = map.classic_cells
            rand_int = random.randint(0, len(classic_cells) - 1)
            position = classic_cells.pop(rand_int)
            image = pygame.transform.scale(pygame.image.load('ressource/'+type+'.png'),(map.SPRITE_WIDTH, map.SPRITE_WIDTH))
            list.append(Object(type, position, image))
        self.list = list
