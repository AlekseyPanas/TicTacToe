import pygame


class Button:
    def __init__(self, top_left_corner, size, image):
        # Position of top left corner of button.
        self.top_left = top_left_corner
        # Width/height of image and the loaded image.
        self.size = size
        self.image = image

        # Image contains 2 states of the button. These 2 surfaces will hold each state.
        self.static = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.hover = pygame.Surface(self.size, pygame.SRCALPHA, 32)

        self.static.blit(self.image, (0, 0))
        self.hover.blit(self.image, (0, -self.size[1]))

        self.button_state = "static"

    def draw(self, screen):
        screen.blit(self.hover if self.button_state == "hover" else self.static, self.top_left)

    def is_hover(self, pos):
        self.button_state = "hover" if pygame.Rect(self.top_left, self.size).collidepoint(pos) else "static"

    def is_clicked(self, pos):
        return pygame.Rect(self.top_left, self.size).collidepoint(pos)
