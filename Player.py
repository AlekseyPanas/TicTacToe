import pygame
import Globals
import random


class Player:
    def __init__(self):
        # Is the player playing with Xs or Os. Determined by game.
        self.value = None

    def move(self, board):
        return 1, 1


class User(Player):
    def __init__(self):
        super().__init__()

    # Is called by the Game when the player needs to make a move. This method is responsible for ensuring the position
    # it chooses isn't taken
    def move(self, board):
        click = False
        while not click:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] < 600 and board[int(event.pos[1] / 200)][int(event.pos[0] / 200)] == 0:
                        click = True
                        return int(event.pos[1] / 200), int(event.pos[0] / 200)
                # Allows the game to quit mid turn by returning -1 as a position on the board and by ending the loop.
                elif event.type == pygame.QUIT:
                    Globals.running = False
                    return -1, -1


class Randomer(Player):
    def move(self, board):
        pos = (random.randint(0,2), random.randint(0, 2))
        while not board[pos[0]][pos[1]] == 0:
            pos = (random.randint(0,2), random.randint(0, 2))
        return pos
