import pygame
from pygame.locals import *

from package.classe import *

def Game(screen):
    width_window = int(Labyrinth.WIDTH_TILE * Labyrinth.WIDTH)
    lenght_window = int(Labyrinth.LENGHT_TILE * Labyrinth.LENGHT)
    
    list_object = ["ether", "tube_plastique", "aiguille"]

    floor = Floor()
    wall = Wall()
    
    labyrinth = Labyrinth("level")
    mac_gyver = Personnage("MacGyver", 15, labyrinth.start_position)
    gardien = Personnage("Gardien", 15, labyrinth.goal_position)

    labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"
    labyrinth.world[gardien.position.x][gardien.position.y] = "g"

    x=0
    for item in list_object:
        list_object[x] = Object(item, True, labyrinth.world)
        if list_object[x].state == True:
            labyrinth.world[list_object[x].position.x][list_object[x].position.y] = "o"
        x+=1

    screen = pygame.display.set_mode((width_window, lenght_window))

    play = 1
    while play:
        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"

        x = 0
        while x < labyrinth.WIDTH:
            y = 0
            while y < labyrinth.LENGHT:
                if labyrinth.world[x][y] == "0":
                    screen.blit(floor.sprite, (y * labyrinth.WIDTH_TILE, x * labyrinth.LENGHT_TILE))
                elif labyrinth.world[x][y] == "m":
                    screen.blit(mac_gyver.sprite, (y * labyrinth.WIDTH_TILE, x * labyrinth.LENGHT_TILE))
                elif labyrinth.world[x][y] == "g":
                    screen.blit(gardien.sprite, (y * labyrinth.WIDTH_TILE, x * labyrinth.LENGHT_TILE))
                elif labyrinth.world[x][y] == "w":
                    screen.blit(wall.sprite, (y * labyrinth.WIDTH_TILE, x * labyrinth.LENGHT_TILE))
               
                y+=1
            x+=1

        for item in list_object:
            if item.state == True:
                item.display_object(screen)

        pygame.display.flip()

        if mac_gyver.position.x == gardien.position.x and mac_gyver.position.y == gardien.position.y:
            print("perdu")
            play = 0


        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "0"

        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mac_gyver.position = mac_gyver.move_personnage("left", labyrinth.world)
                elif event.key == K_UP:
                    mac_gyver.position = mac_gyver.move_personnage("up", labyrinth.world)
                elif event.key == K_RIGHT:
                    mac_gyver.position = mac_gyver.move_personnage("right", labyrinth.world)
                elif event.key == K_DOWN:
                    mac_gyver.position = mac_gyver.move_personnage("down", labyrinth.world)

        for item in list_object:
            if mac_gyver.position.x == item.position.x and mac_gyver.position.y == item.position.y:
                mac_gyver.pick_up_object(item)
                labyrinth.world[item.position.x][item.position.y] = "0"
                item.state= False
