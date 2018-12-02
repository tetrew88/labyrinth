#!/usr/bin/python3.7

import json
import os

class Labyrinth:
    LENGHT = 15
    WIDTH = 15


    def __init__(self, name_level):
        self.world = Labyrinth.__world_load(self, name_level)#list 2D
        self.start_position = Labyrinth.__collecte_start_position(self, name_level)#Position()
        self.goal_position = Labyrinth.__collecte_goal_position(self, name_level)#Position()
        Labyrinth.__place_wall(self, name_level)


    def __world_load(self, name_level):
        file_path = "levels/"
        
        try:
            os.mkdir(file_path)
        
            file_path = file_path + name_level + "/"

            os.mkdir(file_path)
        except FileExistsError:
            pass
        
        file_path = file_path + name_level + ".lvl"

        try:
            with(open(file_path, "r")) as f:
                return json.load(f)

        except IOError:
            base_world = [[0] * self.LENGHT for i in range(15)]

            with(open(file_path, "w")) as f:
                    json.dump(base_world, f)
            
            return base_world
    

    def __collecte_start_position(self, name_level):
        data = {}
        file_path = "levels/" + name_level + "/" + "config.txt"
        
        try:
            with(open(file_path, "r")) as f:
                data = json.load(f)
                data["start_position"] = Position(data["start_position"][0], data["start_position"][1])
        except IOError:
            data["start_position"] = [0, 0]
            
            with(open(file_path, "w")) as f:
                json.dump(data, f)
            
            data["start_position"] = Position(0, 0)

        return data["start_position"]

    
    def __collecte_goal_position(self, name_level):
        data = {}
        
        file_path = "levels/" + name_level + "/" + "config.txt"

        try:
            with(open(file_path, "r")) as f:
                data = json.load(f)
                if "goal_position" in data:
                    data["goal_position"] = Position(data["goal_position"][0], data["goal_position"][1])
                else:
                    raise IOError
        except IOError:
            data["goal_position"] = [15, 15]

            with(open(file_path, "w")) as f:
                json.dump(data, f)

            data["goal_position"] = Position(15, 15)

        return data["goal_position"]

    
    def __place_wall(self, name_level):
        list_wall_position = []
        x = 0
        
        while x < self.WIDTH:
            y = 0
            while y < self.LENGHT:
                if self.world[x][y] == "w":
                    self.world[x][y] = Wall()
                y+=1
            x+=1


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
    pass


if __name__ == "__main__":
    test = Labyrinth("level1")
    print(test.goal_position.x_position)
