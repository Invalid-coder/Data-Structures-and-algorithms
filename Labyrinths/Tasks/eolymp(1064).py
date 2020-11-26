WALL = '#'
SPACE = '.'
POINT = '@'
di = [1, 1, -1, -1, 2, 2, -2, -2]
dj = [-2, 2, -2, 2, -1, 1, -1, 1]

def get_points(maze):
    points = []
    N = len(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == POINT:
                points.append((i, j))

    return points

def get_maze(N):
    maze = []

    for i in range(N):
        row = list(input())
        maze.append(row)

    return maze

def is_beyond(i, j, N):
    if i < 0 or i >= N:
        return True
    if j < 0 or j >= N:
        return True

    return False

def get_wave_matrix(maze, start):
    queue = [start]
    wave_matrix = [[-1 for j in range(len(maze))] for i in range(len(maze))]
    wave_matrix[start[0]][start[1]] = 0

    while queue:
        i, j = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if is_beyond(i1, j1, len(maze)):
                continue

            if wave_matrix[i1][j1] == -1 and maze[i1][j1] != WALL:
                queue.append((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1

    return wave_matrix

def find_way(maze, start, end):
    wave_matrix = get_wave_matrix(maze, start)

    if wave_matrix[end[0]][end[1]] == -1:
        return None

    way = maze.copy()
    current = end

    while True:
        if current == start:
            break

        i, j = current

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if is_beyond(i1, j1, len(maze)):
                continue

            if wave_matrix[i1][j1] == wave_matrix[i][j] - 1:
                current = (i1, j1)
                way[i1][j1] = POINT
                break

    return way

def print_maze(maze):
    for row in maze:
        print(*row)

if __name__ == '__main__':
    n = int(input())
    maze = get_maze(n)
    points = get_points(maze)
    way = find_way(maze, *points)

    if way:
        print_maze(way)
    else:
        print("Impossible")