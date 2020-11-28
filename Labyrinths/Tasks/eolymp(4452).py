#https://www.e-olymp.com/uk/submissions/7866424

WALL = 1
FINISH = 2
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def input_maze(N, M):
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

def find_way(maze, start):
    visited = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    visited[start[0]][start[1]] = True
    queue = [start]

    while queue:
        i, j, counter = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            while not visited[i1][j1] and maze[i1][j1] != WALL:
                if maze[i1][j1] == FINISH:
                    return counter + 1

                visited[i1][j1] = True
                i1 += di[k]
                j1 += dj[k]

            if i1 - di[k] != i or j1 - dj[k] != j: # if True respectively we chanced position
                queue.append((i1 - di[k], j1 - dj[k], counter + 1))

    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = input_maze(n, m)
    start = (1, 1, 0)

    print(find_way(maze, start))
