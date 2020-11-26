#https://www.e-olymp.com/uk/submissions/7848246

WALL = '#'
SPACE = '.'
START = 'S'
END = 'E'
di = [1, 0, 0, 0, 0, -1]
dj = [0, 1, 0, 0, -1, 0]
dk = [0, 0, 1, -1, 0, 0]

def get_pos(maze, figure):
    levels = len(maze)
    rows = len(maze[0])
    cols = len(maze[0][0])

    for i in range(1, levels - 1):
        for j in range(1, rows - 1):
            for k in range(1, cols - 1):
                if maze[i][j][k] == figure:
                    return (i, j, k)

    return None

def get_level(file, i, N, M):
    maze = []
    row0 = [WALL] * (M + 2)
    maze.append(row0)

    for _ in range(N):
        row = list(file[i].rstrip())
        row.insert(0, WALL)
        row.append(WALL)
        maze.append(row)
        i += 1

    last_row = [WALL] * (M + 2)
    maze.append(last_row)

    return maze, i

def get_maze(file,level_num, i, N, M):
    maze = []
    level_0 = [[WALL] * (M + 2) for _ in range(N + 2)]
    maze.append(level_0)

    while level_num > 0:
        level, i = get_level(file, i, N, M)
        maze.append(level)
        i += 1
        level_num -= 1

    last_level = [[WALL] * (M + 2) for _ in range(N + 2)]
    maze.append(last_level)

    return maze, i

def print_maze(maze):
    def print_level(level):
        for row in level:
            print(*row)

    for level in maze:
        print_level(level)
        print()

def find_way(maze):
    levels = len(maze)
    rows = len(maze[0])
    cols = len(maze[0][0])
    start = get_pos(maze, START)
    visited = [[[-1 for k in range(cols)] for j in range(rows)] for i in range(levels)]
    visited[start[0]][start[1]][start[2]] = 0
    queue = [start]

    while queue:
        i, j, k = queue.pop(0)

        if maze[i][j][k] == END:
            return visited[i][j][k]

        for index in range(len(di)):
            i1 = i + di[index]
            j1 = j + dj[index]
            k1 = k + dk[index]

            if visited[i1][j1][k1] == -1 and maze[i1][j1][k1] != WALL:
                queue.append((i1, j1, k1))
                visited[i1][j1][k1] = visited[i][j][k] + 1

    return None

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            file = input.readlines()
            i = 0

            while i < len(file) - 1:
                l, r, c = map(int, file[i].rstrip().split())
                i += 1
                maze, i = get_maze(file, l, i, r, c)
                ans = find_way(maze)

                if ans:
                    print("Escaped in {} minute(s).".format(ans), file=output)
                else:
                    print("Trapped!", file=output)

