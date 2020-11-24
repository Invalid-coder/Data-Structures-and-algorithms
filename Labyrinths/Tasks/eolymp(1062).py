#https://www.e-olymp.com/uk/submissions/7829055

WALL = 'O'
EMPTY_CELL = '.'
START = '@'
FINISH = 'X'
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def inputMaze(N, M):
    maze = []
    row0 = [WALL] * (M + 2)
    maze.append(row0)

    for i in range(N):
        row = list(input())
        row.insert(0, WALL)
        row.append(WALL)
        maze.append(row)

    last_row = [WALL] * (M + 2)
    maze.append(last_row)

    return maze

def printMaze(maze):
    N = len(maze)

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            print(maze[i][j], end='')
        print()

def get_coord(maze, figure):
    N = len(maze)

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if maze[i][j] == figure:
                return (i, j)

def get_wave_matrix(maze, start):
    N = len(maze)
    waveMatrix = []

    for _ in range(N):
        row = [-1] * N
        waveMatrix.append(row)

    queue = [start]
    waveMatrix[start[0]][start[1]] = 0

    while queue:
        i, j = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if waveMatrix[i1][j1] == -1 and maze[i1][j1] != WALL:
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1
                queue.append((i1, j1))

    return waveMatrix

def find_way(maze, start, finish):
    waveMatrix = get_wave_matrix(maze, start)
    matrix = maze.copy()
    current = finish
    N = len(maze)

    if waveMatrix[finish[0]][finish[1]] == -1:
        return []

    while True:
        i, j = current

        if current == start:
            break

        matrix[i][j] = '+'

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if waveMatrix[i1][j1] == waveMatrix[i][j] - 1:
                current = (i1, j1)
                break

    return matrix

if __name__ == '__main__':
    n = int(input())
    maze = inputMaze(n, n)

    start = get_coord(maze, START)
    finish = get_coord(maze, FINISH)
    ans = find_way(maze, start, finish)

    if ans:
        print('Y')
        printMaze(ans)
    else:
        print('N')
