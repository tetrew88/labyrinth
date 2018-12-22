import pygame
from pygame.locals import *

import functions

from classes.character import *
from classes.floor import *
from classes.labyrinth import *
from classes.objective import *
from classes.position import *
from classes.wall import *

def game(screen):#fonction contain the source code of game
    victory = False#initialize boeleen to False
    width_window = int(Labyrinth.WIDTH_TILE * Labyrinth.WIDTH)#calculate width window in multiply(width tile copmposed the world at labytrint width)
    lenght_window = int(Labyrinth.LENGHT_TILE * Labyrinth.LENGHT)##calculate width window in multiply(Lenght tile copmposed the world at labyrinth lenght)

    
    list_objective = ["ether", "plastic tube", "needle"]#create list composed to name of objective to pick-up

    floor = Floor()#create an instance of class Floor
    wall = Wall()#create an instance of class wall
    
    labyrinth = Labyrinth("level")#create an instance of class Labyrinth with the name of level(at change for change level) for argument

    mac_gyver = Character("MacGyver", 15, labyrinth.start_position)#create an inst of class personnage with the argument start position of the class Labyrinth()for argument to position of character
    gardien = Character("Gardien", 15, labyrinth.goal_position)#create an inst of class personnage with the argument goal position of the class Labyrinth() for argument to position of character


    labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"#placed mac_gyver on the map
    labyrinth.world[gardien.position.x][gardien.position.y] = "g"#placed gardien on the map

    list_objective = functions.create_objective_from_list(list_objective)#transform the list name of objective in a list of objective

    for item in list_objective:#for each objective in list of objective
        if item.state == True:#if state of objective is True
            item.obtain_aleatory_position(labyrinth.world)#give a position to objective
            labyrinth.world[item.position.x][item.position.y] = "o"#placed the objective on the map


    screen = pygame.display.set_mode((width_window, lenght_window))#charged the screen

    while labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] != "g":#while Mac Gyver position is diffrent to gardien position
        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"#actulize the position of mac_gyver

        labyrinth.display_world(mac_gyver, gardien, wall, floor, screen)#show the world

        for item in list_objective:#for each objective in list_objective
            if item.state == True:#if objective state is True
                item.display_objective(screen)#display the objective
                if mac_gyver.position.x == item.position.x and mac_gyver.position.y == item.position.y:#if mac_gyver position is the same to objective position
                    mac_gyver.pick_up_objective(item)#mac gyver pick up the objective and add to him inventory
                    labyrinth.world[item.position.x][item.position.y] = "0"#actualize the map

        mac_gyver.display_inventory(screen)#show the inventories of mac gyver

        
        if functions.verify_recipe(list_objective, mac_gyver.inventory) == True:#if the recipe is complete
            mac_gyver.craft_item(list_objective)#mac_gyver craft syringe

        pygame.display.flip()#flip screen

        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "0"

        for event in pygame.event.get():#event loop
            if event.type == QUIT:#if the event is quit
                quit()#quitte
            elif event.type == KEYDOWN:#if a touch  was pressed
                if event.key == K_LEFT:#if the touch is left
                    mac_gyver.move_character("left", labyrinth.world)#if you can move mac gyver to the left 
                elif event.key == K_UP:# else if the touch was up
                    mac_gyver.move_character("up", labyrinth.world)#if you can move mac gyver to the up 
                elif event.key == K_RIGHT:#else if the touch was right
                    mac_gyver.move_character("right", labyrinth.world)#if you can move mac gyver to the right
                elif event.key == K_DOWN:#else if the touch was down
                    mac_gyver.move_character("down", labyrinth.world)#if you can move mac gyver to the down

    functions.end_game(screen, mac_gyver)#end of the game(victory or defeat screen)
