#https://www.e-olymp.com/uk/submissions/7829883

WALL = 1
EMPTY_CELL = 0
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def inputMaze(N, M):
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

def find_way_length(maze, start, finish):
    n = len(maze)
    m = len(maze[0])
    waveMatrix = []

    for _ in range(n):
        row = [-1] * m
        waveMatrix.append(row)

    queue = [start]
    waveMatrix[start[0]][start[1]] = 0

    while queue:
        current = queue.pop(0)

        if current == finish:
            break

        i = current[0]
        j = current[1]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if waveMatrix[i1][j1] == -1 and maze[i1][j1] != WALL:
                queue.append((i1, j1))
                waveMatrix[i1][j1] = waveMatrix[i][j] + 1

    return waveMatrix[finish[0]][finish[1]]

if __name__ == '__main__':
    N, M = map(int, input().split())
    maze = inputMaze(N, M)
    start = tuple(map(int, input().split()))[::-1]
    finish = tuple(map(int, input().split()))[::-1]
    print(find_way_length(maze, start, finish))

