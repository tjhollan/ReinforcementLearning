import numpy as np
import copy

#########################
#  Checkers game board  #
#########################

class Game():

    def __init__(self):
        self.empty_space = 0
        self.players = ['R', 'B']
        # Normal tokens are valued at 1 and -1, kings are 2 and -2
        self.token_values = {'R': 1, 'B': -1, 'RK': 2, 'BK': -2}
        self.tokens = {1: 'R', -1:'B', 2: 'RK', -2:'BK', self.empty_space: '  '}
        self.adjacency_dict = self.build_adjacency_dict(self.valid_spaces())
        self.reset_game()

    def build_adjacency_dict(self, val_spaces):
        adj_dict = {}
        for spot in val_spaces:
            adj_dict[spot] = []
            if spot+7 in val_spaces:
                adj_dict[spot].append(spot+7)
            if spot+9 in val_spaces:
                adj_dict[spot].append(spot+9)
            if spot-7 in val_spaces:
                adj_dict[spot].append(spot-7)
            if spot-9 in val_spaces:
                adj_dict[spot].append(spot-9)
        return adj_dict

    def reset_game(self):
        # Sets all board positions to 0
        self.gameboard = np.array([self.empty_space] * 64)
        # Sets all Red pieces
        for i in range(3):
            for j in range(1-i%2,8,2):
                self.gameboard[i*8+j] = self.token_values[self.players[0]]
        # Sets all Black pieces
        for i in range(5,8):
            for j in range(1-i%2,8,2):
                self.gameboard[i*8+j] = self.token_values[self.players[1]]
        # Sets the previous player value to empty
        self.previous_player = None
    
    def valid_moves(self, state, player = None):
        # Returns a list of valid moves for the player
        if player == self.previous_player:
            return []
        else:
            return []
    
    def valid_spaces(self):
        spaces = []
        for i in range(8):
            for j in range(1-i%2,8,2):
                spaces.append(i*8+j)
        return spaces
       
    def make_move(self, move, player):
        if move in self.valid_moves(self.gameboard, player):
            # Sets the value at the move position to the player value
            self.gameboard[move-1] = self.player_values[player]
            self.previous_player = player
    
    def get_game_state(self):
        # Returns a copy of the game board
        return copy.deepcopy(self.gameboard)

    def get_next_player(self):
        if self.previous_player is None:
            return None
        return self.players[0] if self.previous_player == self.players[1] else self.players[1]

    def no_more_moves(self):
        # Checks for valid moves to make

        return False

    def victory_condition(self, player):
        # Returns true if the player has won the game

        return False

    def defeat_condition(self, test_player):
        # Returns false if the player has lost the game

        return False
    
    def draw_condition(self):
        # Checks for draw conditions

        return False
    
    def game_is_over(self):
        # The game is over if a player meets a victory condition or there are no more 
        # valid moves
        return self.victory_condition(self.players[0]) or self.victory_condition(self.players[1]) or self.no_more_moves()
    
    def print_board(self):
        print()
        print(f"———————————————————————")
        for i in range(8):
            for j in range(7):
                print(f"{self.tokens[self.gameboard[i*8+j]]:2}|", end="")
            print(f"{self.tokens[self.gameboard[i*8+7]]:2}")
            print(f"———————————————————————")
        print()
