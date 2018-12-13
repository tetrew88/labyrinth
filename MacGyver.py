#!/usr/bin/python3

import pygame
import game
import fonctions

from classe import *
from pygame.locals import *

pygame.init()

def main():
    main_menu = 1

    pygame.key.set_repeat(200, 200)

    while main_menu:

        screen = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("Labyrinth")

        if fonctions.menu_principale(screen) != False:
            game.Game(screen)

        else:
            break
if __name__ == "__main__":
    main()
