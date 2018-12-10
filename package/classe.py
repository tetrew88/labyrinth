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
        self.sprite = pygame.image.load("package/ressource/" + self.name + ".png").convert_alpha()
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
        
        return self.position

    def pick_up_object(self, obj):
        self.inventory.append(obj)

    def craft_weapond(self, name, ingredients):
        pass        

    def attack_weapond(self, cible, weapond):
        print("{} attack {} with:\n {} et inflige {}  degats".format(self.name, cible.name, weapond.name, weapond.damage))
        cible.receive_damage(weapond.damage)

    def receive_damage(self, damage):
        self.life = self.life - damage
        if self.life < 1:
            self.alive = False


class Object:
    def __init__(self, name, state, world):
        self.name = name
        self.position = Object.__obtain_position(self, world)
        self.state = state
        self.sprite = (pygame.transform.scale(pygame.image.load("package/ressource/" + name +".png").convert_alpha(), (36, 36)))
        self.position_blit = Position(self.position.y*Labyrinth.WIDTH_TILE, self.position.x*Labyrinth.LENGHT_TILE)

    def __obtain_position(self, world):
        position_ok = False

        while position_ok == False:
            aleatory_x = random.randint(0, Labyrinth.WIDTH - 1)
            aleatory_y = random.randint(0, Labyrinth.LENGHT - 1)

            if world[aleatory_x][aleatory_y] == "0":
                break

        return Position(aleatory_x, aleatory_y)

    def display_object(self, screen):
        screen.blit(self.sprite, (self.position_blit.x, self.position_blit.y))


class Weapond:
    def __init__(self, nom, damage, effect):
        self.nom = name
        self.damage = damage
        self.effect = effect


class Wall:
    def __init__(self):
        self.tileset = pygame.image.load("package/ressource/structures.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.tileset.subsurface(1*20, 1*20 ,20,20), (36,36))

class Floor:
    def __init__(self):
        self.tileset = pygame.image.load("package/ressource/floor-tiles-20x20.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.tileset.subsurface(3*20, 0*20,20,20), (36, 36))


if __name__ == "__main__":
    test = Labyrinth("level")
