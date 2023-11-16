# https://beltoforion.de/en/recreational_mathematics/game_of_life.php
import pygame
import numpy as np

from canva import canva2array

import argparse
import pdb



colour_about_to_die = (200, 200, 225)
colour_alive = (255, 255, 215)
colour_background = (10, 10, 40)
colour_grid = (30, 30, 60)


# ------------------------79---------------------------------------------------

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputImagePath", help="Path to the input image",
                        default="../canvas/canva_small.jpg")
    args = parser.parse_args()
    return args



def update(surface, cur, sz):
    """Update the canva from current state to next state.

            Parameters:
                    surface (?): seems like a pygame stuff

                    cur (?): current state

                    sz (int): cell size

            Returns:
                    nxt (?): seems like a pygame stuff. The next state.
    """
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            colour = colour_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            colour = colour_alive

        colour = colour if cur[r, c] == 1 else colour_background
        pygame.draw.rect(surface, colour, (c*sz, r*sz, sz-1, sz-1))

    return nxt



def main(cellsize):
    # get arguments
    args = get_args()
    path_img = args.inputImagePath
    
    # initialize array
    cells = canva2array(path_img)
    dimx = cells.shape[1]
    dimy = cells.shape[0]

    # initialize pygame    
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("____'s Game of Life")


    # game is on
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(colour_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main(10)