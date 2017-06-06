from SSolve import SSolve

x = SSolve("data/easy4.txt")
x.initSsq()

#for list in x.ssq:
#    for box in list:
#        print box.actual,
#    print

x.calcMarks()
x.printPuzzle()

for list in x.ssq:
    for box in list:
        print box.pnums,
    print

x.solve()
#x.printPuzzle()
