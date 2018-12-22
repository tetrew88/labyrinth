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
        self.tileset = pygame.image.load("ressource/floor-tiles-20x20.png").convert_alpha()#load tileset
        self.sprite = pygame.transform.scale(self.tileset.subsurface(3*20, 0*20,20,20), (36, 36))##load tile position(3*lengt_tile, 0*width_tile) from tileset and resize tile to size 36x36

    def display_floor(self, screen, x,y):
        screen.blit(self.sprite, (y*labyrinth.Labyrinth.WIDTH_TILE, x*labyrinth.Labyrinth.LENGHT_TILE))#blit floor
def main():
    floor = Floor()


if __name__ == "__main__":
    main()

