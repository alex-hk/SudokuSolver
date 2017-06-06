import os
from Sbox import Sbox

class SSolve(object):

    # Initialize file, 9x9 array of Ssquare objects
    # (View Ssquare.py for more info on Ssquare object)
    def __init__(self, filename):
        self.file = open(filename)
        self.ssq = [ [Sbox() for row in range(9)] for row in range(9)]


    def initSsq(self):
        row = 0
        col = 0
        for line in self.file:
            col = 0
            for char in line:
                if char != '\n':
                    self.ssq[row][col].actual = int(char)
                col+=1
            row+=1


    # Solve puzzle
    # Steps:
    # 1. Mark each possible number in each square
    #   i. If square has only one number, set Ssquare's actual to that number
    #     1. Check each Ssquare in horizontal, vertical, and 3x3 square
    #        and remove that number from each
    # 2. Check 
    def solve(self, finish = False):
        finish = True
        self.calcMarks()
        for row in range(0,9):
            for col in range(0,9):
                if self.ssq[row][col].actual == 0:
                    for val in self.ssq[row][col].pnums:
                        if self.checkifSingle(row, col, val):
                            self.ssq[row][col].actual = val
                        else:
                            finsh = False
        if not finish:
            self.solve(finish)

    # Checks if value exists in horizontal
    def checkHor(self, row, val, mark=False):
        count = 0
        for i in range(0,9):
            if mark:
                if self.ssq[row][i].actual == 0 and val in self.ssq[row][i].pnums:
                    count+=1
            else:
                if self.ssq[row][i].actual == val:
                    return True
        if mark:
            return count > 1
        return False

    # Check if value exists in vertical
    def checkVer(self, col, val, mark=False):
        count=0
        for i in range(0,9):
            if mark:
                if self.ssq[i][col].actual == 0 and val in self.ssq[i][col].pnums:
                    count+=1
            else:
                if self.ssq[i][col].actual == val:
                    return True
        if mark:
            return count > 1
        return False
    
    def checkifSingle(self, row, col, val):
        srow = row / 3
        scol = col / 3
        box = (srow*3) + scol
        if self.checkbox(box, val, True) and self.checkHor(row, val, True) and self.checkVer(col, val, True):
            return True
        return False

    # Check if value exists in box
    def checkbox(self, box, val, mark=False):
        srow = (box/3)*3
        scol = (box%3)*3
        count = 0
        for row in range(srow, 3):
            for col in range(scol, 3):
                if mark:
                    if self.ssq[row][col].actual != 0 and val in self.ssq[row][col].pnums:
                        count+=1
                else:
                    if self.ssq[row][col].actual == val:
                        return True
        if mark:
            return count > 1
        return False

    # Check if done
    def validate(self, fname):
        return

    def Solve(self, row, col):
        srow = row / 3
        scol = col / 3
        box = (srow * 3) + scol
        if self.sarr[row][col] != '0':
            for i in range(1,10):
                return
                #if checkBox(
    
    def calcMarks(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.ssq[row][col].actual == 0:
                    srow = row / 3
                    scol = col / 3
                    box = (srow*3) + scol
                    for val in range(1,10):
                        if not self.checkbox(box, val) and not self.checkHor(row, val) and not self.checkVer(col, val):
                            self.ssq[row][col].addPnum(val)




#dirpath = "./data/"
#solvpath = "./solve/"

#for filename in os.listdir('data'):
#:    f = open(filename, 'r')

