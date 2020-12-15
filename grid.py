import random
from cell import Cell

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

    def get_available_cells(self):
        """
        Returns the cells that are still currently active
        """
        arr = []
        for row in self.grid:
            for cell in row:
                if cell.is_active:
                    arr.append(cell)
        return arr

    def __repr__(self):
        return repr(self.grid)

    def __str__(self):
        matrix = self.get_matrix_of_ticks()
        my_str = ""
        for row in matrix:
            my_str += str(row)
            my_str += "\n"
        return my_str
