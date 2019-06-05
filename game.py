from model import *
import pygame

pygame.init()

# DEFINE MAP
map = Map('Structure.csv')
print(map.free_cells)

# INITIALIZE PERSONS ON THE MAP
macgyver = Person('macgyver', map, (0,0))
guardian = Person('guardian',map, (0,0))

# DEFINE SOME COLORS
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# OPEN A NEW WINDOW
size = (15 * map.SPRITE_WIDTH, 15 * map.SPRITE_WIDTH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mac Gyver escapes")

# THE LOOP WILL CARRY ON UNTIL THE USER EXIT THE GAME (E.G. CLICKS THE CLOSE BUTTON).
carryOn = True

# THE CLOCK WILL BE USED TO CONTROL HOW FAST THE SCREEN UPDATES
clock = pygame.time.Clock()

# -------- MAIN PROGRAM LOOP -----------
while carryOn:
    # --- MAIN EVENT LOOP
    keyPressed = 0
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        #
        # MON TEST
        else:
            if event.type == pygame.KEYDOWN:
                keyPressed = event.key

    # --- DRAWING CODE SHOULD GO HERE
    # FIRST, CLEAR THE SCREEN TO WHITE.
    screen.fill(WHITE)

    # DRAW MAP
    free_cells_index = np.where(map.skl > 0)
    free_cells = list(zip(free_cells_index[0], free_cells_index[1]))
    for tuple in free_cells:
        pygame.draw.rect(screen, BLACK, [tuple[1] * map.SPRITE_WIDTH , tuple[0] * map.SPRITE_WIDTH, map.SPRITE_WIDTH, map.SPRITE_WIDTH],0)

    # DRAW PERSONS
    pygame.draw.rect(screen, GREEN, [macgyver.position[1] * map.SPRITE_WIDTH , macgyver.position[0] * map.SPRITE_WIDTH, map.SPRITE_WIDTH, map.SPRITE_WIDTH],0)
    pygame.draw.rect(screen, RED, [guardian.position[1] * map.SPRITE_WIDTH , guardian.position[0] * map.SPRITE_WIDTH, map.SPRITE_WIDTH, map.SPRITE_WIDTH],0)


    # MOVE PERSONS ON THE MAP
    # 0 ---->  #
    # |     y  #
    # |        #
    # V  x     #
    #RÉCUPÉRER LA TOUCHE TAPÉE
    #SI LA CAS EST LIBRE:
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

    if (x2, y2) in map.free_cells:
        macgyver.move((x2,y2))
    else:
        pass


    # PLACE OBJECT ON THE MAP


    # --- GO AHEAD AND UPDATE THE SCREEN WITH WHAT WE'VE DRAWN.
    pygame.display.flip()

    # --- LIMIT TO 60 FRAMES PER SECOND
    clock.tick(60)

# ONCE WE HAVE EXITED THE MAIN PROGRAM LOOP WE CAN STOP THE GAME ENGINE:
pygame.quit()
