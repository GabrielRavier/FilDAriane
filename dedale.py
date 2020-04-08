from tkinter import *
import sys
sys.setrecursionlimit(10000)

incr = 1
size = incr * 10
posX = 1
posY = 1
map = [[]] * 100

for value in range(0, 100):
    map[value] = [0] * 100



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x * (incr), 0, x * (incr), canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y * (incr), canvas_width, y * (incr), fill="#476042")

def right():
    global posX
    global posY
    if (map[posY][posX + 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def left():
    global posX
    global posY
    if (map[posY][posX - 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def up():
    global posY
    global posX
    if (map[posY - 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY -= 1

    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def down():
    global posY
    global posX
    if (map[posY + 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

dir = []

pathToExit = []
alreadyVisitedPositions = [[]] * 100
hasSolved = False

def solveMaze(x, y):
    global alreadyVisitedPositions
    global pathToExit
    if map[y][x] == 2:
        pathToExit.append([x, y])
        return True

    if map[y][x] == 1 or alreadyVisitedPositions[y][x]:
        return False

    alreadyVisitedPositions[y][x] = True

    if x != 0:
        if solveMaze(x - 1, y):
            pathToExit.append([x, y])
            return True

    if x != 99:
        if solveMaze(x + 1, y):
            pathToExit.append([x, y])
            return True

    if y != 0:
        if solveMaze(x, y - 1):
            pathToExit.append([x, y])
            return True

    if y != 99:
        if solveMaze(x, y + 1):
            pathToExit.append([x, y])
            return True

    return False

def doMove(currentIter):
    global posX
    global posY
    xAndY = pathToExit[currentIter + 1]
    possibilities = [[posX, posY - 1], [posX - 1, posY], [posX, posY + 1], [posX + 1, posY]]
    funcs = [up, left, down, right]

    i = 0
    while i < 4:
        if possibilities[i] == xAndY:
            break;
        i += 1

    if i == 4:
        raise ValueError("i bad")

    funcs[i]()

    

def algo(currentIter):
    global hasSolved
    global latestMove
    global alreadyVisitedPositions
    global pathToExit
    if hasSolved == False:
        for i in range(100):
            alreadyVisitedPositions[i] = [False] * 100

        solveMaze(1, 1)
        pathToExit = pathToExit[::-1]
        latestMove = None

    doMove(currentIter)


    




def setACaseXY(X, Y, color):
    points = [X * size, Y * size, size * (X + 1), Y * size, size * (X + 1), size * (Y + 1), X * size, size * (Y + 1)]
    w.create_polygon(points, outline="#476042", fill=color, width=4)



master = Tk()
canvas_width = 1000
canvas_height = 1000
w = Canvas(master,
           width=1000,
           height=1000)











path = 'map.txt'
with open(path) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       x = line.find('x')
       while x != -1:
           setACaseXY(x, cnt, 'red')
           map[cnt][x] = 1
           x = line.find('x', x + 1)
       line = fp.readline()
       cnt += 1

w.pack()

setACaseXY(47, 21, 'green')
map[21][47] = 2


for value in range(0, 1000):
    master.after(value * 100, algo, value)

checkered(w,10)

mainloop()
