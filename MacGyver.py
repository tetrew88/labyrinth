#!/usr/bin/python3

import pygame
from pygame.locals import *

from package import game
from package.classe import *
from package import fonctions

pygame.init()

def main():
    main_menu = 1

    while main_menu:

        screen = pygame.display.set_mode((500, 400))


        if fonctions.menu_principale(screen) != False:
            game.Game(screen)

        else:
            break
if __name__ == "__main__":
    main()
