from SSolve import SSolve

filename = "data/easy"
extension = ".txt"

print "Welcome to Aleksandar Veselinovic's Sudoku Solver"
print "The program runs at a specified speed"
print "1 is one second, .5 is half a second, below 0 is press to continue"
speed = raw_input("Please enter a speed: ")

for num in range(1,5):
    fname = filename + str(num) + extension
    x = SSolve(fname, float(speed))
    x.initSsq()
    x.calcMarks()
    x.solve()
    raw_input("Press Enter to continue...")

print "Thank you for using my program"
