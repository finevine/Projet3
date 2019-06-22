'''
A round of the game used in the game.py
it uses model.py for the classes
'''
from random import seed, choice
from datetime import datetime
import pygame as py
from model import Map, Person, Objects, Sprite, end_print

def play_game(level, life_num):
    ''' Here is the play_game function'''
    # -------- SET LEVEL DIFFICULTY -----------
    # level = input("How many ennemies (0 to 10) ? ")
    # while int(level) not in range(11):
    #     level = input("Ennemies must be between 0 and 10 : ")
    Sprite.LEVEL = int(level) # from 0 to 10

    # -------- INITIALIZE -----------
    # DEFINE MAP
    map_game = Map('structures/Structure'+str(level)+'.csv')

    # OPEN A NEW WINDOW
    size = (15 * map_game.SPRITE_WIDTH, 15 * map_game.SPRITE_WIDTH)
    screen = py.display.set_mode(size)
    py.display.set_caption("Mac Gyver escapes")
    # CLEAR THE SCREEN TO black.
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen.fill(black)

    # DRAW MAP WITH TILES
    tiles = Sprite('floor-tiles-20x20', map_game, (5, 0), 20)
    map_game.draw(tiles, screen)
    font = py.font.Font('ressource/ARCADECLASSIC.ttf', 25)
    level_text = font.render('L '+str(level), 0, white)
    level_text_rect = level_text.get_rect()

    # INITIALIZE PERSONS ON THE MAP
    macgyver = Person('macgyver', map_game)
    guardian = Person('guardian', map_game)
    ennemies = []
    ennemies_images = Sprite('personnages', map_game, (0, 0), 32).surfs
    for i in range(len(ennemies_images)):
        ennemy = Person('ennemy', map_game)
        while ennemy.distance(macgyver) <= 1: # NOT TO LOOSE AT THE BEGINNING OF GAME
            ennemy = Person('ennemy', map_game)
        ennemy.image = ennemies_images[i]
        ennemies.append(ennemy)

    # INITIALIZE OBJECTS ON THE MAP
    objects = Objects(map_game)
    objects_pos = [object.position for object in objects.list]

    # THE LOOP WILL CARRY ON UNTIL THE USER EXIT THE GAME.
    carry_on = True # WHILE NOT QUIT
    playing = True # WHILE NOT WIN AND NOT LOOSE
    update = True # WHEN KEY PRESSED
    win = False
    loose = False

    # THE CLOCK WILL BE USED TO CONTROL HOW FAST THE SCREEN UPDATES
    clock = py.time.Clock()
    py.key.set_repeat(400, 30)


    # ----------------------------------- MAIN PROGRAM LOOP -----------
    while carry_on:
        key_pressed = 0
        for event in py.event.get(): # USER DID SOMETHING
            if event.type == py.QUIT or py.key.get_pressed()[py.K_ESCAPE]: # IF USER CLICKED CLOSE
                carry_on = False # FLAG THAT WE ARE DONE SO WE EXIT THIS LOOP
                return 'quit'
            # LISTEN FOR PRESSED KEY
            if event.type == py.KEYDOWN:
                key_pressed = event.key
                update = True
                if win:
                    return 'win'
                if loose:
                    return 'loose'
        # ------------------------------- EVENTS -----
        if update:
            # MOVE ENNEMIES ON THE MAP
            for ennemy in ennemies:
                (x_en, y_en) = ennemy.position
                seed(datetime.now())
                ennemy_move = choice([273, 274, 275, 276])
                ennemy.move(ennemy_move, map_game)
                # UPDATE LAST POSITION
                tiles.draw_sprite(map_game.decoration[(x_en, y_en)], screen,
                                  x_en * map_game.SPRITE_WIDTH, y_en * map_game.SPRITE_WIDTH)

            # MOVE MACGYVER ON THE MAP
            (x_mac1, y_mac1) = macgyver.position
            if playing:
                macgyver.move(key_pressed, map_game)
            # UPDATE LAST POSITION
            tiles.draw_sprite(map_game.decoration[(x_mac1, y_mac1)],
                              screen,
                              x_mac1 * map_game.SPRITE_WIDTH,
                              y_mac1 * map_game.SPRITE_WIDTH)

            # ----------------------------- DRAWING CODE GOES HERE -----
            # DRAW OBJECT ON THE MAP
            for stuff in objects.list:
                stuff.draw_object(screen, stuff.position[0] * map_game.SPRITE_WIDTH,
                                  stuff.position[1] * map_game.SPRITE_WIDTH)

            # REDRAW PERSONS
            guardian.draw_person(
                screen, guardian.position[0] * map_game.SPRITE_WIDTH,
                guardian.position[1] * map_game.SPRITE_WIDTH)
            macgyver.draw_person(
                screen, macgyver.position[0] * map_game.SPRITE_WIDTH,
                macgyver.position[1] * map_game.SPRITE_WIDTH)
            for ennemy in ennemies:
                ennemy.draw_person(
                    screen, ennemy.position[0] * map_game.SPRITE_WIDTH,
                    ennemy.position[1] * map_game.SPRITE_WIDTH)

            # REDRAW LIVES & LEVEL
            heart = py.transform.scale(py.image.load('ressource/heart.png'),
                                       (int(map_game.SPRITE_WIDTH/2), int(map_game.SPRITE_WIDTH/2)))
            for i in range(life_num):
                screen.blit(heart, (20 * i + 10, 5))
            screen.blit(level_text, (screen.get_width() - level_text_rect.width-10, 5))

            # MAC GYVER TAKE AN OBJECT ON THE MAP
            if macgyver.position in objects_pos:
                # GET INDEX OF OBJECT
                object_found_ind = objects_pos.index(macgyver.position)
                # CLEAR POSITION ON THE MAP
                del objects_pos[object_found_ind]
                # CLEAR OBJECT FROM OBJECTS LIST
                del objects.list[object_found_ind]

            # COMPUTE DISTANCE FROM ENNEMIES
            dist_from_ennemies = [macgyver.distance(ennemy) for ennemy in ennemies]
            dist_from_ennemies.append(macgyver.distance(guardian))

            # MAC GYVER WIN OR DIE
            if min(dist_from_ennemies) <= 1.0:
                playing = False
                if objects.list == [] and macgyver.distance(guardian) == 1:
                    py.display.set_caption("IT'S A WIN!")
                    end_print('you_win', 'Press any key to continue', screen)
                    win = True
                else:
                    if life_num == 1:
                        message = 'GAME OVER'
                    else:
                        message = 'Press any key to continue'
                    py.display.set_caption("YOU DIE!")
                    end_print('you_lose', message, screen)
                    loose = True

            # --- GO AHEAD AND UPDATE THE SCREEN WITH WHAT WE'VE DRAWN. ---
            py.display.flip()
        update = False
        # --- LIMIT TO 60 FRAMES PER SECOND ---
        clock.tick(60)
