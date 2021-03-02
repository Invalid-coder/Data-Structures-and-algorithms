INF = 10**9


def can(h1, h2, h3):
    if h1 < h2 and h3 < h2: return True
    if h1 > h2 and h3 > h2: return True
    return False


def deleteAll(a, b):
    assert deleted[a][b] >= 0
    if deleted[a][b] == a: return
    deleteAll(a, deleted[a][b])
    deleteAll(deleted[a][b], b)
    ans.append(deleted[a][b])


def restoreAns(a, b):
    assert fr[a][b] >= 0
    if fr[a][b] == a:
        deleteAll(a, b)
        return

    restoreAns(a, fr[a][b])
    restoreAns(fr[a][b], b)


def printAns():
    a, b = 0, n - 1
    if fr[a][b] < 0:
        print(-1)
    else:
        restoreAns(a, b)
        print("length: ", len(ans))
        for x in ans:
            print(x + 1)


def main(h):
    for a in range(n - 1):
        deleted[a][a + 1] = a

    for l in range(2, n):
        a = 0
        while a + l < n:
            b = a + l
            for i in range(a + 1, b):
                if deleted[a][i] >= 0 and deleted[i][b] >= 0 and can(h[a], h[i], h[b]):
                    deleted[a][b] = i
                    break
            a += 1

    for l in range(1, n):
        a = 0
        while a + l < n:
            b = a + l

            if h[a] > h[b]:
                a += 1
                continue
            if deleted[a][b] >= 0:
                dyn[a][b] = b - a - 1
                fr[a][b] = a

            for i in range(a + 1, b):
                if h[a] > h[i] or h[i] > h[b]:
                    a += 1
                    continue

                cans = dyn[a][i] + dyn[i][b]

                if dyn[a][b] > cans:
                    dyn[a][b] = cans
                    fr[a][b] = i
            a += 1

    printAns()


if __name__ == '__main__':
    h = list(map(int, input().split()))
    n = len(h)
    deleted = [[-1 for j in range(n)] for i in range(n)]
    dyn = [[INF for j in range(n)] for i in range(n)]
    fr = [[-1 for j in range(n)] for i in range(n)]
    ans = []
    main(h)


