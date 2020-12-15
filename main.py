import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from game import Game

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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    new_game = Game(5)
    print(new_game.get_possible_moves())
    new_game.move_played(0,0)
    new_game.move_played(0,1)
    new_game.move_played(1,0)
    new_game.move_played(1,1)
    new_game.move_played(2,0)
    new_game.move_played(3,1)
    new_game.move_played(3,0)
    sys.exit(app.exec_())
