from model import *

def play_game(level, life_num):
    # -------- SET LEVEL DIFFICULTY -----------
    # level = input("How many ennemies (0 to 10) ? ")
    # while int(level) not in range(11):
    #     level = input("Ennemies must be between 0 and 10 : ")
    Sprite.LEVEL = int(level) # from 0 to 10

    py.init()

    # -------- INITIALIZE -----------
    # DEFINE MAP
    map = Map('structures/Structure'+str(level)+'.csv')

    # OPEN A NEW WINDOW
    size = (15 * map.SPRITE_WIDTH, 15 * map.SPRITE_WIDTH)
    screen = py.display.set_mode(size)
    py.display.set_caption("Mac Gyver escapes")
    # CLEAR THE SCREEN TO BLACK.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(BLACK)

    # DRAW MAP WITH TILES
    tiles = Sprite('floor-tiles-20x20', map, 5, 0, 20)
    map.draw(tiles, screen)
    font = py.font.Font('ressource/ARCADECLASSIC.ttf', 25)
    level_text = font.render('L '+str(level), 0, WHITE)
    level_text_Rect = level_text.get_rect()

    # INITIALIZE PERSONS ON THE MAP
    macgyver = Person('macgyver', map, (0,0))
    guardian = Person('guardian',map, (0,0))
    ennemies = []
    ennemies_images = Sprite('personnages', map, 0, 0, 32).surfs
    for i in range(len(ennemies_images)):
        ennemy = Person('ennemy', map, (0,0))
        while ennemy.distance(macgyver) <= 1: # NOT TO LOOSE AT THE BEGINNING OF GAME
            ennemy = Person('ennemy', map, (0,0))
        ennemy.image = ennemies_images[i]
        ennemies.append(ennemy)

    # INITIALIZE OBJECTS ON THE MAP
    objects = Objects(map)
    objects_pos = [object.position for object in objects.list]

    # THE LOOP WILL CARRY ON UNTIL THE USER EXIT THE GAME.
    carryOn = True # WHILE NOT QUIT
    playing = True # WHILE NOT WIN AND NOT LOOSE
    update = True # WHEN KEY PRESSED
    win = False
    loose = False

    # THE CLOCK WILL BE USED TO CONTROL HOW FAST THE SCREEN UPDATES
    clock = py.time.Clock()
    py.key.set_repeat(400,30)


    # ----------------------------------- MAIN PROGRAM LOOP -----------
    while carryOn:
        keyPressed = 0
        for event in py.event.get(): # USER DID SOMETHING
            if event.type == py.QUIT or py.key.get_pressed()[py.K_ESCAPE]: # IF USER CLICKED CLOSE
                  carryOn = False # FLAG THAT WE ARE DONE SO WE EXIT THIS LOOP
                  return 'quit'
            # LISTEN FOR PRESSED KEY
            elif event.type == py.KEYDOWN:
                keyPressed = event.key
                update = True
                if win:
                    return 'win'
                elif loose:
                    return 'loose'
        # ------------------------------- EVENTS -----
        if update:
            # MOVE ENNEMIES ON THE MAP
            for ennemy in ennemies:
                (x, y) = ennemy.position
                rd.seed(datetime.now())
                ennemy_move = rd.choice([273, 274, 275, 276])
                ennemy.move(ennemy_move, map)
                # UPDATE LAST POSITION
                tiles.draw_sprite(map.decoration[(x, y)], screen, x * map.SPRITE_WIDTH, y * map.SPRITE_WIDTH)

            # MOVE MACGYVER ON THE MAP
            (x1, y1) = macgyver.position
            if playing:
                macgyver.move(keyPressed, map)
            # UPDATE LAST POSITION
            tiles.draw_sprite(map.decoration[(x1,y1)], screen, x1 * map.SPRITE_WIDTH, y1 * map.SPRITE_WIDTH)

            # ----------------------------- DRAWING CODE GOES HERE -----
            # DRAW OBJECT ON THE MAP
            for object in objects.list:
                object.draw_object(screen, object.position[0] * map.SPRITE_WIDTH, object.position[1] * map.SPRITE_WIDTH)

            # REDRAW PERSONS
            guardian.draw_person(
                screen, guardian.position[0] * map.SPRITE_WIDTH , guardian.position[1] * map.SPRITE_WIDTH)
            macgyver.draw_person(
                screen, macgyver.position[0] * map.SPRITE_WIDTH , macgyver.position[1] * map.SPRITE_WIDTH)
            for ennemy in ennemies:
                ennemy.draw_person(
                    screen, ennemy.position[0] * map.SPRITE_WIDTH , ennemy.position[1] * map.SPRITE_WIDTH)

            # REDRAW LIVES & LEVEL
            heart = py.transform.scale(py.image.load('ressource/heart.png'),(int(map.SPRITE_WIDTH/2), int(map.SPRITE_WIDTH/2)))
            for i in range(life_num):
                screen.blit(heart, (20 * i + 10, 5))
            screen.blit(level_text, (screen.get_width() - level_text_Rect.width-10, 5))

            # MAC GYVER TAKE AN OBJECT ON THE MAP
            if macgyver.position in objects_pos:
                # GET INDEX OF OBJECT
                object_found_ind = objects_pos.index(macgyver.position)
                # CLEAR POSITION ON THE MAP
                del(objects_pos[object_found_ind])
                # CLEAR OBJECT FROM OBJECTS LIST
                del(objects.list[object_found_ind])

            # COMPUTE DISTANCE FROM ENNEMIES
            dist_from_ennemies = [macgyver.distance(guardian)] + [macgyver.distance(ennemy) for ennemy in ennemies]

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

# ONCE WE HAVE EXITED THE MAIN PROGRAM LOOP WE CAN STOP THE GAME ENGINE:
py.quit()
