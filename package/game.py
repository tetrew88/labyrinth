import pygame
from pygame.locals import *

from package.classe import *

def Game(screen):
    width_window = int(Labyrinth.WIDTH_TILE * Labyrinth.WIDTH)
    lenght_window = int(Labyrinth.LENGHT_TILE * Labyrinth.LENGHT)

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
                if x == mac_gyver.position.x and y == mac_gyver.position.x:
                    screen.blit(mac_gyver.sprite, (x*labyrinth.WIDTH_TILE, y*labyrinth.LENGHT_TILE))
                elif x == gardien.position.x and y == gardien.position.y:
                    screen.blit(gardien.sprite, (x*labyrinth.WIDTH_TILE, y*labyrinth.LENGHT_TILE))
                elif isinstance(labyrinth.world[x][y], Wall):
                    pass
                else:
                    pass
                y += 1
            x += 1

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0

