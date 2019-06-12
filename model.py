import numpy as np
import pygame as py
import random as rd
from datetime import datetime

class Map:
    '''ARG = CSV WITH 0, 1, 2, 3 WITH SEPARATOR ";"'''
    SPRITE_WIDTH = 30

    def __init__(self, map):
        self.skl = np.nan_to_num((np.genfromtxt(map, delimiter=';')))

    @property
    def free_cells(self):
        free_cells_index = np.where(self.skl > 0)
        return list(zip(free_cells_index[0], free_cells_index[1]))

    @property
    def decoration(self):
        rd.seed(1)
        return {c: rd.randint(0, 2) for c in self.free_cells}

    @property
    def classic_cells(self):
        classic_cells_index = np.where(self.skl == 1)
        return list(zip(classic_cells_index[0], classic_cells_index[1]))

    def draw(self, sprites, screen):
        assert len(sprites.surfs) >=3, 'pas assez de tuiles'
        for tuple in self.free_cells:
            # DRAW A RANDOM TILE AMONGST 3 OF THEM
            sprites.draw_sprite(self.decoration[(tuple[0], tuple[1])], screen, tuple[0] * self.SPRITE_WIDTH , tuple[1] * self.SPRITE_WIDTH)

class Person:
    ''' POSITION OF THE PERSON DEPEND OF ITS TYPE BY CONSTRUCTION OF THE MAP '''

    def __init__(self, type, map, position):
        self.type = type
        a = 1
        place = 0
        if type == 'macgyver':
            a = 2 # PAR CONVENTION
        elif type == 'guardian':
            a = 3 # PAR CONVENTION
        elif type == 'ennemy':
            a = 1
            rd.seed(datetime.now())
            place = rd.randint(0, len(np.where(map.skl == a)[0]-1))

        self.position = (np.where(map.skl == a)[0][place], np.where(map.skl == a)[1][place])
        if type != 'ennemy':
            self.image = py.transform.scale(py.image.load('ressource/'+type+'.png'),(map.SPRITE_WIDTH, map.SPRITE_WIDTH))

    def move(self, keyPressed, map):
            # 0 ---->  #
            # |     y  #
            # |        #
            # V  x     #
        (x1, y1) = self.position
        (x2, y2) = (x1, y1)
        if keyPressed == 273:
            x2 -= 1
        elif keyPressed == 274:
            x2 += 1
        elif keyPressed == 275:
            y2 += 1
        elif keyPressed == 276:
            y2 -= 1
        else:
            pass
        #SI x2, y2 EST ACCESSIBLE:
        if ((abs(x1-x2), abs(y1-y2)) in [(1,0), (0,1), (0,0)]) and (x2, y2) in map.free_cells:
            self.position = (x2, y2)

    def draw_person(self, screen, x, y):
        screen.blit(self.image, (y, x))

    def distance(self, person2):
        return np.linalg.norm(np.array(self.position) - np.array(person2.position))

    def take(self, object):
        pass

class Ennemy:
    def __init__(self, position, image):
        self.type = type
        self.position = position
        self.image = image

class Object:

    def __init__(self, type, position, image):
        self.type = type
        self.position = position
        self.image = image

    def draw_object(self, screen, x, y):
        '''need to depend on the map since it is erased if a Person step on the obect'''
        screen.blit(self.image, (y, x))

class Objects:
    '''OBJECT TYPE HAS AN ATTRIBUTE LIST OF OBJECTS THAT DEPEND ON THE MAP GIVEN IN ARGUMENT '''

    TYPES = ['ether', 'needle', 'plastictube', 'sting']

    def __init__(self, map):
        list = []
        for type in self.TYPES:
            classic_cells = map.classic_cells
            rand_int = rd.randint(0, len(classic_cells) - 1)
            position = classic_cells.pop(rand_int)
            image = py.transform.scale(py.image.load('ressource/'+type+'.png'),(map.SPRITE_WIDTH, map.SPRITE_WIDTH))
            list.append(Object(type, position, image))
        self.list = list

class Sprite:
    LEVEL = 3

    def __init__(self, type, map, row, col, width):
        img = py.image.load('ressource/'+type+'.png')
        surfs = []
        if type =='floor-tiles-20x20':
            r = 3
        else:
            r = self.LEVEL
        for i in range(r):
            tile = img.subsurface((row + i) * width, (col) * width, width, width)
            surfs.append(py.transform.scale(tile,(map.SPRITE_WIDTH, map.SPRITE_WIDTH)))
        self.surfs = surfs

    def draw_sprite(self, n, screen, x, y):
        screen.blit(self.surfs[n], (y, x))

def end_print(result, screen):
    result = py.image.load('ressource/'+result+'.png')
    result = py.transform.scale(result,(int(screen.get_width() / 2), int(screen.get_width() / 2)))
    return screen.blit(
        result,
        (screen.get_width() / 2 - result.get_width() / 2 , screen.get_height() / 2 - result.get_height() / 2)
    )
