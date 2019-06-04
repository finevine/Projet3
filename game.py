from model import *
import pygame

pygame.init()

# DEFINE MAP
map = Map('Structure.csv')

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
    (free_row, free_col) = np.where(map.skl > 0)
    i = 0
    while i < free_col.size:
        pygame.draw.rect(screen, BLACK, [free_col[i] * 20 , free_row[i] * 20, 20, 20],0)
        i += 1


    # MOVE PERSONS ON THE MAP
    # 0 ---->  #
    # |     y  #
    # |        #
    # V  x     #

    # choices = {
    #     pygame.K_UP: macgyver.position[0] -=1, #UP',
    #     pygame.K_RIGHT: macgyver.position[1] +=1, #RIGHT',
    #     pygame.K_DOWN: macgyver.position[0] +=1, #DOWN',
    #     pygame.K_LEFT: macgyver.position[1] -=1#LEFT'
    # }
    # choices[event.key]

    #RÉCUPÉRER LA TOUCHE TAPÉE
    #SI LA CAS EST LIBRE:
        #ALLER SUR LA CASE
    #SINON RESTER SUR LA MÊME CASE



    # PLACE OBJECT ON THE MAP


    # --- GO AHEAD AND UPDATE THE SCREEN WITH WHAT WE'VE DRAWN.
    pygame.display.flip()

    # --- LIMIT TO 60 FRAMES PER SECOND
    clock.tick(60)

# ONCE WE HAVE EXITED THE MAIN PROGRAM LOOP WE CAN STOP THE GAME ENGINE:
pygame.quit()
