#!/usr/bin/python3

import pygame#import pygame for 2d and image
from pygame.locals import *#import constante pygame

import functions
import game

pygame.init()#initialize pygame

def main():
    main_menu = True#initialise main_menu to true

    pygame.key.set_repeat(200, 200)#enabled key repeat

    screen = pygame.display.set_mode((500, 400))#initialize screen
    pygame.display.set_caption("Labyrinth")#rename screen


    while main_menu:#main menu

        if functions.main_menu(screen) != False:#if the function main_menu() return true
            game.game(screen)#charged game

        else:#else
            break#quit 
if __name__ == "__main__":
    main()
