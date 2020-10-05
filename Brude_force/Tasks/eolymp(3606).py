#https://www.e-olymp.com/uk/submissions/7367194

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def pairsAmount():
    pairs = []

    for i in range(N):
        for j in range(N):
            if i != j and (j, i) not in pairs:
                if distance(*arr[i], *arr[j]) <= R:
                    pairs.append((i, j))

    return len(pairs)

if __name__ == '__main__':
    N, R = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    print(pairsAmount())