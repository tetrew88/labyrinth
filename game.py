import pygame
from pygame.locals import *

import fonctions

from classe import *

def Game(screen):
    victory = False
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

    list_object = fonctions.create_object_from_list(list_object)

    for item in list_object:
        item.obtain_aleatory_position(labyrinth.world)
        if item.state == True:
            labyrinth.world[item.position.x][item.position.y] = "o"


    screen = pygame.display.set_mode((width_window, lenght_window))

    play = 1
    while play:
        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "m"

        labyrinth.display_world(mac_gyver, gardien, wall, floor, screen)

        for item in list_object:
            if item.state == True:
                item.display_object(screen)
                if mac_gyver.position.x == item.position.x and mac_gyver.position.y == item.position.y:
                    mac_gyver.pick_up_object(item)
                    labyrinth.world[item.position.x][item.position.y] = "0"

        mac_gyver.display_inventory(screen)

        
        if fonctions.verify_recipe(list_object, mac_gyver.inventory) == True:
            mac_gyver.craft_object(list_object)

        pygame.display.flip()

        labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] = "0"

        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mac_gyver.move_personnage("left", labyrinth.world)
                elif event.key == K_UP:
                    mac_gyver.move_personnage("up", labyrinth.world)
                elif event.key == K_RIGHT:
                    mac_gyver.move_personnage("right", labyrinth.world)
                elif event.key == K_DOWN:
                    mac_gyver.move_personnage("down", labyrinth.world)

        if labyrinth.world[mac_gyver.position.x][mac_gyver.position.y] == "g":
            fonctions.end_game(screen, mac_gyver)
            play = False
