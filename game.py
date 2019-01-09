import pygame
from pygame.locals import *

import functions

from classes.character import *
from classes.floor import *
from classes.labyrinth import *
from classes.objective import *
from classes.position import *
from classes.wall import *

def game(screen):
    """code of the game"""

    victory = False#initialize boeleen to False

    """initialise size of the window"""
    #calculation width window 
    width_window = int(Labyrinth.WIDTH_TILE * Labyrinth.WIDTH)
    
    #calculation lenght window
    lenght_window = int(Labyrinth.LENGHT_TILE * Labyrinth.LENGHT)
    
    
    #create list composed to name of objective to pick-up
    list_objective = ["ether", "plastic tube", "needle"]

    floor = Floor()#create an instance of class Floor
    wall = Wall()#create an instance of class wall
    
    #create an instance of class Labyrinth with the name of level for argument
    #at change for change level
    labyrinth = Labyrinth("level")

    
    """create character"""
    #create Mac gyver character with start position of labyrinth for position
    mac_gyver = Character("MacGyver", 15, labyrinth.start_position)
    
    #create gardien character with goal position of labyrinth for position
    gardien = Character("Gardien", 15, labyrinth.goal_position)

    
    #create objective list from objective name list
    list_objective = functions.create_objective_from_list(list_objective)
    
    
    """placed element on map"""
    #placed mag gyver on map
    labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"

    #placed gardien on map
    labyrinth.world[gardien.position.x][gardien.position.y] = "g"

    #placed objective on map
    for item in list_objective:#for each objective in list of objective
        if item.state == True:#if state of objective is True
            item.obtain_aleatory_position(labyrinth.world)#give a position to objective
            labyrinth.world[item.position.x][item.position.y] = "o"


    #initialize screen
    screen = pygame.display.set_mode((width_window, lenght_window))
    
    
    """Game start"""
    

    """main loop of the game"""
    #while mac_gyver position is different to gardien position
    while labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] != "g":
        #actualize position of mac gyver
        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"

        #display the world
        labyrinth.display_world(mac_gyver, gardien, wall, floor, screen)

        
        """check if the objectives must be display and captured"""
        for item in list_objective:#for each objective in list_objective
            if item.state == True:#if objective state is True
                item.display_objective(screen)#display the objective
                    
                #check if mag gyver position is equal to objectif position
                if mac_gyver.position.x == item.position.x and \
                mac_gyver.position.y == item.position.y:

                    #mac gyver can pick_up_objective
                    mac_gyver.pick_up_objective(item)

                    #actualise the world
                    labyrinth.world[item.position.x][item.position.y] = "0"
        
        
        #show inventory of macGyver
        mac_gyver.display_inventory(screen)

        
        """verify if mac have the necessary for craft syringe"""
        #if recipe is good
        if functions.verify_recipe(list_objective, mac_gyver.inventory) == True:
            #mac gyver craft the syringe
            mac_gyver.craft_item(list_objective)

        pygame.display.flip()#flip screen

        #prepared the world for mac gyver move's
        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "0"


        """event loop"""
        for event in pygame.event.get():
            #if click croos
            if event.type == QUIT:
                quit()#quit
            
            #if a touch was pressed
            elif event.type == KEYDOWN:
                #if the touch was left
                if event.key == K_LEFT:
                    #try move mac gyver to the left
                    mac_gyver.move_character("left", labyrinth.world)
                
                #else if the touch was up
                elif event.key == K_UP:
                    #try move macGyver to the left
                    mac_gyver.move_character("up", labyrinth.world)

                #else if the touch was right
                elif event.key == K_RIGHT:
                    #try move mac gyver to the right
                    mac_gyver.move_character("right", labyrinth.world)
                
                #else if the touch was down
                elif event.key == K_DOWN:
                    #try move mac gyver to the right
                    mac_gyver.move_character("down", labyrinth.world)

    
    """End of the game"""
    #verify victory, victory screen or defeat screen
    functions.end_game(screen, mac_gyver)
