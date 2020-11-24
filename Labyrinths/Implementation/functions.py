N = 7 # amount of rows
M = 7 # amount of columns
WALL = 0
EMPTY_CELL = -1
di = [0, -1, 0, 1] # shifting by rows
dj = [-1, 0, 1, 0] # shifting by cols

def showMaze(maze):
    for row in maze:
        for el in row:
            print("%3s" % el, end="")

def inputMaze(N, M):
    """
        Maze with walls

        00000000
        0      0
        0      0
        0      0
        00000000
    """

    maze = []
    row0 = [WALL] * (M + 2)
    maze.append(row0)

    for i in range(N):
        row = list(map(int, input().split()))
        row.insert(0, WALL)
        row.append(WALL)
        maze.append(row)

    last_row = [WALL] * (M + 2)
    maze.append(last_row)

    return maze

def readMazeFromFile(file_name, M):
    """
            Maze with walls

            00000000
            0      0
            0      0
            0      0
            00000000
        """

    maze = []
    row0 = [WALL] * (M + 2)
    maze.append(row0)

    with open(file_name) as f:
        for str_row in f:
            row = list(map(int, str_row.rstrip().split()))
            row.insert(0, WALL)
            row.append(WALL)
            maze.append(row)

    last_row = [WALL] * (M + 2)
    maze.append(last_row)

    return maze

def getWaveMatrix(maze, start):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = []

    for _ in range(n):
        row = [EMPTY_CELL] * m
        waveMatrix.append(row)

    queue = [start]
    waveMatrix[start[0]][start[1]] = 0

    while queue:
        current = queue.pop(0)
        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if waveMatrix[i1][j1] == EMPTY_CELL and maze[i1][j1] != WALL:
                queue.append((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1

    return waveMatrix

def findWay(maze, start, end):
    """
    :param maze: matrix of maze
    :param start: start point
    :param end: end point
    :return matrix with the way from start to end
    """

    waveMatrix = getWaveMatrix(maze, start)

    if waveMatrix[end[0]][end[1]] == EMPTY_CELL:
        print("The way does not exxist")
        return

    n = len(maze)
    m = len(maze[0])
    matrix = []

    for i in range(n):
        row = [" . "] * m
        matrix.append(row)

    matrix[end[0]][end[1]] = 'F' # remarked the destination
    current = end

    while True:
        if current == start:
            matrix[current[0]][current[1]] = " S "
            break

        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            current = None

            if waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)
                matrix[i1][j1] = " # "
                break

    return matrix

def find_way(maze, start, end):
    """
    :param maze: matrix of maze
    :param start: start point
    :param end: end point
    :return list of way cells
    """

    waveMatrix = getWaveMatrix(maze, start)

    if waveMatrix[end[0]][end[1]] == EMPTY_CELL:
        print("The way does not exxist")
        return []

    stack = []
    current = end

    while True:
        stack.push(current)

        if current == start:
            break

        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            current = None

            if waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)
                break
    way = []

    while stack:
        way.append(stack.pop())

    return way
