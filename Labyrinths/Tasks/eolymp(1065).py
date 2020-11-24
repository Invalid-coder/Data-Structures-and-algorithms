#https://www.e-olymp.com/uk/submissions/7830345

WALL = '.'
CELL = '#'
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

def BFS(maze, visited, i, j):
    queue = [(i, j)]
    visited[i][j] = True

    while queue:
        i, j = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if not visited[i1][j1] and maze[i1][j1] == CELL:
                queue.append((i1, j1))
                visited[i1][j1] = True

def countPeaces(maze):
    N = len(maze)
    M = len(maze[0])
    visited = [[False for j in range(M)] for i in range(N)]
    counter = 0

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maze[i][j] == CELL and not visited[i][j]:
                BFS(maze, visited, i, j)
                counter += 1

    return counter

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = inputMaze(n, m)

    print(countPeaces(maze))
