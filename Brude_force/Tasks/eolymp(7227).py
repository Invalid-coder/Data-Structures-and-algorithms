#https://www.e-olymp.com/uk/submissions/7367972

def findMinAmount(arr):
    balloons = 0
    time = 0

    while balloons < M:
        time += 1

        for i in range(N):
            if arr[i][4] == time:
                balloons += 1
                arr[i][3] += 1
                arr[i][4] += arr[i][0]

                if arr[i][3] == arr[i][1]:
                    arr[i][4] += arr[i][2]
                    arr[i][3] = 0

    return time

if __name__ == '__main__':
    M, N = map(int, input().split())
    arr = []

    for i in range(N):
        a = list(map(int, input().split()))
        a.append(0) #amount of inflated balloons by certain persen
        a.append(a[0])  #next point of the time when balloon will be inflated
        arr.append(a)

    print(findMinAmount(arr))
