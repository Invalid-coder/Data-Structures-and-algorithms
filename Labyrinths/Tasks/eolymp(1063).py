#https://www.e-olymp.com/uk/submissions/7829391

WALL = '.'
PAPER = '#'
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

def BFS(maze, visited, start):
    queue = [start]
    visited[start[0]][start[1]] = True

    while queue:
        i, j = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if not visited[i1][j1] and maze[i1][j1] == PAPER:
                visited[i1][j1] = True
                queue.append((i1, j1))

def count_peaces(maze):
    N = len(maze)
    M = len(maze[0])
    visited = [[False for j in range(M)] for i in range(N)]
    counter = 0

    for row in range(1, N - 1):
        for col in range(1, M - 1):
            if maze[row][col] == PAPER and not visited[row][col]:
                BFS(maze, visited, (row, col))
                counter += 1

    return counter

if __name__ == '__main__':
    m, n = map(int, input().split())
    maze = inputMaze(m, n)
    print(count_peaces(maze))
