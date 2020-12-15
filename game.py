import copy
import numpy as np
from grid import Grid

class Game:
    """
    Game class
    """
    def __init__(self, size):
        self.size = size
        self.grid = Grid(size, size*size//5)
        self.turn = 0
        self.winning_alignment = 4

    def player_tick(self):
        """
        Returns the tick string of the current player
        """
        return "X" if self.turn==0 else "O"

    def change_player_turn(self):
        """
        Changes the turn value : 0 or 1
        """
        self.turn = (self.turn+1)%2

    def move_played(self,chosen_x,chosen_y):
        """
        Adds the move to the grid, checks if it is winning and changes turn
        """
        self.grid.insert_move(chosen_x, chosen_y, self.player_tick())
        print(self.grid)
        if self.grid_is_winning():
            print(f"Player {self.turn+1} won !")
        else:
            if len(self.get_possible_moves())==0:
                print("It's a draw !")
            else:
                self.change_player_turn()

    def grid_is_winning(self):
        """
        Evaluates the grid and returns a boolean value if winning
        """
        arr = self.grid.get_matrix_of_ticks()
        matrix = np.array(arr)
        computed_range = len(arr)-self.winning_alignment+1
        success = False
        for i in range(computed_range):
            for j in range(computed_range):
                if Game.evaluate_small_grid(matrix[i:self.winning_alignment+i,j:self.winning_alignment+j]):
                    success = True
        return success

    def get_game_copy(self):
        """
        Returns a copy of the current game
        """
        return copy.deepcopy(self)

    def get_possible_moves(self):
        """
        Returns an array of Cells that haven't been chosen yet
        """
        return self.grid.get_available_cells()


    @staticmethod
    def evaluate_small_grid(matrix):
        """
        Evaluates if there is a winning alignment in this sub-grid
        Returns the corresponding boolean
        """
        len_m = len(matrix)
        rows = ["" for _ in range(len_m)]
        cols = ["" for _ in range(len_m)]
        diags = ["",""]
        for i, row in enumerate(matrix):
            for j, tick in enumerate(row):
                rows[i]+=tick
                cols[j]+=tick
                if i==j:
                    diags[0]+=tick
                elif i+j==len_m-1:
                    diags[1]+=tick
        success = False
        for seq in rows:
            if Game.evaluate_sequence(seq):
                success = True
        if success:
            return True
        for seq in cols:
            if Game.evaluate_sequence(seq):
                success = True
        if success:
            return True
        for seq in diags:
            if Game.evaluate_sequence(seq):
                success = True
        return success

    @staticmethod
    def evaluate_sequence(sequence):
        """
        Evaluates if the sequence contains only the letter X or only the letter O
        Returns the corresponding boolean
        """
        ref = sequence[0]
        if ref not in ("X","O"):
            return False
        flag = True
        for c in sequence:
            if c != ref:
                flag = False
        return flag
