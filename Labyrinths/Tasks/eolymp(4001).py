#https://www.e-olymp.com/uk/submissions/7821900

WALL = '*'
EMPTY_CELL = '.'
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def get_room_area(maze, start):
    n = len(maze)
    m = len(maze[0])
    visited = [[False for i in range(m)] for j in range(n)]
    visited[start[0]][start[1]] = True
    counter = 0
    queue = [start]

    while queue:
        i, j = queue.pop(0)
        counter += 1

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if not visited[i1][j1] and maze[i1][j1] != WALL:
                queue.append((i1, j1))
                visited[i1][j1] = True

    return counter

if __name__ == '__main__':
    n = int(input())
    maze = []

    for _ in range(n):
        row = list(input())
        maze.append(row)

    start = tuple(map(lambda x: int(x) - 1, input().split()))
    print(get_room_area(maze, start))
