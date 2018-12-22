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
        self.tileset = pygame.image.load("ressource/structures.png").convert_alpha()#load tileset
        self.sprite = pygame.transform.scale(self.tileset.subsurface(1*20, 1*20, 20, 20), (36, 36))#load tile position(position.x of tile*lengt_tile, position.y od tile *width_tile) from tileset and resize tile to size 36x36


    def display_wall(self, screen, x,y):
        screen.blit(self.sprite, (y*labyrinth.Labyrinth.WIDTH_TILE, x*labyrinth.Labyrinth.LENGHT_TILE))#blit the wall


def main():
    wall = Wall()


if __name__ == "__main__":
    main()
