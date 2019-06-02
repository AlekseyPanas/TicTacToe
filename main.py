import pygame
import Globals

SCREEN_SIZE = (600, 680)
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)

# Conversions
Globals.quit_image = Globals.quit_image.convert_alpha()
Globals.pve_image = Globals.pve_image.convert_alpha()
Globals.pvp_image = Globals.pvp_image.convert_alpha()

while Globals.running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            Globals.running = False

    if Globals.gamestate == "game":
        Globals.GAME.run_game(screen, events)
    else:
        Globals.MENU.run_menu(screen, events)
