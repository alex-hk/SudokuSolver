class Sbox(object):

    # pnums: array of possible values for specific square
    # count: number of values in pnums
    # actual: actual value for square
    def __init__(self):
        self.count = 0
        self.pnums = []
        self.actual = 0

    # Changes actual value if val exists (May not work correctly)
    def ssActual(self, val):
        if val:
            self.actual = val
        else:
            return self.actual
    
    # Checks if there is only one value in Pnums
    # If so, value in pnums is actual value
    def ifActual(self):
        return self.count == 1

    # Adds value into pnum if it does not exist
    def addPnum(self, val):
        if val not in self.pnums:
            self.pnums.append(val)
            self.count+=1

    def removePnum(self, val):
        if val in self.pnums:
            self.pnums.remove(val)
            self.count+=-1
