#!/usr/bin/python3

import pygame#for load image
from pygame.locals import *#import constante pygame

from classes import labyrinth

class Wall:
    """class designed a wall by:
        - his tileset
        - his sprite
    """
    def __init__(self):
        """Constructor of class wall"""
        
        #load tileset
        self.tileset = pygame.image.load("ressource/structures.png"). \
        convert_alpha()

        #selectionned sprite 1 from tileset
        self.sprite = pygame.transform.scale(self.tileset.subsurface \
            (1*20, 1*20, 20, 20), (36, 36))


    def display_wall(self, screen, x,y):
        """Methode for display wall"""

        #display wall
        screen.blit(self.sprite, (y*labyrinth.Labyrinth.WIDTH_TILE, \
        x*labyrinth.Labyrinth.LENGHT_TILE))


def main():
    wall = Wall()


if __name__ == "__main__":
    main()
