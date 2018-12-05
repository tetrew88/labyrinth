#!/usr/bin/python3

import pygame
from pygame.locals import *

from package import game
from package.classe import *
from package import fonctions

pygame.init()

def main():
    screen = pygame.display.set_mode((500, 400))


    if fonctions.menu_principale(screen) != False:
        if game.Game(screen) != False:
            pass

if __name__ == "__main__":
    main()
