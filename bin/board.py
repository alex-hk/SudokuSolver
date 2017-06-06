from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from SSolver import SSolve

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class BoardUI(Frame):
    
    def __init__(self, parent, game):
        self.parent = parent
        self.game = game
        Frame.__init__(self, parent)

        self.row = 0
        self.col = 0

        self.initGUI()

    def initGUI(self):
        self.parent.title("Sudoku Solver - Aleksandar Veselinovic")
        
    
