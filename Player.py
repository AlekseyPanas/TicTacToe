import pygame
import Globals
import random
import copy


class Player:
    def __init__(self, name):
        # Is the player playing with Xs or Os. Determined by game.
        self.value = None
        self.name = name

    def move(self, board):
        return 1, 1


class User(Player):
    def __init__(self, name):
        super().__init__(name)

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
        pos = (random.randint(0, 2), random.randint(0, 2))
        while not board[pos[0]][pos[1]] == 0:
            pos = (random.randint(0, 2), random.randint(0, 2))
        return pos


class Minimax(Player):
    def move(self, board):
        # Checks if its the first turn and automatically takes center tile
        if Globals.is_board_blank(board):
            return random.randint(0, 2), random.randint(0, 2)

        else:
            # The value of the opponent
            self.other_value = 2 if self.value == 1 else 1

            # All the decision values
            decisions = self.minimax(board)

            # Finds highest value
            top_decision_value = max(decisions)

            # Stores positions of top values in decisions list
            top_decision_positions = []

            # Finds the positions of top values
            for idx, dec in enumerate(decisions):
                if dec == top_decision_value:
                    top_decision_positions.append(idx)

            # Stores the best moves (If there are multiple tied for first, it'll go random
            correct_moves = []

            # Counts the empty spaces to determine which empty space the correct move is on
            empty_space_count = 0

            # Goes through board and finds the board position of the correct moves
            for idx, row in enumerate(board):
                for idx2, col in enumerate(row):
                    # Finds empty space
                    if col == 0:
                        # Checks if this empty space is one of the correct moves
                        if empty_space_count in top_decision_positions:
                            correct_moves.append([idx, idx2])
                        # Increments count
                        empty_space_count += 1

            final_choice = random.choice(correct_moves)
            return final_choice[0], final_choice[1]

    def minimax(self, board, depth=0):
        depth_copy = depth

        # Checks if game is won.
        if Globals.check_win(self.value, board):
            return 10 - depth_copy
        elif Globals.check_win(self.other_value, board):
            return -10 - depth_copy
        elif Globals.check_tie(board):
            return 0 - depth_copy
        else:
            # List of all possible moves and board scenarios
            move_list = []

            # Checks for empty spots on board and appends a new state
            for idx, row in enumerate(board):
                for idx2, col in enumerate(row):
                    if col == 0:
                        board_copy = copy.deepcopy(board)
                        board_copy[idx][idx2] = self.value if depth % 2 == 0 else self.other_value
                        move_list.append(copy.deepcopy(board_copy))

            if depth == 0:
                return [self.minimax(x, copy.deepcopy(depth_copy) + 1) for x in move_list]
            if not depth == 0:
                if depth % 2 == 0:
                    return max([self.minimax(x, copy.deepcopy(depth_copy) + 1) for x in move_list])
                else:
                    return min([self.minimax(x, copy.deepcopy(depth_copy) + 1) for x in move_list])
