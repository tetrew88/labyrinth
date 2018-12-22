#!/usr/bin/python3

import pygame#import pygame for 2D display
from pygame.locals import *#import pygame constant

from classes.position import *
from classes.character import *
from classes.floor import *
from classes.objective import *
from classes.wall import *

import os#import os for create folder, manipulate file, ...

class Labyrinth:
    """Class was designed a labyrith by:
        - his number of ceils of lenght
        - his number of ceils of Width

        - lenght of tile
        - width of tile

        - his world(list 2D)
        - start position of the world(class Position(x,y))
        - goal position of the world(class Position(x,y))
    """

    LENGHT = 15#Number of case of labyrinth lenght
    WIDTH = 15#Number of case of labyrinth width

    LENGHT_TILE = 36#lenght of tile
    WIDTH_TILE = 36#width of tile

    def __init__(self, name_level):
        """constructor of class Labyrinth use name_level for research file of level"""
        self.world = Labyrinth.__world_load(self, name_level)#collecte world from file
        self.start_position = Labyrinth.__collect_start_position(self)#collecte start position from world
        self.goal_position = Labyrinth.__collect_goal_position(self)#collecte goal position from world

    def __world_load(self, name_level):
        """Method for collecte world from file"""
        file_path = "levels/"#path of file contain world
        base_world = []#world of base

        try:#try create a folder(chemin)
             os.mkdir(file_path)
        except FileExistsError:#if the folder was already create
            pass#pass

        file_path = file_path + name_level + ".lvl"#complete the path of file contain world with the name of level and the extension .lvl

        try:#try open file contain world and load world in base_world
            with(open(file_path, "r")) as f:#open the file contain the world
                for ligne in f:#for each  ligne in file
                    level_ligne = []#initialize ligne of level
                    for character in ligne:#for each character in ligne
                        if character != "\n":#if character is different of "\n"
                            level_ligne.append(character)#add character to list level_ligne
                    base_world.append(level_ligne)#add level ligne to 2D list base_world

        except IOError:#if the file contain world do not exist
            base_world = ["0" * self.LENGHT for i in range(self.WIDTH)]#generate a world filled "0" of lenght and width size of labyrinth

            with(open(file_path, "w")) as f:#create the file was contain world
                for ligne in base_world:#for each ligne in base world
                    f.write(str(ligne) + "\n")#write the ligne convert in string in file
                return False #return False

        return base_world#if the world be charged with succes return base_world

    def __collect_start_position(self):
        """Method for collecte start position from world"""
        start = Position(0,0)#initialize start to class Positon(x,y)

        x = 0#initialize counter x
        while x < self.WIDTH:#while x is lower to labyrinth width
            y = 0#initialize counter y
            while y < self.LENGHT:#while y is lower to labyrinth lenght
                if self.world[x][y] == "s":#if world position(x,y) is equal to "s"(for start)
                    start = Position(x, y)#start register the position

                y += 1#add 1 to counter y
            x += 1#add 1 to counter x
            
        return start#return start position

    def __collect_goal_position(self):
        """Method for collecte goal position from world"""
        goal = Position(0,0)#initialize goal to class Position(x,y)

        x = 0#initialize counter x
        while x < self.WIDTH:#while x is lower to labyrinth width
            y = 0#initialize counter y
            while y < self.LENGHT:#while y is lower to labyrinth lenght
                if self.world[x][y] == "g":#if world position(x,y) is equal to "g"(for goal)
                    goal = Position(x, y)#goal register the position

                y += 1#add 1 to counter y
            x += 1#add 1 to counter x

        return goal#return goal position


    def display_world(self, character, gardien, wall, floor, screen):
        """Method for display world"""
        x = 0#initialize counter x
        while x < self.WIDTH:#while x is lower to labyrinth width
            y = 0#initialize counter y
            while y < self.LENGHT:#while y is lower to labyrinth Lenght
                if self.world[x][y] == "0":#if world position(x,y) is equal to "0"
                    floor.display_floor(screen ,x,y)#display floor

                elif self.world[x][y] == "m":#if world position(x,y) is equal to "m"(for mac_gyver)
                    character.display_character(screen)#display character
                    
                elif self.world[x][y] == "g":#if world position(x,y) is equal to "g"(for gardien)
                    gardien.display_character(screen)#display gardien
                
                elif self.world[x][y] == "w":#if world position(x,y) is equal to "w"(for wall)
                    wall.display_wall(screen, x,y)#display wall
                
                elif self.world[x][y] == 'o':# if world position(x,y) is equal to "o" for object
                    floor.display_floor(screen, x,y)#display floor
                y+=1
            x+=1



def main():
    level  = Labyrinth("level")

    if level.world != False:
        print("goal_position: x:{}, y:{}".format(level.goal_position.x, level.goal_position.y))


if __name__ == "__main__":
    main()
