#This is Bot Maze
#You Need to Input Height, Width & Maze (With Bot Position & Goal)
#Then This Program Will Show You How Bot Walk to the Goal 
#And Then It will Show you the Path The Bot Have Pass
#Code Length Without Comment 74
#This Code Was Compute By Ace Fhid
#Python 3.8.5
"""
Example Maze
6 7
g0--00-
-00----
-0--00-
----0--
0-0-00-
--0---b
"""

import BotProgram as bp
import time

dir = [(0,-1),(0,1),(-1,0),(1,0)]

def printboard(data : list, b, g, h, w, path):                                                                                                                                                                                                                                                                                                                                                        
    data = bp.array(['▦' if j == 0 else '▢' for i in data for j in i]).reshape(h,w)
    data[b[0]][b[1]] = '\033[038;2;235;255;0mB\033[0;0m'
    data[g[0]][g[1]] = '\033[038;2;235;255;0mG\033[0;0m'
    if path != 0:
        for i in path:
            data[i[0]][i[1]] = '\033[038;2;245;255;130m▢\033[0;0m'
    print(' ')
    for i in data[1:h-1]:
        print(*i[1:w-1])
#Make Path that Bot Walk
def Path(data : list, g: tuple):
    path = []
    NowPos = g
    NowVal = data[g[0]][g[1]]
    path.append(NowPos)
    NowVal -= 1
    while NowVal != 0:
        for j in dir:
            Select = (NowPos[0] + j[0], NowPos[1] + j[1])
            if data[Select[0]][Select[1]] == NowVal:
                NowPos = Select
                path.append(NowPos)
                break
        NowVal -= 1
    path.reverse()
    return path
#Bot Solve Maze
def bot(wall : list, data : list, h, w, b : tuple, g : tuple):
    num = 1
    data[b[0]][b[1]] = num
    while True:
        choose = [(i,j) for i in range(h) for j in range(w) if data[i][j] == num]
        for i in choose:
            for j in dir:
                face = (i[0] + j[0], i[1] + j[1])
                if wall[face[0]][face[1]] == 1 and data[face[0]][face[1]] == 0:
                    data[face[0]][face[1]] = num + 1
        num += 1
        if data[g[0]][g[1]] != 0:
            break
    return data, num
#Map Edge With Wall
def AutoCover(Grid : list, h, w):
    for i in range(h):
        Grid[i].insert(0,'0')
        Grid[i].insert(len(Grid[i]),'0')
    Grid.insert(0,['0']*(w+2))
    Grid.insert(len(Grid),['0']*(w+2))
    return Grid, h + 2, w + 2
def Main():
    #collect Height & Width of Maze
    h, w = (int(i) for i in input().strip().split())
    #Collect Maze
    grid = [list(input()) for i in range(h)]
    #Map Edge With Wall
    grid, h, w = AutoCover(grid, h, w)
    #Make 0 list to count bot movement
    grid_data = list([0]*w for i in range(h))
    #Make difference between wall(0) and path(1)
    wall_data = [[1 if j != '0' else 0 for j in i] for i in grid]
    #Find Goal and Bot Position
    for i in range(h):
        for j in range(w):
            if grid[i][j].lower() == 'g':
                g = (i, j)
            if grid[i][j].lower() == 'b':
                b = (i, j)
    #Bot Solve Maze
    grid_data, last = bot(wall_data,grid_data,h,w,b,g)
    #Make Path of Bot
    path = Path(grid_data, g)
    #Print Bot movement
    for i in path:
        printboard(wall_data, i, g, h, w, 0)
        time.sleep(0.5)
    #Draw move line
    printboard(wall_data, i, g, h, w, path)
    #Print move count
    print('Move :', last)

if __name__ == '__main__':
    Main()