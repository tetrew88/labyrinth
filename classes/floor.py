#!/usr/bin/python3

import pygame#for load image
from pygame.locals import *#import constante pygame

from classes import labyrinth

class Floor:
    """Class designed a floor by:
        - his tilesett
        - his sprite
    """
    def __init__(self):
        """constructor of class floor"""
        
        #load tileset
        self.tileset = pygame.image.load("ressource/floor-tiles-20x20.png"). \
        convert_alpha()

        #selectionned picture 3 from tileset
        self.sprite = pygame.transform.scale(self.tileset.subsurface \
        (3*20, 0*20,20,20), (36, 36))

    def display_floor(self, screen, x,y):
        """Methode for display floor"""

        #display floor
        screen.blit(self.sprite, (y*labyrinth.Labyrinth.WIDTH_TILE, \
        x*labyrinth.Labyrinth.LENGHT_TILE))#blit floor


def main():
    floor = Floor()


if __name__ == "__main__":
    main()

