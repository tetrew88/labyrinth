#!/usr/bin/python3

import pygame#import pygame for 2D and image
from pygame.locals import *#import constante pygame

from classes.objective import *#import class objective

def main_menu(screen):
    """main menu of the game"""
    play = True#initialize booleen play to true
    
    #load background picture
    background = (pygame.image.load("ressource/Menu.png").convert())
    
    #display background
    screen.blit(background, (0, 0))

    pygame.display.flip()#flip screen

    
    """main loop"""
    while play:

        """event loop"""
        for event in pygame.event.get():
            #if event is quit
            if event.type == QUIT:
                #quit
                play = False
            
            #else if a touch was pressed
            elif event.type == KEYDOWN:
                #if the touch was 'q':
                if event.key == K_q:
                    #quit
                    play = False
                
                #else if the touch was "1"
                elif event.key == K_KP1:
                    play = False#quit boucle
                    return True#function return true
                
                #else if the touch was "2"
                elif event.key == K_KP2:#else if the touch was "2"
                    #quit
                    play = False

    return play


def create_objective_from_list(list_objective):
    """function for create list objective from name objective list"""
    x=0#counter x initialize 0
    
    #start creation
    for item in list_objective:#for each objective in list_objective
        #the objective[x] transform himself in instance Objective()
        list_objective[x] = Objective(item, True)
        x+=1#add 1 to x
    

    return list_objective#return list of objective
 

def verify_recipe(ingredient_list, inventory):
    """function for verify if mac gyver a the necessary for craft syringe"""

    x = 0#x initialize to false
    
    #travel list of ingredients
    for item in ingredient_list:
        #if the ingredient is present to inventory of mac gyver
        if item in inventory:
            x+=1#add 1 to x

    #verify if the counter is equal to lenght of ingredient_list
    if x == (len(ingredient_list)):
        return True#function return true
    else:#sinon
        return False#function return false


def verify_victory(inventory):
    """function for verify the victory or the defeat"""
    victory = False#victory initialize to false

    #travel the inventory of mac gyver
    for item in inventory:
        #if syringe is in inventory of mac_gyver
        if item.name == "syringe":
            victory = True#victory is true
            break#quit the loop

    return victory#return victory


def end_game(screen, mac_gyver):#
    """function of end game display victory or defeat"""
    
    end_screen = True
    
    #resize screen
    screen = pygame.display.set_mode((500, 400))
    
    #test victory
    victory = verify_victory(mac_gyver.inventory)

    #if it's a victory
    if victory == True:
        #load victory picture
        background = pygame.image.load("ressource/win.png").convert()
   
    #if it's a deafeat
    else:
        #load defeat picture
        background = pygame.image.load("ressource/lose.png").convert()
        mac_gyver.alive = False#mac gyver is dead

    #resize picture
    background = pygame.transform.scale(background , (500, 400))

    screen.blit(background, (0, 0))#blit the image

    pygame.display.flip()#flip screen


    """event loop"""
    while end_screen == True:
        for event in pygame.event.get():
            #if event is quit
            if event.type == QUIT:
                end_screen = False#quit
            
            #if any touch was pressed
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    end_screen = False#quit
