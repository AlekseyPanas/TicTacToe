import pygame
import Game
import Player
import Globals
import Menu

SCREEN_SIZE = (600, 680)
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)

# Conversions
Globals.quit_image = Globals.quit_image.convert_alpha()

MENU = Menu.Menu()
GAME = Game.Game(Player.User(), Player.Randomer())

while Globals.running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            Globals.running = False

    if Globals.gamestate == "game":
        GAME.run_game(screen)
    else:
        MENU.run_menu(screen, events)
