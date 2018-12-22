#!/usr/bin/python3

import pygame#import pygame for 2D and image
from pygame.locals import *#import constante pygame

from classes.objective import *#import class objective

def main_menu(screen):#main menu of game
    play = True#initialize booleen play to true
    
    background = (pygame.image.load("ressource/Menu.png").convert())#load the background image
    screen.blit(background, (0, 0))#blit background

    pygame.display.flip()#flip screen

    while play:#while play
        for event in pygame.event.get():#event loop
            if event.type == QUIT:#if event is quit
                play = False#play equal false
                return False#function return false
            elif event.type == KEYDOWN:#else if a touch was pressed
                if event.key == K_q:#if the touch is "q"
                    play = False#play equal false
                    return False#function return False
                elif event.key == K_KP1:#else if the touch was "1"
                    play = False#play equal false
                    return True#function return true
                elif event.key == K_KP2:#else if the touch was "2"
                    play = False#play equal false
                    return False#function return false

def create_objective_from_list(list_objective):#function for create list objecitve from list name objective
    x=0#counter x initialize 0
    for item in list_objective:#for each objective in list_objective
        list_objective[x] = Objective(item, True)#the objective[x] transform himself in instance Objective()
        x+=1#add 1 to x
    
    return list_objective#return list of objective
 
def verify_recipe(ingredient_list, inventory):#functions for verify if a inventory contains all the ingredients of a list of ingredients
    x = 0#x initialize to false
    for item in ingredient_list:#for each ingredients in ingredient list
        if item in inventory:#if the ingredient was present in inventory
            x+=1#add 1 to x

    if x == (len(ingredient_list)):#if x is equal to lenght of list ingredients
        return True#function return true
    else:#sinon
        return False#function return false

def verify_victory(inventory):#function for verify the victory or the defeat
    victory = False#victoire initialize to false

    for item in inventory:#for each item in inventory
        if item.name == "syringe":#if the name of item is syringe
            victory = True#victory is true
            break#quit the loop

    return victory#return victory

def end_game(screen, mac_gyver):#function of end game display victory or defeat)
    end_screen = True
    screen = pygame.display.set_mode((500, 400))#resize screen
    victory = verify_victory(mac_gyver.inventory)#test the victory or the defeat

    if victory == True:#if it's a victory
        background = pygame.image.load("ressource/win.png").convert()#load the victory image
    else:#if it's a defeat
        background = pygame.image.load("ressource/lose.png").convert()#load the defeat image

    background = pygame.transform.scale(background , (500, 400))#resize the image

    screen.blit(background, (0, 0))#blit the image

    pygame.display.flip()#flip screen

    while end_screen == True:#event loop
        for event in pygame.event.get():
            if event.type == QUIT:#if the event is quit
                end_screen = False#quit
            elif event.type == KEYUP:#if any touch was pressed
                if event.key == K_RETURN:
                    end_screen = False#quit
