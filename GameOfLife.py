import time, random, copy

WIDTH = 60
HEIGHT = 20

dx=[0,0,1,-1]
dy=[1,-1,0,0]

nextCells = []
for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        if random.randint(0,1) == 0:
            row.append("#") # Denotes a living cell
        else:
            row.append(' ')
    nextCells.append(row)

while True:
    print("\n\n\n")
    currentCells = copy.deepcopy(nextCells)

    for x in range(HEIGHT):
        for y in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    
    for x in range(HEIGHT):
        for y in range(WIDTH):
            numNeighbors = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < HEIGHT and ny < WIDTH and ny >= 0 and nx >= 0 and currentCells[nx][ny] == "#":
                    numNeighbors+=1
            
            if numNeighbors >= 2 and currentCells[x][y] == "#":
                nextCells[x][y] = "#"
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = ' '
    time.sleep(1)
