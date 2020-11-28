#https://www.e-olymp.com/uk/submissions/7857823

SPACE = '.'
di = [1, 1, -1, -1, 2, 2, -2, -2]
dj = [-2, 2, -2, 2, -1, 1, -1, 1]

def game_dimension(row, col):
    return (chr(col + 97), 8 - row)

def matrix_dimension(line):
    row = 8 - int(line[1])
    col = ord(line[0]) - 97

    return (row, col)

def is_beyond(i, j, N):
    if i < 0 or i >= N:
        return True
    if j < 0 or j >= N:
        return True

    return False

def find_way(maze, start, finish):
    queue = [start]
    wave_matrix = [[-1 for j in range(len(maze))] for i in range(len(maze))]
    wave_matrix[start[0]][start[1]] = 0

    while queue:
        i, j = queue.pop(0)

        if (i, j) == finish:
            return wave_matrix[i][j]

        for k in range(len(dj)):
            i1 = i + di[k]
            j1 = j + dj[k]

            if is_beyond(i1, j1, len(maze)):
                continue

            if wave_matrix[i1][j1] == -1:
                queue.append((i1, j1))
                wave_matrix[i1][j1] = wave_matrix[i][j] + 1

    return 0

if __name__ == '__main__':
    maze = [[SPACE for j in range(8)] for i in range(8)]

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            for line in input:
                start, finish = line.rstrip().split()
                moves = find_way(maze, matrix_dimension(start), matrix_dimension(finish))

                print("To get from {} to {} takes {} knight moves.".format(start, finish, moves), file=output)
