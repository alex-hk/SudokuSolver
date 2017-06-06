from SSolve import SSolve
import time

direct = "data/"
extension = ".txt"
spnums = False
speed = -1
ifspeed = True

def run(diff, numpuzz, spd, spnum):
    for num in range(1,numpuzz+1):
        fname = direct + diff + str(num) + extension
        x = SSolve(fname, float(speed), spnums)
        start = time.time()
        x.initSsq()
        x.calcMarks()
        x.solve()
        end = time.time()
        siter = x.iterSolve
        miter = x.iterMarks
        riter = x.iterRemove
        titer = siter+miter+riter
        print "{0:s} {1:d} puzzle done".format(diff, num)
        print "Time to complete: ",end-start
        print "Total passes through puzzle: ", x.trials
        print "Steps to calculate marks: {0:d}".format(miter)
        print "Steps to find matches: {0:d}".format(siter)
        print "Steps to remove marks: {0:d}".format(riter)
        print "Total steps: {0:d}".format(titer)
        print "Validating if puzzle is correct"
        #time.sleep(1)
        if x.validate():
            print "Puzzle is correct"
        else: print "Puzzle is incorrect"

        raw_input("Press Enter to continue to next puzzle")



print "Welcome to Aleksandar Veselinovic's Sudoku Solver"
print "The program runs at a specified speed"
print "1 is one second, .5 is half a second, 0 is press to continue, -1 is off"
choice = raw_input("Please enter a speed: ")
if choice:
    speed = float(choice)
print "Would you like to show possible numbers? Y/N?"
choice = raw_input("")
if choice.lower() == "y":
    spnums = True

run("easy", 5, speed, spnums)
run("medium", 3, speed, spnums)
run("hard", 1, speed, spnums)

print "Thank you for using my program"
