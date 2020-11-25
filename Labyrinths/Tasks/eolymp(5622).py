#https://www.e-olymp.com/uk/submissions/7842686

WALL = '#'
SPACE = '.'
ENTRANCE = '+'
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def inputMaze(N):
    maze = []
    row0 = [ENTRANCE] * 2 + [WALL] * N
    maze.append(row0)
    row1 = list(input())
    row1.insert(0, ENTRANCE)
    row1.append(WALL)
    maze.append(row1)

    for i in range(N - 2):
        row = list(input())
        row.insert(0, WALL)
        row.append(WALL)
        maze.append(row)

    rowN = list(input())
    rowN.insert(0, WALL)
    rowN.append(ENTRANCE)
    maze.append(rowN)
    last_row = [WALL] * N + [ENTRANCE] * 2
    maze.append(last_row)

    return maze

def count_area(maze):
    n = len(maze)
    exit = (n - 2, n - 2)
    entrance = (1, 1)
    queue = [entrance, exit]
    visited = [[False for j in range(n)] for i in range(n)]
    visited[entrance[0]][entrance[1]] = True
    visited[exit[0]][exit[1]] = True
    counter = 0

    while queue:
        i, j = queue.pop(0)

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if maze[i1][j1] == WALL:
                counter += 1
            elif maze[i1][j1] == SPACE and not visited[i1][j1]:
                queue.append((i1, j1))
                visited[i1][j1] = True

    return counter * 9

if __name__ == '__main__':
    n = int(input())
    maze = inputMaze(n)

    print(count_area(maze))
