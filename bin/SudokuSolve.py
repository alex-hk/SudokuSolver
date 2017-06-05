import os
import Ssquare

class SudokuSolver(object):

    # Initialize file, 9x9 array of Ssquare objects
    # (View Ssquare.py for more info on Ssquare object)
    def __init__(self,fname):
        return

    # Solve puzzle
    # Steps:
    # 1. Mark each possible number in each square
    #   i. If square has only one number, set Ssquare's actual to that number
    #     1. Check each Ssquare in horizontal, vertical, and 3x3 square
    #        and remove that number from each
    # 2. Check 
    def solve(self):
        return

    # Checks horizontal at row for similar values
    # Mark set if it adds marks or removes marks
    # Sarr is array of sudoku squares
    def checkHor(self, row, mark=0, sarr):
        if mark:
    
        return

    def checkVer(self, mark=0):
        return

    def checkNon(self, mark=0):
        return
    
    def validate(self, fname):
        return



dirpath = "./data/"
solvpath = "./solve/"

for filename in os.listdir('data'):
    f = open(filename, 'r')

