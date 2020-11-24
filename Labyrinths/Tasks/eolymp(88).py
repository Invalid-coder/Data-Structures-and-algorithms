PLAYER_1 = 'g'
PLAYER_2 = 'l'
WALL = 'R'
FINISH = 'e'
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def coords(maze, r, c, player):
    for i in range(r):
        for j in range(c):
            if maze[i][j] == player:
                return (i, j)

def get_next_coords(i, j, maze, player, visited):
    positions = []

    for k in range(len(dj)):
        i1 = i + di[k]
        j1 = j + dj[k]

        if maze[i1][j1] != WALL and not visited[i1][j1]:
            if maze[i1][j1] == FINISH and player == PLAYER_2:
                continue

            positions.append((i1, j1))
            visited[i1][j1] = True

    return positions

def wayExists(maze, pos1, pos2):
    queue = [(pos1, pos2)]
    visited1 = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    visited1[pos1[0]][pos1[1]] = True
    visited2 = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    visited2[pos2[0]][pos2[1]] = True

    while queue:
        pos1, pos2 = queue.pop(0)

        if pos1 == pos2:
            continue
        if maze[pos1[0]][pos1[1]] == FINISH:
            return True

        coords1 = get_next_coords(*pos1, maze, PLAYER_1 , visited1)
        coords2 = get_next_coords(*pos2, maze, PLAYER_2, visited2)

        for c1 in coords1:
            for c2 in coords2:
                queue.append((c1, c2))

    return False

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        r, c = map(int, input().split())
        maze = []

        for _ in range(r):
            row = list(input())
            maze.append(row)

        pos1 = coords(maze, r, c, PLAYER_1)
        pos2 = coords(maze, r, c, PLAYER_2)
        print("YES" if wayExists(maze, pos1, pos2) else "NO")
