#!/usr/bin/python3

import pygame
from pygame.locals import *

from package.classe import *

def menu_principale(screen):
    play = 1
    
    background = pygame.image.load("package/ressource/Menu.png").convert()
    screen.blit(background, (0, 0))

    pygame.display.flip()

    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
                return False
            elif event.type == KEYUP:
                if event.key == K_q:
                    play = 0
                    return False 
                elif event.key == K_KP1:
                    play = 0
                    return True
                elif event.key == K_KP2:
                    play = 0
                    return False

def create_object_from_list(list_object):
    x=0
    for item in list_object:
        list_object[x] = Object(item, True)
        x+=1
    
    return list_object
 
def verify_recipe(ingredient_list, inventory):
    test = False
    x = 0
    for item in ingredient_list:
        if item in inventory:
            test = True
            x+=1

    if x == (len(ingredient_list)):
        return True
    else:
        return False

def verify_victory(inventory):
    victory = False

    for item in inventory:
        if item.name == "seringue":
            victory = True
            break

    return victory

def end_game(screen, mac_gyver):
    end_screen = True
    screen = pygame.display.set_mode((500, 400))
    victory = verify_victory(mac_gyver.inventory)

    if victory == True:
        background = pygame.image.load("package/ressource/win.png").convert()
    else:
        background = pygame.image.load("package/ressource/lose.png").convert()

    background = pygame.transform.scale(background , (500, 400))

    screen.blit(background, (0, 0))

    pygame.display.flip()

    while end_screen == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                end_screen = False
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    end_screen = False
