#https://www.e-olymp.com/uk/submissions/7343324

maxLength = 0

def findMaxLength(length, num):
    global maxLength

    if num >= M or length == N:
        if length > maxLength:
            maxLength = length

        return

    findMaxLength(length, num + 1)

    nextLength = length + tracks[num]

    if nextLength <= N:
        findMaxLength(nextLength, num + 1)

if __name__ == '__main__':
    with open('input.txt') as inp:
        for line in inp.readlines():
            data = list(map(int, line.split()))
            N,M, tracks = data[0], data[1], data[2:]
            findMaxLength(0, 0)

            print('sum:{}'.format(maxLength))

            maxLength = 0


