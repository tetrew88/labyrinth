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
        self.sprite = pygame.image.load("ressource/" + self.name + ".png").convert_alpha()#load the sprite of caractere from folder ressource in foction of the name of character


    def move_character(self, direction, world):
        """Method for move the character"""
        if direction == "right":#if the playeur want go to the right
            if self.position.y < labyrinth.Labyrinth.LENGHT:#check if the character doesn't go out the map
                if world[self.position.x][(self.position.y + 1)] != "w":#check if there is a wall on the right of the character
                    self.position = Position(self.position.x, (self.position.y +1))#if all done good, registry the new position in cacracter.position

        elif direction == "left":#if the playeur want go to left
            if self.position.y > -1:#check if the character doesn't go outside the map
                if world[self.position.x][(self.position.y - 1)] != "w":#check if there is a wall on the left of the character
                    self.position = Position(self.position.x, (self.position.y +- 1))#if all done good, registry the new position in cacracter.position

        elif direction == "up":#if the playeur want go up
            if self.position.x > -1:#check if the character don't go out the map
                if world[(self.position.x - 1)][self.position.y] != "w":#check if there is a wall on the top of the character
                    self.position = Position((self.position.x - 1),self.position.y)#if all done good, registry the new position in cacracter.position

        elif direction == "down":#if the playeur want to go down
            if self.position.x < labyrinth.Labyrinth.WIDTH:#check if the character doesn't go out the map
                if world[(self.position.x + 1)][self.position.y] != "w":#check if there is a wall on the down of the character
                     self.position = Position((self.position.x + 1),self.position.y)#if all done good, registry the new position in cacracter.position


    def pick_up_objective(self, objective):
        """Method for pick-up an objective from the world"""
        self.inventory.append(objective)#add objective at the inventory of playeur
        objective.state = False#change the booleen of display(state) to False


    def craft_item(self, ingredients_list):
        """Method for craft an item"""
        for item in ingredients_list:#for each item in ingredients list
            self.inventory.remove(item)#remove item in the ingredients list

        syringe = objective.Objective("syringe", False)#create syringe
        self.inventory.append(syringe)#add syringe to inventory of the playeur


    def display_inventory(self, screen):
        """Method for display the inventory of playeur"""
        x= y = 0#initialize coordonee x and y

        for item in self.inventory:#for each item in playeur inventory
            screen.blit(pygame.transform.scale(item.sprite, (30,30)), (x*30 ,y))#resize each item to dimension "30x30" and blit it to position(x*taille_tile, 0)
            x += 2#add 2 at 2

    def display_character(self, screen):
        screen.blit(self.sprite, (self.position.y*labyrinth.Labyrinth.WIDTH_TILE, self.position.x*labyrinth.Labyrinth.LENGHT_TILE))#blit character

def main():
    character = Character("MacGyver", True, Position(0, 0))
    print(character.name)


if __name__ == "__main__":
    main()
