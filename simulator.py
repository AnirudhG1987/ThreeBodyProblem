"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
#from pygame.locals import *
from universe import Universe

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location


# This sets the margin between each cell
MARGIN = 1

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
WINDOW_SIZE = [1000, 1000]
#g = GameOfLife(100,100)
universe = Universe()
#WIDTH = WINDOW_SIZE[0]/len(g.board[0])
#HEIGHT = WINDOW_SIZE[1]/len(g.board)

pygame.init()

# Set the HEIGHT and WIDTH of the screen

screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Two Body Problem")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x,y=0,0
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(WHITE)
    for planet in universe.planets:
        pygame.draw.circle(screen, planet.color,planet.location, planet.radius, 0)
        pygame.draw.lines(screen, planet.color, False,planet.path)


    # Limit to 60 frames per second
    if abs(planet.accel[0])<3000:
        t=10
    else:
        t=60
    clock.tick(t)
    universe.updateUniverse()
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    #pygame.display.update()

pygame.quit()