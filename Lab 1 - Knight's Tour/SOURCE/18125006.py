import argparse
import time
import sys

xs = ys = m = count = numberOfMoves = runningTime = finished = board = None
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
orig_stdout = sys.stdout

def isAccessible(x, y):
    if x>=0 and y>=0 and x<m and y<m and board[x][y] == -1:
        return True
    return False

#backtracking

def doBacktracking(x, y, count):
    global finished, board, numberOfMoves
    numberOfMoves += 1

    if count == m*m + 1:
        finished = True
    
    for i in range(8):
        ux = x + dx[i]
        uy = y + dy[i]
        if isAccessible(ux, uy):
            board[ux][uy] = count
            doBacktracking(ux, uy, count + 1)
            if finished:
                return
            board[ux][uy] = -1

    return

def backtracking():
    init()
    doBacktracking(ys - 1, xs - 1, 2)
    printSolution("18125006_backtrack.txt")

####################

#warnsdorff’s algorithm
def numberOfAccessibleMoves(x, y):
    count = 0
    for i in range (8):
        ux = x + dx[i]
        uy = y + dy[i]
        if isAccessible(ux, uy):
            count += 1
    return count

def nextMove(x, y):
    minAccess = 9
    k = -1
    for i in range(8):
        ux = x + dx[i]
        uy = y + dy[i]
        if (isAccessible(ux, uy)):
            num = numberOfAccessibleMoves(ux, uy)
            if num >= 0 and num < minAccess:
                minAccess = num
                k = i
    return k

def warnsdorff():
    global numberOfMoves, board, count
    init()
    x = ys - 1
    y = xs - 1
    numberOfMoves = 0
    for i in range (2, m*m + 1):
        k = nextMove(x, y)
        if k == -1:
            break
        x = x + dx[k]
        y = y + dy[k]
        count += 1
        board[x][y] = count
    numberOfMoves = i
    printSolution("18125006_heuristic.txt")

####################

def init():
    global board, finised, numberOfMoves, runningTime, count
    board = [[-1]*m for _ in range(m)]
    finished = False
    board[ys - 1][xs - 1] = 1
    numberOfMoves = 0
    count = 1
    runningTime = time.time()

def readInput():
    global xs, ys, m
    parser = argparse.ArgumentParser()
    parser.add_argument("-px", help = "initial x")
    parser.add_argument("-py", help = "initial y")
    parser.add_argument("-s", help = "size")
    args = parser.parse_args()
    xs = int(args.px)
    ys = int(args.py)
    m = int(args.s)

def printSolution(path):
    global runningTime
    runningTime = (time.time() - runningTime) * 1000
    f = open(path, "w")
    sys.stdout = f
    print("{:d} {:d} {:d}\n{:d}\n{:f}".format(xs, ys, m, numberOfMoves, runningTime))
    for i in range(m):
        for j in range(m):
            print(board[i][j], end = " ")
        print()
    sys.stdout = orig_stdout
    f.close()

if __name__ == "__main__":
    readInput()
    backtracking()
    warnsdorff()