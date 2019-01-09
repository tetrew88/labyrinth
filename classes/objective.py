#!/usr/bin/python3

import random

import pygame#for load image
from pygame.locals import*#import constante pygame

from classes.position import *
from classes.labyrinth import *

class Objective:
    """Class designed an objective by:
        - his name
        - his position
        - his state(for blit or not objective)
        - his sprite
    """
    def __init__(self, name, state):
        """Constructor of class objective()"""
        self.name = name
        self.position = Position(0,0)
        self.state = state

        #load and resize image to size 36*36
        self.sprite = pygame.transform.scale(pygame.image.load("ressource/" \
        + name +".png").convert_alpha(), (36, 36))

    
    @property
    def blit_position(self):#blit position of the objective
        """blit position"""

        return Position(self.position.y*Labyrinth.WIDTH_TILE, \
        self.position.x*Labyrinth.LENGHT_TILE)


    def obtain_aleatory_position(self, world):
        """Method for obtain a aleatory position"""
        position_ok = False#position_ok initialize to false

        #while position wasn't empty
        while position_ok == False:
            #generate random x
            self.position.x = random.randint(0, Labyrinth.WIDTH - 1) 
            
            #generate random y
            self.position.y = random.randint(0, Labyrinth.LENGHT - 1)

            #if case is empty
            if world[self.position.x][self.position.y] == "0":
                break#quit the loop

    
    def display_objective(self, screen):
        """Method for display objective"""
        #if state of objective is true
        if self.state == True:
            #display objective
            screen.blit(self.sprite, (self.blit_position.x, self.blit_position.y))


def main():
    objective = Objective("test", True)
    print(objective.name)



if __name__ == "__main__":
    main()
