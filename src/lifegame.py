# https://beltoforion.de/en/recreational_mathematics/game_of_life.php
import pygame
import numpy as np
from math import floor

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
    parser.add_argument("-b", "--brushSize", help="Size of brush.",
                        default=3)
    args = parser.parse_args()
    return args



# ------------------------79---------------------------------------------------
def update(surface:pygame.surface.Surface, cur:np.ndarray, sz:int) -> np.ndarray:
    """Update the canva from current state to next state.

            Parameters:
                    surface (pygame.surface.Surface): The surface on which
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



def update_by_mouse_event(mouse_pos:tuple, cur:np.ndarray, cellsize:int, brushsize:int) -> np.ndarray:
    """Update the current state by mouse event. When the mouse is drawing on
    the canva, what it draw will be considered as live cells.

            Parameters:
                    mouse_pos (tuple): The current position of mouse. 
                    mouse_pos[0] is the x axis.
                    mouse_pos[1] is the y axis.
                    The origine is the left top most.

                    cur (np.ndarray): The current state.

                    cellsize (int): Cell size. The number of pixels of a 
                    cell's length

                    brushsize (int): size of brush.

            Returns:
                    cur (np.ndarray): The current state updated by mouse 
                    event.
    """
    # print(mouse_pos)
    row, col = mouse_pos[1] // cellsize, mouse_pos[0] // cellsize
    # The formula below solves the scenario:
    # If brushsize is odd, 3 for example, i want cells below to be alive:
    # 0 0 0 0 0
    # 0 + + + 0
    # 0 + * + 0
    # 0 + + + 0
    # 0 0 0 0 0 (* is where the mouse clicked)
    # If brushsize is even, 4 for example, i want cells below to be alive:
    # 0 0 0 0 0 0
    # 0 + + + + 0
    # 0 + * + + 0
    # 0 + + + + 0
    # 0 + + + + 0 (* is where the mouse clicked)
    # 0 0 0 0 0 0 (* is where the mouse clicked)
    part_small = (brushsize-1) // 2
    part_big  = brushsize - part_small
    # The following conditions are for numpy slicing.
    # np recognize cur[0:1], but it does not recognize cur[-1:1]
    row_left = row - part_small if row - part_small >= 0 else 0
    col_left = col - part_small if col - part_small >= 0 else 0
    row_right = row + part_big if row + part_big <= cur.shape[0] else cur.shape[0]
    col_right = col + part_big if col + part_big <= cur.shape[1] else cur.shape[1]
    # Lives givens by the brush
    cur[row_left:row_right, col_left:col_right] = 1
    return cur



# ------------------------79---------------------------------------------------
def game_is_on(surface:pygame.surface.Surface, cells:np.ndarray, 
               cellsize:int, brushsize:int) -> None:
    """Start Conway's lifegame.

            Parameters:
                    surface (pygame.surface.Surface): The surface on which our
                    pygame is displayed. 

                    cells (np.ndarray): Array of cells, live or dead. It will
                    be represented on the surface.

                    cellsize (int): Cell size. The number of pixels of a 
                    cell's length.
                    
                    brushsize (int): Brush size.

            Returns:
                    Never. 
    """
    # game is on
    drawing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # mouse event stuffs
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                cells = update_by_mouse_event(pygame.mouse.get_pos(), 
                                              cells, cellsize, brushsize)
                while drawing:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION and drawing:
                            # print("mouse motion")
                            cells = update_by_mouse_event(pygame.mouse.get_pos(), 
                                                          cells, cellsize, brushsize)
                        elif event.type == pygame.MOUSEBUTTONUP:
                            # print("mouse up")
                            drawing = False
                            cells = update_by_mouse_event(pygame.mouse.get_pos(),
                                                          cells, cellsize, brushsize)
            # print("for loop end")

        surface.fill(colour_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()



def main():
    # get arguments
    args = get_args()
    path_img = args.inputImagePath
    cellsize = args.cellSize
    brushsize = args.brushSize
    
    # initialize array from input image
    cells = canva2array(path_img)
    dimx = cells.shape[1] # width of input image
    dimy = cells.shape[0] # height of input image

    # initialize pygame    
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Conway's Game of Life")

    # game is on
    game_is_on(surface, cells, cellsize, brushsize)

    

if __name__ == "__main__":
    main()