from datetime import datetime
from random import seed, randint
import numpy as np
import pygame as py

class Map:
    '''ARG = CSV WITH 0, 1, 2, 3 WITH SEPARATOR ";"'''
    SPRITE_WIDTH = 30

    def __init__(self, game_map):
        self.skl = np.nan_to_num((np.genfromtxt(game_map, delimiter=';')))

    @property
    def free_cells(self):
        '''Define cells that are accessibles'''
        free_cells_index = np.where(self.skl > 0)
        return list(zip(free_cells_index[0], free_cells_index[1]))

    @property
    def decoration(self):
        ''' Define tiles decoration for free_cells'''
        seed(1)
        return {c: randint(0, 2) for c in self.free_cells}

    @property
    def classic_cells(self):
        classic_cells_index = np.where(self.skl == 1)
        return list(zip(classic_cells_index[0], classic_cells_index[1]))

    def draw(self, sprites, screen):
        assert len(sprites.surfs) >= 3, 'pas assez de tuiles'
        for tuple in self.free_cells:
            # DRAW A RANDOM TILE AMONGST 3 OF THEM
            sprites.draw_sprite(self.decoration[(tuple[0], tuple[1])],
                                screen, tuple[0] * self.SPRITE_WIDTH,
                                tuple[1] * self.SPRITE_WIDTH)


class Person:
    ''' POSITION OF THE PERSON DEPEND OF ITS TYPE BY CONSTRUCTION OF THE MAP '''

    def __init__(self, kind, game_map):
        self.kind = kind
        csv_num = 1
        place = 0
        if kind == 'macgyver':
            csv_num = 2 # BY CONVENTION
        elif kind == 'guardian':
            csv_num = 3 # BY CONVENTION
        elif kind == 'ennemy':
            csv_num = 1
            seed(datetime.now())
            place = randint(0, len(np.where(game_map.skl == csv_num)[0]) - 1)

        self.position = (np.where(game_map.skl == csv_num)[0][place],
                         np.where(game_map.skl == csv_num)[1][place])
        if kind != 'ennemy':
            self.image = py.transform.scale(py.image.load('ressource/'+kind+'.png'),
                                            (game_map.SPRITE_WIDTH, game_map.SPRITE_WIDTH))

    def move(self, keyPressed, game_map):
        '''Define Movement of the personn depending on Keypressed'''
            # 0 ---->  #
            # |     y  #
            # |        #
            # V  x     #
        (x_1, y_1) = self.position
        (x_2, y_2) = (x_1, y_1)
        if keyPressed == py.K_UP:
            x_2 -= 1
        elif keyPressed == py.K_DOWN:
            x_2 += 1
        elif keyPressed == py.K_RIGHT:
            y_2 += 1
        elif keyPressed == py.K_LEFT:
            y_2 -= 1
        else:
            pass
        #SI x2, y2 EST ACCESSIBLE:
        move_not_too_long = ((abs(x_1-x_2), abs(y_1-y_2)) in [(1, 0), (0, 1), (0, 0)])
        if move_not_too_long and (x_2, y_2) in game_map.free_cells:
            self.position = (x_2, y_2)

    def draw_person(self, screen, x_pers, y_pers):
        '''draw person on the screen parameter'''
        screen.blit(self.image, (y_pers, x_pers))

    def distance(self, person2):
        '''compute the distance between 2 persons'''
        return np.linalg.norm(np.array(self.position) - np.array(person2.position))


class Ennemy:
    def __init__(self, position, image):
        '''initialize ennemy Person'''
        self.position = position
        self.image = image


class Object:
    '''define an object depending on kind of object it is'''
    def __init__(self, kind, position, image):
        self.kind = kind
        self.position = position
        self.image = image

    def draw_object(self, screen, x_obj, y_obj):
        '''need to depend on the game_map since it is erased if a Person step on the obect'''
        screen.blit(self.image, (y_obj, x_obj))


class Objects:
    '''OBJECT TYPE HAS AN ATTRIBUTE LIST OF OBJECTS THAT DEPEND ON THE MAP GIVEN IN ARGUMENT '''
    TYPES = ['ether', 'needle', 'plastictube', 'sting']

    def __init__(self, game_map):
        liste = []
        for kind in self.TYPES:
            classic_cells = game_map.classic_cells
            rand_int = randint(0, len(classic_cells) - 1)
            position = classic_cells.pop(rand_int)
            image = py.transform.scale(py.image.load('ressource/'+kind+'.png'),
                                       (game_map.SPRITE_WIDTH, game_map.SPRITE_WIDTH))
            liste.append(Object(kind, position, image))
        self.list = liste


class Sprite:
    '''Sprite are 3 tiles in a row in the ressource folder
    OR Ennemies in the "personnages.png" image
    They can also be Macgyver, or the guardian'''
    LEVEL = 3

    def __init__(self, kind, game_map, pos, width):
        (row, col) = pos
        img = py.image.load('ressource/'+kind+'.png')
        surfs = []
        if kind == 'floor-tiles-20x20':
            sprite_num = 3
        else:
            sprite_num = self.LEVEL
        for i in range(sprite_num):
            tile = img.subsurface((row + i) * width, (col) * width, width, width)
            surfs.append(py.transform.scale(tile, (game_map.SPRITE_WIDTH, game_map.SPRITE_WIDTH)))
        self.surfs = surfs

    def draw_sprite(self, num, screen, x_sprite, y_sprite):
        '''draw a sprite'''
        screen.blit(self.surfs[num], (y_sprite, x_sprite))

def end_print(result, message, screen):
    ''' for printing the splash screen at the end of game'''
    white = (255, 255, 255)
    result = py.image.load('ressource/'+result+'.png')
    result = py.transform.scale(result, (int(screen.get_width() / 2), int(screen.get_width() / 2)))
    font = py.font.Font('ressource/ARCADECLASSIC.ttf', 25)
    level_text = font.render(message, 0, white)
    level_text_rect = level_text.get_rect()
    screen.blit(
        result,
        (screen.get_width() / 2 - result.get_width() / 2,
         screen.get_height() / 2 - result.get_height() / 2)
    )
    screen.blit(
        level_text,
        (screen.get_width() / 2 - level_text_rect.width / 2,
         6 * screen.get_height() / 8 +10)
    )
