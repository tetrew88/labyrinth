import pygame
from pygame.locals import *

from package.classe import *

def Game(screen):
    width_tile = 43
    lenght_tile = 32

    width_window = int(lenght_tile * Labyrinth.WIDTH + 200)
    lenght_window = int(width_tile * Labyrinth.LENGHT)

    labyrinth = Labyrinth("level")

    mac_gyver = Personnage("MacGyver", 15, labyrinth.start_position)
    gardien = Personnage("Gardien", 15, labyrinth.goal_position)

    screen = pygame.display.set_mode((width_window, lenght_window))
    
    play = 1
    while play:
        x = 0
        while x < labyrinth.WIDTH:
            y = 0
            while y < labyrinth.LENGHT:
                if Position(x, y) == mac_gyver.position:
                    screen.blit(mac_gyver.sprite, mac_gyver.position)
                elif Position(x, y) == gardien.position:
                    screen.blit(gardien.sprite, gardien.position)
                elif isinstance(labyrinth.world[x][y], Wall):
                    pass
                else:
                    pass

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0

