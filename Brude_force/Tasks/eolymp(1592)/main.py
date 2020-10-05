minTime = 100500
minWay = None

def findMinTime(time, arrived, way):
    global minTime, minWay

    if len(arrived) == n:

        if time < minTime:
            minTime = time
            minWay = way

        return

    for i in range(n):
        for j in range(n):
            if i != j and not i in arrived and not j in arrived:
                nextArrived = arrived[:]
                nextWay = way[:]
                nextArrived.append(i)
                nextArrived.append(j)
                nextWay.append((arr[i], arr[j]))

                if len(nextArrived) < n:
                    back = nextArrived.pop(nextArrived.index(min(nextArrived, key=lambda x: arr[x])))
                    nextWay.append(arr[back])
                    findMinTime(time + max(arr[i], arr[j]) + arr[back], nextArrived, nextWay)
                else:
                    findMinTime(time + max(arr[i], arr[j]), nextArrived, nextWay)


if __name__ == '__main__':
    with open('input.txt') as inp:
        text = inp.readlines()
        i = 0

        while i < len(text):
            n = int(text[i])
            arr = list(map(int, text[i + 1].split()))
            i += 2

            findMinTime(0, [], [])

            print(minTime)

            for step in minWay:
                if isinstance(step, tuple):
                    print(*step)
                else:
                    print(step)
