#!/usr/bin/python3


import pygame#import pygame for load image
from pygame.locals import *#import constante pygame

from classes import labyrinth
from classes.position import *
from classes import objective

class Character:
    """Class was disigned a character by:
        - his name
        - a booleen who says if the character is alive or no
        - his position
        - his inventory
        - his sprite
    """
    def __init__(self, name, alive, position):
        """constructor of the class Character()"""
        self.name = name
        self.alive = alive
        self.position = position
        self.inventory = []

        #load sprite character
        self.sprite = pygame.image.load("ressource/" + self.name + ".png") \
        .convert_alpha()


    def move_character(self, direction, world):
        """Method for move the character"""

        #if the user want go to the right
        if direction == "right":
            #check if character d'ont go outside the map
            if self.position.y < labyrinth.Labyrinth.LENGHT:
                #if the element at the right of character is different to wall
                if world[self.position.x][(self.position.y + 1)] != "w":
                    #move the character
                    self.position = Position(self.position.x, \
                    (self.position.y +1))
        
        #else if the user want go to left
        elif direction == "left":
            #check if character don't go outside the map
            if self.position.y > -1:
                #if the element at the left of character is different to wall
                if world[self.position.x][(self.position.y - 1)] != "w":
                    #move character
                    self.position = Position(self.position.x, \
                    (self.position.y +- 1))

        #else if the playeur want go up
        elif direction == "up":
            #check if the character don't go outside the map
            if self.position.x > -1:
                #if the element at the up of character is different to wall
                if world[(self.position.x - 1)][self.position.y] != "w":
                    #move character
                    self.position = Position((self.position.x - 1), \
                    self.position.y)

        #else if the playeur want go down
        elif direction == "down":
            #check if the character don't go outside the map
            if self.position.x < labyrinth.Labyrinth.WIDTH:
                #if the element at the down of character is different to wall
                if world[(self.position.x + 1)][self.position.y] != "w":
                    #move character
                    self.position = Position((self.position.x + 1), \
                    self.position.y)


    def pick_up_objective(self, objective):
        """Method for pick-up an objective from the world"""
        
        #add objective to playeur inventory
        self.inventory.append(objective)

        #unactive objective state
        objective.state = False


    def craft_item(self, ingredients_list):
        """Method for craft an item"""
        
        #for each item in ingredients_list
        for item in ingredients_list:
            #del the item in the inventory playeur
            self.inventory.remove(item)

        #create syringe
        syringe = objective.Objective("syringe", False)

        #add syringe to playeur inventory
        self.inventory.append(syringe)


    def display_inventory(self, screen):
        """Method for display the inventory of playeur"""
        x= y = 0#initialize coordonee x and y

        #for each item in playeur inventory
        for item in self.inventory:
            #resize item to dimension "30x30" and 
            #blit it to position(x*taille_tile, 0)
            
            #display item
            screen.blit(pygame.transform.scale(item.sprite, (30,30)), (x*30 ,y))
            
            x += 2#add 2 at x

    def display_character(self, screen):
        """Methode for display character"""

        #display the character to his position
        screen.blit(self.sprite, \
        (self.position.y*labyrinth.Labyrinth.WIDTH_TILE, \
        self.position.x*labyrinth.Labyrinth.LENGHT_TILE))

def main():
    character = Character("MacGyver", True, Position(0, 0))
    print(character.name)


if __name__ == "__main__":
    main()
