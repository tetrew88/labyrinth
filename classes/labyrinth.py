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
        
        #collect world from file level
        self.world = Labyrinth.__world_load(self, name_level)

        #collecte start position
        self.start_position = Labyrinth.__collect_start_position(self)

        #collecte goal position
        self.goal_position = Labyrinth.__collect_goal_position(self)

    def __world_load(self, name_level):
        """Method for collecte world from file"""
        #path of file contain world
        file_path = "levels/"

        base_world = []#world of base

        #try create a folder(chemin)
        try:
            os.mkdir(file_path)
        #if the folder was already create

        except FileExistsError:
            pass#pass

        #complete path with name of level and extention ".lvl"
        file_path = file_path + name_level + ".lvl"

        """load world"""

        #try open file contain world and load world in base_world
        try:
            #open the file contain the world
            with(open(file_path, "r")) as f:
                #for each  ligne in file
                for ligne in f:
                    #initialize ligne of level
                    level_ligne = []
                    
                    #for each character in ligne
                    for character in ligne:
                        #if character is different of "\n"
                        if character != "\n":
                            #add character to list level_ligne
                            level_ligne.append(character)
                    
                    #add level ligne to 2D list base_world
                    base_world.append(level_ligne)

        #if the file contain world do not exist
        except IOError:
            #generate a world filled "0"
            base_world = ["0" * self.LENGHT for i in range(self.WIDTH)]

            #create a file for save the new world
            with(open(file_path, "w")) as f:
                #for each line in fichier
                for ligne in base_world:
                    #write the line in file
                    f.write(str(ligne) + "\n")
                
                return False #return False

        return base_world

    def __collect_start_position(self):
        """Method for collecte start position from world"""

        #initialize start (0,0)
        start = Position(0,0)

        x = 0#initialize counter x
        #while x is lower to width of labyrinth
        while x < self.WIDTH:
            y = 0#initialize counter y

            #while y is lower to labyrinth lenght
            while y < self.LENGHT:
                #if world[x][y] is equal to "s" for start
                if self.world[x][y] == "s":
                    #register start position
                    start = Position(x, y)

                y += 1#add 1 to counter y
            x += 1#add 1 to counter x
            
        return start#return start position

    def __collect_goal_position(self):
        """Method for collecte goal position from world"""
        #initialize goal to class Position(x,y)
        goal = Position(0,0)

        x = 0#initialize counter x
        #while x is lower to labyrinth width
        while x < self.WIDTH:
            y = 0#initialize counter y
            
            #while y is lower to labyrinth lenght
            while y < self.LENGHT:
                #if world position(x,y) is equal to "g"(for goal)
                if self.world[x][y] == "g":
                    goal = Position(x, y)#goal register the position

                y += 1#add 1 to counter y
            x += 1#add 1 to counter x

        return goal#return goal position


    def display_world(self, character, gardien, wall, floor, screen):
        """Method for display world"""
        x = 0#initialize counter x
        
        #while x is lower to labyrinth width
        while x < self.WIDTH:
            y = 0#initialize counter y
            
            #while y is lower to labyrinth Lenght
            while y < self.LENGHT:
                #if world position(x,y) is equal to "0"
                if self.world[x][y] == "0":
                    floor.display_floor(screen ,x,y)#display floor

                #if world position(x,y) is equal to "m"(for mac_gyver)
                elif self.world[x][y] == "m":
                    character.display_character(screen)#display character
                    
                #if world position(x,y) is equal to "g"(for gardien)
                elif self.world[x][y] == "g":
                    gardien.display_character(screen)#display gardien
                
                #if world position(x,y) is equal to "w"(for wall)
                elif self.world[x][y] == "w":
                    wall.display_wall(screen, x,y)#display wall
                
                # if world position(x,y) is equal to "o" for object
                elif self.world[x][y] == 'o':
                    floor.display_floor(screen, x,y)#display floor
                
                y+=1
            x+=1



def main():
    level  = Labyrinth("level")

    if level.world != False:
        print("goal_position: x:{}, y:{}".format(level.goal_position.x, level.goal_position.y))


if __name__ == "__main__":
    main()
