import pygame
pygame.init()


class Menu:
    def __init__(self):
        pass

    def run_menu(self, screen):
        font = pygame.font.SysFont("Impact", 120, False)
        text = font.render("Tic-Tac-Toe", False, (255, 255, 255))
        screen.blit(text, (30, 0))
        pygame.display.update()
