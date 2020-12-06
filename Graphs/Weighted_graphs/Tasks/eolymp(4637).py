import sys
INF = sys.maxsize * -1

di = [0, 1]
dj = [1, 0]

def isBeyond(i, j, maze):
    if i >= len(maze) or j >= len(maze[0]):
        return True

    return False

def count_ways(maze, start, end, maxDist, K):
    queue = [start]
    counter = 0

    while queue:
        i, j, distance = queue.pop(0)

        if (i, j) == end:
            if maxDist - distance <= K:
                counter += 1

        for k in range(len(di)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if isBeyond(i1, j1, maze):
                continue

            newDist = distance + maze[i1][j1]
            queue.append((i1, j1, newDist))

    return counter

def find_max(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    distances = [[INF] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = maze[start[0]][start[1]]
    current = start

    while True:
        i, j = current

        if (i, j) == end:
            break

        for k in range(len(di)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if isBeyond(i1, j1, maze):
                continue

            newDist = distances[i][j] + maze[i1][j1]

            if newDist > distances[i1][j1]:
                distances[i1][j1] = newDist

        distance = INF

        for k in range(len(di)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if isBeyond(i1, j1, maze):
                continue

            if distances[i1][j1] > distance:
                distance = distances[i1][j1]
                current = (i1, j1)

    return distances[end[0]][end[1]]

if __name__ == '__main__':
    M, N, K = map(int, input().split())
    maze = []

    for _ in range(M):
        row = list(map(int, input().split()))
        maze.append(row)

    maxDist = find_max(maze, (0, 0), (M - 1, N - 1))
    counter = count_ways(maze, (0, 0, maze[0][0]), (M - 1, N - 1), maxDist, K)

    print(maxDist)
    print(counter)