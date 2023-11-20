import pygame
import numpy as np

import argparse
import pdb


def update_grid():
    print("test, drawing")
    return


def test():
    # init game
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("test mouse event")

    # game is on
    drawing = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # mouse event stuffs
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                update_grid()
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                update_grid()
            elif event.type == pygame.MOUSEMOTION and drawing:
                update_grid()
    return



if __name__ == "__main__":
    test()

