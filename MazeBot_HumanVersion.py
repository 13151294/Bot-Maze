import BotProgram as bp

def printboard(data : list, b, g, h, w):                                                                                                                                                                                                                                                                                                                                                        
    data = bp.array(['▢' if j == 1 else '▦' for i in data for j in i]).reshape(h,w)
    print(*b)
    print(*g)
    data[b[0]][b[1]] = 'B'
    data[g[0]][g[1]] = 'G'
    for i in data:
        print(*i)
def findposition(grid, h, w):
    g, b = (0, 0)
    for i in range(h):
        for j in range(w):
            if grid[i][j].lower() == 'g':
                g = (i, j)
            if grid[i][j].lower() == 'b':
                b = (i, j)
            if g != 0 and b != 0:
                break
    return g, b
h, w = (int(i) for i in input().strip().split())
grid = [list(input()) for i in range(h)]
#Enable This if you want Auto cover
'''
#cover map with wall
for i in range(h):
    grid[i].insert(0,'0')
    grid[i].insert(len(grid[i]),'0')
grid.insert(0,['0']*(w+2))
grid.insert(len(grid),['0']*(w+2))
h += 2
w += 2
'''
grid_data = bp.array([1 if each != '0' else 0 for i in grid for each in i])
grid_data = grid_data.reshape(h,w)
g, b = findposition(grid, h, w)
for i in grid_data:
    print(*i)
for i in grid:
    print(*i)
while g != b:
    cmd = (input('Enter the dir : ')).lower()
    if len(cmd) == 0:
        print('Empty Input')
        continue

    if cmd[0] == 'l' or (cmd[0] == 'a' and len(cmd) == 1):
        move = (0, -1)
    elif cmd[0] == 'r' or (cmd[0] == 'd' and len(cmd) == 1):
        move = (0, 1)
    elif cmd[0] == 'u' or (cmd[0] == 'w' and len(cmd) == 1):
        move = (-1, 0)
    elif cmd[0] == 'd' or (cmd[0] == 's' and len(cmd) == 1):
        move = (1, 0)
    predict = (abs(b[0] + move[0]), abs(b[1] + move[1]))
    if grid_data[predict[0]][predict[1]] == 1:
        b = predict
        printboard(grid_data, b, g, h, w)
    else:
        print('That is wall')
print('Win!')
