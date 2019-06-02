import pygame
import Button
import Globals
import Game
import Player
pygame.init()


class Menu:
    def __init__(self):
        self.pvp_button = Button.Button((200, 200), (200, 100), Globals.pvp_image)
        self.pve_button = Button.Button((200, 320), (200, 100), Globals.pve_image)
        self.quit_button = Button.Button((200, 440), (200, 100), Globals.quit_image)

        # Background color
        self.shade = 0
        # The way the shade changes
        self.change = 1

    def run_menu(self, screen, events):
        # Updates buttons
        for event in events:
            # Checks for hover event using mouse pos
            if event.type == pygame.MOUSEMOTION:
                self.quit_button.is_hover(event.pos)
                self.pve_button.is_hover(event.pos)
                self.pvp_button.is_hover(event.pos)

            # Checks for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quits game
                if self.quit_button.is_clicked(event.pos):
                    Globals.running = False
                # Starts a player vs computer match
                elif self.pve_button.is_clicked(event.pos):
                    Globals.GAME = Game.Game(Player.Minimax("Computer"), Player.User("Player"))
                    Globals.gamestate = "game"
                # Starts a player vs player match
                elif self.pvp_button.is_clicked(event.pos):
                    Globals.GAME = Game.Game(Player.User("Player 1"), Player.User("Player 2"))
                    Globals.gamestate = "game"

        # Fills screen with color
        screen.fill([int(self.shade) for x in range(3)])

        # Draws title text
        font = pygame.font.SysFont("Impact", 120, False)
        text = font.render("Tic-Tac-Toe", False, (255, 255, 255))
        screen.blit(text, (20, 0))

        # Draws buttons
        self.quit_button.draw(screen)
        self.pve_button.draw(screen)
        self.pvp_button.draw(screen)

        pygame.display.update()

        # Adjusts shade.
        if self.shade >= 100:
            self.change = -.07
        elif self.shade <= 0:
            self.change = .07
        self.shade += self.change
