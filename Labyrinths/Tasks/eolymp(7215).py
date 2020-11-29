#https://www.e-olymp.com/uk/submissions/7879822

WALL = 'U'
SPACE = ' '
START = '+'
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
direction = ['w', 'e', 'n', 's']

def get_pos(maze, figure):
    N = len(maze)
    M = len(maze[0])

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maze[i][j] == figure:
                return (i, j)

    return None

def input_maze(N, M):
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

def find_way(maze, start):
    N = len(maze)
    M = len(maze[0])
    visited = [[-1 for j in range(M)] for i in range(N)]
    visited[start[0]][start[1]] = 0
    queue = [(start, '')]

    while queue:
        coord, sequence = queue.pop(0)
        i, j = coord

        if i == 1 or i == N - 2 or j == 1 or j == M - 2:
            if maze[i][j] == SPACE or maze[i][j] == START:
                return visited[i][j], sequence

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if visited[i1][j1] == -1 and maze[i1][j1] != WALL:
                visited[i1][j1] = visited[i][j] + 1
                queue.append(((i1, j1), sequence + direction[k]))

    return None

if __name__ == '__main__':
    m, n = map(int, input().split())
    maze = input_maze(m, n)
    start = get_pos(maze, START)
    ans = find_way(maze, start)

    if ans:
        print(ans[0])
        print(ans[1])
    else:
        print(-1)