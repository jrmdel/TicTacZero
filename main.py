import sys
import random
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    """
    Used to design the PyQt interface
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("TicTacZero")
        self.init_ui()

    def init_ui(self):
        """
        Basic init
        """
        pass





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





class Grid:
    """
    The grid of the game
    """
    def __init__(self, size, number_of_holes):
        print(f"Size = {size}, holes = {number_of_holes}")
        self.grid = Grid.create_grid(size, number_of_holes)
        print(self)

    @staticmethod
    def create_grid(size, n_holes):
        """
        Creates a grid of cells
        """
        # Create a grid
        possible_cells = []
        rows = []
        for i in range(size):
            cols = []
            for j in range(size):
                cols.append(Cell(i,j))
                possible_cells.append(size*i+j)
            rows.append(cols)
        # Assign holes to some cells
        print(possible_cells)
        for _ in range(n_holes):
            h = random.choice(possible_cells)
            print(h)
            possible_cells.remove(h)
            rows[h//size][h%size].set_cell_to_hole()
        return rows

    def insert_move(self, row, col, tick):
        """
        Inserts the move played to the cell
        """
        self.grid[row][col].set_player_tick(tick)

    def get_matrix_of_ticks(self):
        """
        Returns a matrix containing only the tick values. Useful for evaluation purposes.
        """
        return [[cell.get_tick_value() for cell in row] for row in self.grid]

    def __repr__(self):
        return repr(self.grid)

    def __str__(self):
        matrix = self.get_matrix_of_ticks()
        s = ""
        for row in matrix:
            s += str(row)
            s += "\n"
        return s





class Cell:
    """
    A cell from the grid
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_active = True
        self.is_hole = False
        self.tick = " "

    def set_cell_to_hole(self):
        """
        Defines the cell as an inactive hole
        """
        self.tick = "H"
        self.is_hole = True
        self.is_active = False

    def set_player_tick(self, tick):
        """
        Changes the tick value of the cell and makes it inactive
        """
        self.tick = tick
        self.is_active = False

    def get_tick_value(self):
        """
        Getter for the tick
        """
        return self.tick

    def __repr__(self):
        return f"<Cell({self.x},{self.y}):Active={self.is_active}/Hole={self.is_hole}/Tick={self.tick}>"





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    new_game = Game(5)
    new_game.move_played(0,0)
    new_game.move_played(0,1)
    new_game.move_played(1,0)
    new_game.move_played(1,1)
    new_game.move_played(2,0)
    new_game.move_played(3,1)
    new_game.move_played(3,0)
    sys.exit(app.exec_())