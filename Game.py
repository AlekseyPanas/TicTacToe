import pygame
import random
import Exception
import time
import Globals


class Game:
    def __init__(self, player1, player2, start=0):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        # 2 class instances of players.
        self.p1 = player1
        self.p2 = player2

        if start == 0:
            # Assigns X or O to players
            pool = [1, 2]
            choice = random.choice(pool)
            pool.remove(choice)
            self.p1.value = choice
            self.p2.value = pool[0]
        else:
            if start == 1:
                self.p1.value = 1
                self.p2.value = 2
            elif start == 2:
                self.p2.value = 1
                self.p1.value = 2

        # Determines who's turn it is first
        self.current_player = self.p1 if self.p1.value == 1 else self.p2

        # The player who won
        self.winner = None

    def run_game(self, screen, events):
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
        text_surface = pygame.font.SysFont("Pacific", 60).render(self.current_player.name + "'s turn", False,
                                                                 (255, 255, 255))

        screen.blit(text_surface, ((600 - text_surface.get_width()) / 2, 610))

        # Runs if game is over
        if self.winner is not None:
            # Displays the winner in the middle of screen.
            if not self.winner == "tie":
                text_surface = pygame.font.SysFont("Impact", 70, False).render(self.winner.name + " Wins!", False,
                                                                              (90, 255, 90))
            else:
                text_surface = pygame.font.SysFont("Impact", 70, False).render("Its a Tie!", False,(90, 255, 90))

            screen.blit(text_surface, ((600 - text_surface.get_width()) / 2, 30))

            # Checks for click event to end game
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Globals.MENU.menu_state = "menu"
                    Globals.gamestate = "menu"

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
            if Globals.check_win(self.current_player.value, self.board):
                self.winner = self.current_player

            elif Globals.check_tie(self.board):
                self.winner = "tie"

            # Changes the turn to the next player
            self.current_player = self.p1 if self.current_player == self.p2 else self.p2

    # Places an 1 (x) or a 2 (O) in the given board position
    def place_mark(self, value, position):
        self.board[position[0]][position[1]] = value

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
