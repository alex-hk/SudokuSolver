class SSolve(object):
    def __init__(self, filename):
        self.file = open(filename)
        self.nons = ['0' for row in range(9)]

    def fillArr(self):
        row = 0
        for line in f:
            self.nons[row] = line
            row++
        self.nons

    def checkHor(self, row, val):
        return val in self.nons[row]

    def checkVir(self, col, val):
        for i in range(0,9):
            if self.nons[i][col] == val:
                return True
        return False

