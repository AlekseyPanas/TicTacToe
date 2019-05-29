import pygame
import random
import Exception
import time
import Globals


class Game:
    def __init__(self, player1, player2):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        # 2 class instances of players.
        self.p1 = player1
        self.p2 = player2

        # Assigns X or O to players
        pool = [1, 2]
        choice = random.choice(pool)
        pool.remove(choice)
        self.p1.value = choice
        self.p2.value = pool[0]

        # Determines who's turn it is first
        self.current_player = random.choice((self.p1, self.p2))

        # The player who won
        self.winner = None

    def run_game(self, screen):
        screen.fill((55, 55, 55))
        self.draw_grid(screen)

        # Looks for 1s and places an X. Looks for 2s in board and places Os
        for idx1, row in enumerate(self.board):
            for idx2, col in enumerate(row):
                if col == 1:
                    self.draw_x((idx2 * 200, idx1 * 200), screen)
                elif col == 2:
                    self.draw_o((idx2 * 200, idx1 * 200), screen)

        # Draws text at bottom of screen

        pygame.display.update()

        # Runs the game
        ###############
        if self.winner is None:
            # Waits a little bit between each turn
            time.sleep(.3)

            # Calls the player move function which returns position on board
            mark_pos = self.current_player.move(self.board)

            # Crashes game if X or O is placed on an occupied tile. Player class must ensure this does not happen
            if not self.board[mark_pos[0]][mark_pos[1]] == 0 and not mark_pos[0] == -1:
                raise Exception.OccupiedTileException

            self.place_mark(self.current_player.value, mark_pos)

            # Checks for wins and runs the game over procedure.
            if self.check_win(self.current_player.value):
                self.winner = self.current_player

            # Changes the turn to the next player
            self.current_player = self.p1 if self.current_player == self.p2 else self.p2
        else:
            print("Yo")

    # Places an 1 (x) or a 2 (O) in the given board position
    def place_mark(self, value, position):
        self.board[position[0]][position[1]] = value

    # Returns a boolean based on whether the game is won or not
    def check_win(self, value):
        # Checks all board win conditions
        if self.board[1][1] == value:
            if (self.board[0][0] == value and self.board[2][2] == value) or (
                    self.board[0][2] == value and self.board[2][0] == value) or (
                    self.board[1][0] == value and self.board[1][2] == value) or (
                    self.board[0][1] == value and self.board[2][1] == value):
                return True

        elif self.board[0][0] == value:
            if (self.board[0][1] == value and self.board[0][2] == value) or (
                    self.board[1][0] == value and self.board[2][0] == value):
                return True

        elif self.board[2][2] == value:
            if (self.board[2][0] == value and self.board[2][1] == value) or (
                    self.board[1][2] == value and self.board[0][2] == value):
                return True
        return False

    # Draws an x given the top left position of the desired drawing location
    @staticmethod
    def draw_x(top_left, screen):
        pygame.draw.line(screen, (255, 255, 255),
                         (top_left[0] + 30, top_left[1] + 30), (top_left[0] + 160, top_left[1] + 160), 8)
        pygame.draw.line(screen, (255, 255, 255),
                         (top_left[0] + 160, top_left[1] + 30), (top_left[0] + 30, top_left[1] + 160), 8)

    # Draws an o given the top left position of the desired drawing location
    @staticmethod
    def draw_o(top_left, screen):
        pygame.draw.circle(screen, (255, 255, 255), (top_left[0] + 100, top_left[1] + 100), 70, 6)

    # Draws tic tac toe grid
    @staticmethod
    def draw_grid(screen):
        pygame.draw.line(screen, (200, 200, 200), (0, 200), (600, 200), 5)
        pygame.draw.line(screen, (200, 200, 200), (0, 400), (600, 400), 5)

        pygame.draw.line(screen, (200, 200, 200), (200, 0), (200, 600), 5)
        pygame.draw.line(screen, (200, 200, 200), (400, 0), (400, 600), 5)

        pygame.draw.line(screen, (100, 100, 100), (0, 640), (600, 640), 90)
