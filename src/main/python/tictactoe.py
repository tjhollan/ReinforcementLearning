import numpy as np
import copy

##########################
# Tic Tac Toe game board #
##########################

class Game():

    def __init__(self):
        self.empty_space = 0
        self.players = ['X', 'O']
        self.player_values = {'X': 1, 'O': 2}
        self.reset_game()

    def reset_game(self):
        # Sets all board positions to 0
        self.gameboard = np.array([self.empty_space] * 9)
        # Sets the previous player value to empty
        self.previous_player = None
    
    def valid_moves(self, state, player = None):
        if player == self.previous_player:
            return []
        else:
            return [x+1 for x in np.where(state == self.empty_space)[0]]
       
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
        for player in self.players:
            if len(self.valid_moves(self.gameboard, player)) > 0:
                return False
        return True

    def victory_condition(self, player):
        # A list of all victory conditions in groups of three
        combos = np.array((0,1,2, 3,4,5, 6,7,8, 0,3,6, 1,4,7, 2,5,8, 0,4,8, 2,4,6))
        # Returns true if the player has any of the winning combinations
        return np.any(np.all(self.player_values[player] == self.gameboard[combos].reshape((-1, 3)), axis=1))

    def defeat_condition(self, test_player):
        for player in self.players:
            if player != test_player and self.victory_condition(player):
                return True
        return False
    
    def draw_condition(self):
        # Check for a winner
        for player in self.players:
            if self.victory_condition(player):
                return False
        # Check for no more moves
        return self.no_more_moves()
    
    def game_is_over(self):
        # The game is over if a player meets a victory condition or there are no more 
        # valid moves
        return self.victory_condition(self.players[0]) or self.victory_condition(self.players[1]) or self.no_more_moves()
    
    def print_board(self):
        display = {self.empty_space: ' ', self.player_values[self.players[0]]: 'X', self.player_values[self.players[1]]: 'O'}
        print()
        print(f"{display[self.gameboard[0]]}|{display[self.gameboard[1]]}|{display[self.gameboard[2]]}")
        print(f"—————")
        print(f"{display[self.gameboard[3]]}|{display[self.gameboard[4]]}|{display[self.gameboard[5]]}")
        print(f"—————")
        print(f"{display[self.gameboard[6]]}|{display[self.gameboard[7]]}|{display[self.gameboard[8]]}")
        print()
