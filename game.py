from model import *
import pygame

pygame.init()
#Define map
map = Map('Structure.csv', 20)
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
# Open a new window
size = (15* map.SPRITE_WIDTH, 15*20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white.
    screen.fill(WHITE)
    #initialize map
    (free_row, free_col) = np.where(map.skl > 0)
    i = 0
    while i < free_col.size:
        pygame.draw.rect(screen, BLACK, [free_col[i] * 20 , free_row[i] * 20, 20, 20],0)
        i += 1

    #place object on the Map
    #place persons on the Map


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
