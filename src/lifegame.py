# https://beltoforion.de/en/recreational_mathematics/game_of_life.php
import pygame
import numpy as np

from canva import canva2array

import argparse
import pdb



colour_about_to_die = (200, 200, 225)
colour_alive = (255, 255, 215)
colour_background = (10, 10, 10)
colour_grid = (30, 30, 60)



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputImagePath", help="Path to the input image",
                        default="../canvas/canva_small.jpg")
    parser.add_argument("-c", "--cellSize", help="Size of a cell, on pixels.",
                        default=10)
    args = parser.parse_args()
    return args



# ------------------------79---------------------------------------------------
def update(surface, cur, sz):
    """Update the canva from current state to next state.

            Parameters:
                    surface (pygame.surface.Surface): the surface on which
                    our pygame is displayed.

                    cur (np.ndarray): The current state

                    sz (int): Cell size. The number of pixels of a cell's length

            Returns:
                    next (np.ndarray): The next state.
    """
    next = np.zeros((cur.shape[0], cur.shape[1]))

    # Iterate through each cell, check one by one if they are going to 
    # die or live.
    for r, c in np.ndindex(cur.shape):
        # Count how many live neigbours does the cell have.
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        # Compute the next state:
        # The cell is living this turn, but is going to die the next turn
        # because of underpopulation or overpopulation
        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            colour = colour_about_to_die
        # The live cell will keep living, or the dead cell becomes alive next turn
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            next[r, c] = 1
            colour = colour_alive

        # Display the current state:
        colour = colour if cur[r, c] == 1 else colour_background
        pygame.draw.rect(surface, colour, (c*sz, r*sz, sz-1, sz-1))
    return next



def update_by_mouse_event():
    print("test, drawing")
    return



def main():
    # get arguments
    args = get_args()
    path_img = args.inputImagePath
    cellsize = args.cellSize
    
    # initialize array
    cells = canva2array(path_img)
    dimx = cells.shape[1] # width of input image
    dimy = cells.shape[0] # height of input image

    # initialize pygame    
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Conway's Game of Life")

    # game is on
    drawing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # change here
            # mouse event stuffs
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                update_by_mouse_event()
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                update_by_mouse_event()
            elif event.type == pygame.MOUSEMOTION and drawing:
                update_by_mouse_event()

        surface.fill(colour_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main()