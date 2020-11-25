WALL = '#'
SPACE = '.'
START = 'S'
END = 'E'
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

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

def get_pos(maze, figure):
    n = len(maze)
    m = len(maze[0])

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if maze[i][j] == figure:
                return (i, j)

def pass_maze(level, next_level, start, distance):
    queue = [start]
    distances = [[-1 for j in range(len(level[0]))] for i in range(len(level))]
    distances[start[0]][start[1]] = distance
    destinations = []

    while queue:
        i, j = queue.pop(0)

        if level[i][j] == END:
            destinations.append(((i, j), distances[i][j]))
            break

        if next_level and next_level[i][j] != WALL:
            destinations.append(((i, j), distances[i][j] + 1))

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if distances[i1][j1] == -1 and level[i1][j1] != WALL:
                queue.append((i1, j1))
                distances[i1][j1] = distances[i][j] + 1

    return destinations

def find_way(levels):
    i = 0
    starts = [(get_pos(levels[i], START), 0)]

    while i < len(levels):
        if not starts:
            return None

        curr_level = levels[i]
        next_level = levels[i + 1] if i < len(levels) - 1 else None
        temp = []

        for start, distance in starts:
            temp.extend(pass_maze(curr_level, next_level, start, distance))

        starts = temp

        i += 1


    if starts:
        return starts[0][1]
    else:
        return None

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            file = input.readlines()
            i = 0

            while i < len(file) - 1:
                l, r, c = map(int, file[i].rstrip().split())
                levels = []
                i += 1

                while l > 0:
                    level, i = get_level(file, i, r, c)
                    levels.append(level)
                    i += 1
                    l -= 1

                ans = find_way(levels)

                if ans:
                    print("Escaped in {} minute(s).".format(ans), file=output)
                else:
                    print("Trapped!", file=output)

