#!/usr/bin/python3

import json
import os

class Labyrinth:
    LENGHT = 15
    WIDTH = 15

    def __init__(self, name_level):
        self.world = Labyrinth.__world_load(self, name_level)#list 2D
        self.start_position = Labyrinth.__collecte_start_position(self)#Position
        self.goal_position = Labyrinth.__collecte_goal_position(self)#Position
        Labyrinth.__place_wall(self)
        #self.sprite_floor

    def __world_load(self, name_level):
        file_path = "levels/"
        base_world = []

        try:    
            os.mkdir(file_path)
        except FileExistsError:
                pass
        file_path = file_path + name_level + "/"

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
        x=0
        while x < self.WIDTH:
            y=0
            while y < self.LENGHT:
                if self.world[x][y] == "s":
                    return Position(x, y)
                y += 1
            x += 1

    
    def __collecte_goal_position(self):
        x=0
        while x < self.WIDTH:
            y=0
            while y < self.LENGHT:
                if self.world[x][y] == "g":
                    return Position(x, y)
                y += 1
            x += 1


    def __place_wall(self):
        x=0
        while x < self.WIDTH:
            y=0
            while y < self.LENGHT:
                if self.world[x][y] == "m":
                    self.world[x][y] = Wall()
                y +=1
            x +=1


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
        self.sprite = ("package/ressource/" + name + ".png")
    
    def move_personnage(self, direction, labyrinth):
        if direction == "left":
            if (self.position.y_position - 1) > -1:
                if isinstance(labyrinth.world[self.position.x_position][(self.position.y_position - 1)],  MUR) == False:
                    self.position.y_position -= 1

        elif direction == "right":
            if (self.position.y_position + 1) < labyrinth.LENGHT:
                if isinstance(labyrinth.world[self.position.x_position][(self.position.y_position +1)], MUR) == False:
                    self.position.y_position += 1

        elif direction == "down":
            if(self.position.x_position + 1 ) < labyrinth.WIDTH:
                if isinstance(labyrinth.world[(self.position.x_position +1)][self.position.y_position] ,MUR) == False:
                    self.position.x_position += 1
        elif direction == "up":
            if (self.position.x_position - 1) > -1:
                if isinstance(labyrinthe.world[(self.position.x_position - 1)][self.position.y_position] ,Mur) == False:
                    self.position.x_position -= 1


    def pick_up_object(self, obj):
        self.inventory.append(obj)
        obj.state = False


    def craft_weapond(self, name, ingredients):
        pass
        

    def attack_arme(self, cible, weapond):
        print("{} attack {} with:\n {} et inflige {}  degats".format(self.name, cible.name, weapond.name, weapond.damage))
        cible.receive_damage(weapond.damage)

    def receive_damage(self, damage):
        self.life = self.life - damage
        if self.life < 1:
            self.alive = False


class Object:
    def __init__(self, name, position, state):
        self.name = name
        self.position = position
        self.state = state


class Weapond:
    def __init__(self, nom, damage, effect):
        self.nom = name
        self.damage = damage
        self.effect = effect

class Wall:
    
    def __init__():
    #self.sprite = 
        pass

if __name__ == "__main__":
    test = Labyrinth("level")
    print(test.goal_position.x_position)
