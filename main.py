import pygame
import Game
import Player
import Globals
import Menu

SCREEN_SIZE = (600, 680)
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF)

MENU = Menu.Menu()
GAME = Game.Game(Player.User(), Player.Randomer())

while Globals.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Globals.running = False

    if Globals.gamestate == "game":
        GAME.run_game(screen)
    else:
        MENU.run_menu()
