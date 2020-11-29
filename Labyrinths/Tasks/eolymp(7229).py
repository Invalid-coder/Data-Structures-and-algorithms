WALL = 1
SPACE = 0
COIN = 2
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

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

def find_way(maze, start, end, distance):
    N = len(maze)
    M = len(maze[0])
    visited = [[-1 for j in range(M)] for i in range(N)]
    visited[start[0]][start[1]] = 0
    queue = [(start, 0)]
    coins = 0

    while queue:
        current, counter = queue.pop(0)
        i, j = current


        if current == end and maze[i][j] <= distance:
            coins = max(coins, counter)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if visited[i1][j1] == -1 or visited[i1][j1] >= visited[i][j]:
                if maze[i1][j1] != WALL:
                    if maze[i1][j1] == COIN:
                        queue.append(((i1, j1), counter + 1))
                    else:
                        queue.append(((i1, j1), counter))

                    visited[i1][j1] = visited[i][j] + 1

    if visited[end[0]][end[1]] == -1:
        return -1
    else:
        return coins

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    maze = input_maze(n, m)
    start = (1, 1)
    end = (n, m)
    ans = find_way(maze, start, end, k)

    if ans:
        print(ans)
    else:
        print(-1)
