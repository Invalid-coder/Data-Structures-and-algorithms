WALL = 1
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

def get_next(maze, visited, i , j):
    arr = []

    for k in range(len(dj)):
        i1 = i + di[k]
        j1 = j + dj[k]

        if not visited[i1][j1] and maze[i1][j1] != WALL:
            arr.append((i1, j1))
            visited[i1][j1] = True

    arr.append((i, j))

    return arr

def find_way(maze, start1, start2):
    n = len(maze)
    m = len(maze[0])
    visited_1 = [[False for j in range(m)] for i in range(n)]
    visited_2 = [[False for j in range(m)] for i in range(n)]
    visited_1[start1[0]][start1[1]] = True
    visited_2[start2[0]][start2[1]] = True
    queue = [(start1, start2)]

    while queue:
        a, b = queue.pop(0)
        i1, j1 = a
        i2, j2 = b

        if i1 == i2 and j1 == j2:
            return (i1, j1)

        arr1 = get_next(maze, visited_1, i1, j1)
        arr2 = get_next(maze, visited_2, i2, j2)

        for start1 in arr1:
            for start2 in arr2:
                queue.append((start1, start2))

    return None

if __name__ == '__main__':
    n, m = map(int, input().split())
    start1 = tuple(map(int, input().split()))
    start2 = tuple(map(int, input().split()))
    maze = input_maze(n, m)
    ans = find_way(maze, start1, start2)

    if ans:
        print(*ans)
    else:
        print(-1)