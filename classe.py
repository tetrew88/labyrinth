#!/usr/bin/python3.7

import json

class Labyrinth:
    LENGHT = 15
    WIDTH = 15

    def __init__(self, name_level):
        self.world = Labyrinth.__world_load(name_level)#list 2D
        self.start_position = Labyrinth.__collecte_start_position(self)#Position()
        self.goal_position = Labyrinth.__collecte_goal_position(self)#Position()

    def __world_load(name_level):
        pass
    

    def __collecte_start_position(self):
        pass

    
    def __collecte_goal_position(self):
        pass


class Position:
    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y

class Personnage:
    def __init__(self, name, life, position):
        self.name = name
        self.alive = True
        self.position = position
        self.inventory = []

    def pick_up_object(self, objet):
        pass

    def craft_weapond(self, name, ingredients):
        pass
        
class Object:
    def __init__(self, name, position, state):
        self.name = name
        self.position = position
        self.state = state

class Weapond:
    def __init__(self, nom, damage):
        self.nom = nom
        self.damage = damage
