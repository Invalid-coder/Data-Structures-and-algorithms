#https://www.e-olymp.com/uk/submissions/7367414

def inversionsAmount():
    counter = 0

    for j in range(n):
        for k in range(j + 1, n):
            if arr[j] > arr[k] + t:
                counter += 1

    return counter

if __name__ == '__main__':
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    print(inversionsAmount())