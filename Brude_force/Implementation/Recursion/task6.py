#https://www.e-olymp.com/uk/submissions/7324858

minTime = 100500

def findMinTime(score, time, curr):
    global minTime

    if curr >= N:
        if score >= K and time < minTime:
            minTime = time

        return

    findMinTime(score, time, curr + 1)

    nextTime = time + t[curr]

    if nextTime >= minTime:
        return

    nextScore = score + a[curr]
    findMinTime(nextScore, nextTime, curr + 1)

if __name__ == '__main__':
    maxN = 100
    N, K = map(int, input().split())
    a, t = [0] * maxN, [0] * maxN

    for i in range(N):
        a[i], t[i] = map(int, input().split())

    findMinTime(0, 0, 0)
    print(minTime if minTime != 100500 else -1)