#!/usr/bin/python3

import pygame
from pygame.locals import *

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
