import os
import time
from Sbox import Sbox

class SSolve(object):

    # Initialize file, 9x9 array of Ssquare objects
    # (View Ssquare.py for more info on Ssquare object)
    def __init__(self, filename, speed, spnums):
        self.file = open(filename)
        self.ssq = [ [Sbox() for row in range(9)] for row in range(9)]
        self.speed = speed
        self.iterMarks  = 0
        self.iterSolve  = 0
        self.iterRemove = 0
        self.trials = 0
        self.totaltrials = 200
        self.showPnums  = spnums
        #self.


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

    def printPuzzle(self):
        row = 0
        col = 0
        for list in self.ssq:
            for box in list:
                print "{0:d} ".format(box.actual),
            print
        print

    def printPnums(self):
        for list in self.ssq:
            for box in list:
                print box.pnums,
            print
        print

    def printBoth(self):
        for list in self.ssq:
            for box in list:
                print "{0:d} ".format(box.actual),
            print "\t",
            for box2 in list:
                print box2.pnums,
                if len(box2.pnums) < 3:
                    print "\t",
                print "\t",
            print
        print


    def solve(self):
        self.calcMarks()
        self.checkAll(False)

    # Solve puzzle
    # Steps:
    # 1. Mark each possible number in each square
    #   i. If square has only one number, set Ssquare's actual to that number
    #     1. Check each Ssquare in horizontal, vertical, and 3x3 square
    #        and remove that number from each
    # 2. Check 
    def checkAll(self, finish = False, count=0):
        while count < 81 and (self.trials < self.totaltrials):
            self.trials+=1
            count = 0
            for row in range(0,9):
                for col in range(0,9):
                    if self.ssq[row][col].actual == 0:
                        for val in self.ssq[row][col].pnums:
                            if self.checkifSingle(row, col, val):
                                os.system('clear')
                                self.ssq[row][col].actual = val
                                del self.ssq[row][col].pnums[:]
                                self.removeAll(row, col, val)
                                if self.showPnums:
                                    self.printBoth()
                                else:
                                    self.printPuzzle()
                                #self.printPnums()
                                if self.speed > 0:
                                    time.sleep(self.speed)
                                else:
                                    if self.speed == 0:
                                        raw_input("Press Enter to continue...")
            #                    print "NOT SINGLE\n"
                            
                    else:
             #           print "Value is not 0"
                        count+=1

            #print count
        #self.printPuzzle()

    def removeAll(self, row, col, val):
        srow = row / 3
        scol = col / 3
        box = (srow*3) + scol
        self.removeVer(col, val)
        self.removeHor(row, val)
        self.removeBox(box, val)

    # Checks if value exists in horizontal
    def checkHor(self, row, val, mark=False):
        count = 0
        for i in range(0,9):
            if mark:
                self.iterSolve+=1
          #     print "Checking horizontal if value is single"
                if self.ssq[row][i].actual == 0 and val in self.ssq[row][i].pnums:
                    count+=1
            else:
                self.iterMarks+=1
                if self.ssq[row][i].actual == val:
                    return True
        if mark:
            return count == 1
        else:
            return False

    # Check if value exists in vertical
    def checkVer(self, col, val, mark=False):
        count=0
        for i in range(0,9):
            if mark:
                self.iterSolve+=1
         #      print "Checking vertical if value is single"
                if self.ssq[i][col].actual == 0 and val in self.ssq[i][col].pnums:
                    count+=1
            else:
                self.iterMarks+=1
                if self.ssq[i][col].actual == val:
                    return True
        if mark:
            return count == 1
        else:
            return False
    
    def checkifSingle(self, row, col, val):
        srow = row / 3
        scol = col / 3
        box = (srow*3) + scol
        #print "Checking if Single"
        if self.checkbox(box, val, True) or self.checkHor(row, val, True) or self.checkVer(col, val, True):
            #print "Value {0:d} single".format(val)
            return True
        return False

    # Check if value exists in box
    def checkbox(self, box, val, mark=False):
        srow = (box/3)*3
        scol = (box%3)*3
        count = 0
        for row in range(srow, srow+3):
            for col in range(scol, scol+3):
           #     print "Stuff"
                if mark is True:
                    self.iterSolve+=1
                    #print "Checking box if value is single"
                    if self.ssq[row][col].actual == 0 and val in self.ssq[row][col].pnums:
                        #print "Box contains value"
                        count+=1
                else:
                    self.iterMarks+=1
                    if self.ssq[row][col].actual == val:
                        return True
        if mark:
            return count == 1
        else:
            return False

    def removeVer(self, col, val):
        for i in range(0,9):
            self.iterRemove+=1
            if val in self.ssq[i][col].pnums:
                self.ssq[i][col].removePnum(val)

    def removeHor(self, row, val):
        for i in range(0,9):
            self.iterRemove+=1
            if val in self.ssq[row][i].pnums:
                self.ssq[row][i].removePnum(val)

    def removeBox(self, box, val):
        srow = (box/3)*3
        scol = (box%3)*3
        for row in range(srow, srow+3):
            for col in range(scol, scol+3):
                self.iterRemove+=1
                if val in self.ssq[row][col].pnums:
                    self.ssq[row][col].removePnum(val)


    def validate(self):
        for row in range(0,9):
            for col in range(0,9):
                box  = (row/3)*3 + (col/3)
                val = self.ssq[row][col].actual
                if not self.boxValid(box, val) and not self.horValid(row, val) and not self.verValid(col, val):
                    return False
        return True

    def boxValid(self, box, val):
        srow = (box/3)*3
        scol = (box%3)*3
        count = 0
        for row in range(srow, srow+3):
            for col in range(scol, scol+3):
                if self.ssq[row][col].actual == val:
                    count+=1
        return count == 1
    
    def horValid(self, row, val):
        count = 0
        for i in range(0,9):
            if self.ssq[row][i].actual == val:
                count+=1
        return count == 1

    def verValid(self, col, val):
        count = 0
        for i in range(0,9):
            if self.ssq[i][col].actual == val:
                count+=1
        return count == 1


    def calcMarks(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.ssq[row][col].actual == 0:
                    srow = row / 3
                    scol = col / 3
                    box = (srow*3) + scol
                    for val in range(1,10):
                        if not self.checkbox(box, val, False) and not self.checkHor(row, val, False) and not self.checkVer(col, val, False):
                            self.ssq[row][col].addPnum(val)

                        self.iterMarks+=1




#dirpath = "./data/"
#solvpath = "./solve/"

#for filename in os.listdir('data'):
#:    f = open(filename, 'r')

