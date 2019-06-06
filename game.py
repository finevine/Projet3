from model import *

py.init()


# -------- INITIALIZE -----------
# DEFINE MAP
map = Map('Structure2.csv')

# INITIALIZE PERSONS ON THE MAP
macgyver = Person('macgyver', map, (0,0))
guardian = Person('guardian',map, (0,0))

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
tiles = Tiles(map, 5, 0)

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
            if event.type == py.KEYDOWN:
                keyPressed = event.key

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
    (x2, y2) = macgyver.position

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

    if (x2, y2) in map.free_cells and playing:
        macgyver.move((x2,y2))
    else:
        pass

    # MAC GYVER TAKE AN OBJECT ON THE MAP
    if macgyver.position in objects_pos:
        object_found_ind = objects_pos.index(macgyver.position)
        del(objects_pos[object_found_ind])
        del(objects.list[object_found_ind])

    # MAC GYVER WIN OR DIE
    if macgyver.position == guardian.position:
        playing = False
        if objects.list == []:
            py.display.set_caption("IT'S A WIN!")
        else:
            py.display.set_caption("YOU DIE!")



    # ----- DRAWING CODE SHOULD GO HERE -----
    # FIRST, CLEAR THE SCREEN TO WHITE.
    screen.fill(BLACK)

    # REDRAW MAP
    for tuple in map.free_cells:
        rd.seed(tuple[1]/(tuple[0]+1))
        screen.blit(tiles.surfs[rd.randint(0, 3)], (tuple[1] * map.SPRITE_WIDTH , tuple[0] * map.SPRITE_WIDTH))
        #py.draw.rect(screen, BLACK, [tuple[1] * map.SPRITE_WIDTH , tuple[0] * map.SPRITE_WIDTH, map.SPRITE_WIDTH, map.SPRITE_WIDTH],0)

    # REDRAW PERSONS
    screen.blit(macgyver.image, (macgyver.position[1] * map.SPRITE_WIDTH , macgyver.position[0] * map.SPRITE_WIDTH))
    screen.blit(guardian.image, (guardian.position[1] * map.SPRITE_WIDTH , guardian.position[0] * map.SPRITE_WIDTH))

    # REDRAW OBJECT ON THE MAP
    for object in objects.list:
        screen.blit(object.image, (object.position[1] * map.SPRITE_WIDTH , object.position[0] * map.SPRITE_WIDTH))



    # --- GO AHEAD AND UPDATE THE SCREEN WITH WHAT WE'VE DRAWN. ---
    py.display.flip()

    # --- LIMIT TO 60 FRAMES PER SECOND ---
    clock.tick(60)

# ONCE WE HAVE EXITED THE MAIN PROGRAM LOOP WE CAN STOP THE GAME ENGINE:
py.quit()
