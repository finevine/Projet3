from model import *
from datetime import datetime

py.init()

# -------- SET LEVEL DIFFICULTY -----------
Sprite.LEVEL = 5 # from 4 to 8

# -------- INITIALIZE -----------
# DEFINE MAP
map = Map('Structure.csv')

# INITIALIZE PERSONS ON THE MAP
macgyver = Person('macgyver', map, (0,0))
guardian = Person('guardian',map, (0,0))
ennemies = []
ennemies_images = Sprite('personnages', map, 0, 0, 32).surfs
for i in range(len(ennemies_images)):
    ennemy = Person('ennemy', map, (0,0))
    ennemy.image = ennemies_images[i]
    ennemies.append(ennemy)

# INITIALIZE OBJECTS ON THE MAP
objects = Objects(map)
objects_pos = []
for object in objects.list:
    objects_pos.append(object.position)

# DEFINE COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# DEFINE TILES
tiles = Sprite('floor-tiles-20x20', map, 5, 0, 20)

# OPEN A NEW WINDOW
size = (15 * map.SPRITE_WIDTH, 15 * map.SPRITE_WIDTH)
screen = py.display.set_mode(size)
py.display.set_caption("Mac Gyver escapes")

# THE LOOP WILL CARRY ON UNTIL THE USER EXIT THE GAME (E.G. CLICKS THE CLOSE BUTTON).
carryOn = True
playing = True

# THE CLOCK WILL BE USED TO CONTROL HOW FAST THE SCREEN UPDATES
clock = py.time.Clock()


py.key.set_repeat(400,30)


# -------- MAIN PROGRAM LOOP -----------
while carryOn:
    # ----- MAIN EVENT LOOP -----
    keyPressed = 0
    for event in py.event.get(): # USER DID SOMETHING
        if event.type == py.QUIT: # IF USER CLICKED CLOSE
              carryOn = False # FLAG THAT WE ARE DONE SO WE EXIT THIS LOOP
        # LISTEN FOR PRESSED KEY
        else:
            # MOVE ONE BY ONE
            if event.type == py.KEYDOWN and playing:
                keyPressed = event.key
                # MOVE ENNEMIES ON THE MAP
                for ennemy in ennemies:
                    rd.seed(datetime.now())
                    ennemy_move = rd.choice([273, 274, 275, 276])
                    ennemy.move(ennemy_move, map)


    # MOVE MACGYVER ON THE MAP
    # 0 ---->  #
    # |     y  #
    # |        #
    # V  x     #
    #RÉCUPÉRER LA TOUCHE TAPÉE
    #SI LA CASE EST LIBRE:
        #ALLER SUR LA CASE
    #SINON RESTER SUR LA MÊME CASE
    (x1, y1) = macgyver.position

    # pressed = py.key.get_pressed()
    # if pressed[py.K_UP]:
    #     x2 -= 1
    # elif pressed[py.K_DOWN]:
    #     x2 += 1
    # elif pressed[py.K_RIGHT]:
    #     y2 += 1
    # elif pressed[py.K_LEFT]:
    #     y2 -= 1
    # else:
    #     pass

    if playing:
        macgyver.move(keyPressed, map)

    # MAC GYVER TAKE AN OBJECT ON THE MAP
    if macgyver.position in objects_pos:
        object_found_ind = objects_pos.index(macgyver.position)
        del(objects_pos[object_found_ind])
        del(objects.list[object_found_ind])

    # ----- DRAWING CODE SHOULD GO HERE -----
    # FIRST, CLEAR THE SCREEN TO WHITE.
    screen.fill(BLACK)

    # REDRAW MAP
    for tuple in map.free_cells:
        rd.seed(tuple[1]/(tuple[0]+1))
        screen.blit(tiles.surfs[rd.randint(0, 3)], (tuple[1] * map.SPRITE_WIDTH , tuple[0] * map.SPRITE_WIDTH))
        #py.draw.rect(screen, BLACK, [tuple[1] * map.SPRITE_WIDTH , tuple[0] * map.SPRITE_WIDTH, map.SPRITE_WIDTH, map.SPRITE_WIDTH],0)

    # REDRAW PERSONS
    screen.blit(guardian.image, (guardian.position[1] * map.SPRITE_WIDTH , guardian.position[0] * map.SPRITE_WIDTH))
    screen.blit(macgyver.image, (macgyver.position[1] * map.SPRITE_WIDTH , macgyver.position[0] * map.SPRITE_WIDTH))
    for ennemy in ennemies:
        screen.blit(ennemy.image, (ennemy.position[1] * map.SPRITE_WIDTH , ennemy.position[0] * map.SPRITE_WIDTH))

    # REDRAW OBJECT ON THE MAP
    for object in objects.list:
        screen.blit(object.image, (object.position[1] * map.SPRITE_WIDTH , object.position[0] * map.SPRITE_WIDTH))

    dist_from_ennemies = [np.linalg.norm(np.array(macgyver.position) - np.array(guardian.position))]
    for ennemy in ennemies:
        dist_from_ennemies.append(np.linalg.norm(np.array(macgyver.position) - np.array(ennemy.position)))

    # MAC GYVER WIN OR DIE
    if min(dist_from_ennemies) <= 1.0:
        playing = False
        if objects.list == [] and np.linalg.norm(np.array(macgyver.position) - np.array(guardian.position)) == 1:
            py.display.set_caption("IT'S A WIN!")

            # DISPLAY WIN SPLASH SCREEN
            you_win = py.image.load('ressource/you_win.png')
            you_win = py.transform.scale(you_win,(int(screen.get_width() / 2), int(screen.get_width() / 2)))
            screen.blit(
                you_win,
                (screen.get_width() / 2 - you_win.get_width() / 2 , screen.get_height() / 2 - you_win.get_height() / 2)
            )
        else:
            py.display.set_caption("YOU DIE!")

            # DISPLAY LOOSE SPLASH SCREEN
            you_lose = py.image.load('ressource/you_lose.png')
            you_lose = py.transform.scale(you_lose,(int(screen.get_width() / 2), int(screen.get_width() / 2)))
            screen.blit(
                you_lose,
                (screen.get_width() / 2 - you_lose.get_width() / 2 , screen.get_height() / 2 - you_lose.get_height() / 2)
            )

    # --- GO AHEAD AND UPDATE THE SCREEN WITH WHAT WE'VE DRAWN. ---
    py.display.flip()

    # --- LIMIT TO 60 FRAMES PER SECOND ---
    clock.tick(60)

# ONCE WE HAVE EXITED THE MAIN PROGRAM LOOP WE CAN STOP THE GAME ENGINE:
py.quit()
