import pygame
import Button
import Globals
pygame.init()


class Menu:
    def __init__(self):
        self.quit_button = Button.Button((200, 200), (200, 100), Globals.quit_image)

    def run_menu(self, screen, events):
        # Updates buttons
        for event in events:
            # Checks for hover event using mouse pos
            if event.type == pygame.MOUSEMOTION:
                self.quit_button.is_hover(event.pos)
            # Checks for clicks and
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Draws title text
        font = pygame.font.SysFont("Impact", 120, False)
        text = font.render("Tic-Tac-Toe", False, (255, 255, 255))
        screen.blit(text, (20, 0))

        # Draws buttons
        self.quit_button.draw(screen)

        pygame.display.update()
