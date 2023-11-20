import pygame
import numpy as np

import argparse
import pdb


def test():
    # init game
    pygame.init()
    surface = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("test mouse event")

    # game is on
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # mouse event stuffs
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse button down")
            elif event.type == pygame.MOUSEBUTTONUP:
                print("mouse button up")
            elif event.type == pygame.MOUSEMOTION:
                print("mouse motion")
    return



if __name__ == "__main__":
    test()

