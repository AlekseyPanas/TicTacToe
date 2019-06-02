import pygame
import Menu

running = True

gamestate = "menu"

# images
quit_image = pygame.image.load("quitbutton.png")
pve_image = pygame.image.load("pvebutton.png")
pvp_image = pygame.image.load("pvpbutton.png")

GAME = None
MENU = Menu.Menu()


# Returns a boolean based on whether the game is won or not
def check_win(value, board):
    # Checks all board win conditions
    if board[1][1] == value:
        if (board[0][0] == value and board[2][2] == value) or (
                board[0][2] == value and board[2][0] == value) or (
                board[1][0] == value and board[1][2] == value) or (
                board[0][1] == value and board[2][1] == value):
            return True

    if board[0][0] == value:
        if (board[0][1] == value and board[0][2] == value) or (
                board[1][0] == value and board[2][0] == value):
            return True

    if board[2][2] == value:
        if (board[2][0] == value and board[2][1] == value) or (
                board[1][2] == value and board[0][2] == value):
            return True
    return False


# Checks for tie
def check_tie(board):
    # Checks for tie
    tie = True
    for row in board:
        for col in row:
            if col == 0:
                tie = False
    return tie


def is_board_blank(board):
    # Counts blank spaces
    count = 0

    for row in board:
        for col in row:
            if col == 0:
                count += 1

    # If whole board is blank, returns true
    if count == 9:
        return True
    else:
        return False
