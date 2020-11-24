WALL = '#'
SPACE = '.'
ENTRANCE = '+'

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

if __name__ == '__main__':
    n = int(input())
    maze = inputMaze(n)

    for row in maze:
        print(*row)