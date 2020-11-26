WALL = '#'
SPACE = '.'
STATE = '123'
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def get_state(maze, figure):
    N = len(maze)
    M = len(maze[0])
    coords = []

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maze[i][j] == figure:
                coords.append((i, j))

    return coords

def inputMaze(N, M):
    maze = []
    first_row = [WALL] * (M + 2)
    maze.append(first_row)

    for _ in range(N):
        row = list(input())
        row.insert(0, WALL)
        row.append(WALL)
        maze.append(row)

    last_row = [WALL] * (M + 2)
    maze.append(last_row)

    return maze

def find_way(maze, start, figure):
    queue = [start]
    distances = [[-1 for j in range(len(maze[0]))] for i in range(len(maze))]
    distances[start[0]][start[1]] = 0

    while queue:
        i, j = queue.pop(0)

        if maze[i][j] == figure:
            return distances[i][j] - 1

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if distances[i1][j1] == -1 and maze[i1][j1] != WALL:
                queue.append((i1, j1))
                distances[i1][j1] = distances[i][j] + 1

    return 1e9

def count_bridges(maze):
    state = get_state(maze, '1')
    dist1 = 1e9
    dist2 = 1e9

    for coord in state:
        dist1 = min(dist1, find_way(maze, coord, '2'))
        dist2 = min(dist2, find_way(maze, coord, '3'))

    if dist1 == 1e9 or dist2 == 1e9:
        return None
    else:
        return dist1 + dist2

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = inputMaze(n, m)
    ans = count_bridges(maze)

    if ans:
        print(ans)
    else:
        print(-1)

