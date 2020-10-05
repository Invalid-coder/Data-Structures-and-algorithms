#https://www.e-olymp.com/uk/submissions/7366872

minTime = 100500

def fidnMinTime(time, arrived):
    global minTime

    if len(arrived) >= n:
        if time < minTime:
            minTime = time

        return

    for i in range(n):
        for j in range(n):
            if i != j and i not in arrived and j not in arrived:
                nextArrived = arrived[:]
                nextArrived.append(i)
                nextArrived.append(j)
                time += max(arr[i], arr[j])

                if len(nextArrived) < n:
                    back = nextArrived.pop(nextArrived.index(min(nextArrived, key=lambda x: arr[x])))
                    fidnMinTime(time + back, nextArrived)
                else:
                    fidnMinTime(time, nextArrived)

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    fidnMinTime(0, [])

    print(minTime)

