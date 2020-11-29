WALL = '#'
SPACE = '.'
PLAYER1 = '1'
PLAYER2 = '2'
FINISH = '*'
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

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

def find_way(maze, start1, start2, end):
    queue1 = [(start1, '')]
    queue2 = [start2]

    while queue1 and queue2:
        coord, sequence = queue1.pop(0)
        i1, j1 = coord
        i2, j2 = queue2.pop(0)

        if (i1, j1) == (i2, j2) == end:
            return sequence

        for k in range(len(dj)):
            i11 = i1 + di[k]
            j11 = j1 + dj[k]
            i22 = i2 + di[k]
            j22 = j2 + dj[k]

            if maze[i11][j11] != WALL:
                queue1.append(((i11, j11), sequence + direction[k]))
            else:
                queue1.append(((i1, j1), sequence + direction[k]))

            if maze[i22][j22] != WALL:
                queue2.append((i22, j22))
            else:
                queue2.append((i2, j2))

    return None

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = input_maze(n, m)
    s1, s2 = get_pos(maze, PLAYER1), get_pos(maze, PLAYER2)
    end = get_pos(maze, FINISH)
    ans = find_way(maze, s1, s2, end)

    if ans:
        print(len(ans))
        print(ans)

