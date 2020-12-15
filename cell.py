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
