#!/usr/bin/python3

import pygame
from pygame.locals import *

import json
import os
import random

class Labyrinth:
    LENGHT = 15
    WIDTH = 15

    LENGHT_TILE = 32
    WIDTH_TILE = 36

    def __init__(self, name_level):
        self.world = Labyrinth.__world_load(self, name_level)#list 2D
        self.start_position = Labyrinth.__collecte_start_position(self)#Position
        self.goal_position = Labyrinth.__collecte_goal_position(self)#Position

    def __world_load(self, name_level):
        file_path = "levels/"
        base_world = []

        try:    
            os.mkdir(file_path)
        except FileExistsError:
                pass
        
        file_path = file_path + name_level + ".lvl"

        try:
            with(open(file_path, "r")) as f:
                for ligne in f:
                    ligne_niveau = []
                    for letters in ligne:
                        if letters != "\n":
                            ligne_niveau.append(letters)
                    base_world.append(ligne_niveau)
        
        except IOError:
            base_world = ["0" * self.LENGHT for i in range(self.WIDTH)]

            with(open(file_path, "w")) as f:
                for ligne in base_world:
                    f.write(str(ligne) + "\n")
            return False
        return base_world
    

    def __collecte_start_position(self):
        start = Position(0, 0)
        x=0
        while x < self.WIDTH:
            y=0
            while y < self.LENGHT:
                if self.world[x][y] == "s":
                    start = Position(x, y)
                y += 1
            x += 1
        return start

    
    def __collecte_goal_position(self):
        goal = Position(0, 0)
        x=0
        while x < self.WIDTH:
            y=0
            while y < self.LENGHT:
                if self.world[x][y] == "g":
                    goal = Position(x, y)
                y += 1
            x += 1
        return goal

    def display_world(self, mac_gyver, gardien, wall, floor, screen):
        x = 0
        while x < self.WIDTH:
            y = 0
            while y < self.LENGHT:
                if self.world[x][y] == "0":
                    floor.display_floor(screen ,x,y)
                elif self.world[x][y] == "m":
                    mac_gyver.display_personnage(screen)
                elif self.world[x][y] == "g":
                    gardien.display_personnage(screen)
                elif self.world[x][y] == "w":
                    wall.display_wall(screen, x,y)
                elif self.world[x][y] == 'o':
                    floor.display_floor(screen, x,y)
                y+=1
            x+=1


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Personnage:
    def __init__(self, name, life, position):
        self.name = name
        self.alive = True
        self.position = position
        self.inventory = []
        self.sprite = pygame.image.load("ressource/" + self.name + ".png").convert_alpha()
        self.life = life
     
    def move_personnage(self, direction, world):
        if direction == "right":
            if self.position.y < Labyrinth.LENGHT:
                if world[self.position.x][(self.position.y + 1)] != "w":
                   self.position = Position(self.position.x, (self.position.y +1))
        elif direction == "left":
            if self.position.y > -1:
                if world[self.position.x][self.position.y - 1] != "w":
                    self.position = Position(self.position.x, (self.position.y - 1))
        elif direction == "up":
            if self.position.x > -1:
                if world[self.position.x - 1][self.position.y] != "w":
                    self.position = Position((self.position.x - 1), self.position.y)
        elif direction == "down":
            if self.position.x < Labyrinth.WIDTH:
                if world[self.position.x + 1][self.position.y] != "w":
                    self.position = Position((self.position.x + 1), self.position.y)

    def pick_up_object(self, obj):
        self.inventory.append(obj)
        obj.state = False

    def craft_object(self, list_ingredients):
        for item in list_ingredients:
            self.inventory.remove(item)

        seringue = Object("seringue", False)
        self.inventory.append(seringue)

    def display_personnage(self, screen):
        screen.blit(self.sprite, (self.position.y*Labyrinth.WIDTH_TILE, self.position.x*Labyrinth.LENGHT_TILE))

    def display_inventory(self, screen):
        x = 0
        for item in self.inventory:
            screen.blit(pygame.transform.scale(item.sprite, (30,30)), (x*20, 0))
            x += 2

class Object:
    def __init__(self, name, state):
        self.name = name
        self.position = Position(0,0)
        self.state = state
        self.sprite = pygame.transform.scale(pygame.image.load("ressource/" + name +".png").convert_alpha(), (36, 36))
        
    @property
    def blit_position(self):
        return Position(self.position.y*Labyrinth.WIDTH_TILE, self.position.x*Labyrinth.LENGHT_TILE)

    def obtain_aleatory_position(self, world):
        position_ok = False

        while position_ok == False:
            self.position.x = random.randint(0, Labyrinth.WIDTH - 1)
            self.position.y = random.randint(0, Labyrinth.LENGHT - 1)

            if world[self.position.x][self.position.y] == "0":
                break

    def display_object(self, screen):
        if self.state == True:
            screen.blit(self.sprite, (self.blit_position.x, self.blit_position.y))

class Wall:
    def __init__(self):
        self.tileset = pygame.image.load("ressource/structures.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.tileset.subsurface(1*20, 1*20 ,20,20), (36,36))

    def display_wall(self, screen, x,y):
        screen.blit(self.sprite, (y*Labyrinth.WIDTH_TILE, x*Labyrinth.LENGHT_TILE))


class Floor:
    def __init__(self):
        self.tileset = pygame.image.load("ressource/floor-tiles-20x20.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.tileset.subsurface(3*20, 0*20,20,20), (36, 36))

    def display_floor(self, screen, x,y):
        screen.blit(self.sprite, (y*Labyrinth.WIDTH_TILE, x*Labyrinth.LENGHT_TILE))

if __name__ == "__main__":
    test = Labyrinth("level")
