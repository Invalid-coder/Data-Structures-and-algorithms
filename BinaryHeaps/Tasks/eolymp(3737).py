#https://www.e-olymp.com/uk/submissions/7620483

def isHeap(array, n):
    for i in range(n):
        left = 2 * i + 1
        right = left + 1

        if left <= n - 1 and array[left] < array[i]:
            return False
        if right <= n - 1 and array[right] < array[i]:
            return False

    return True

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print("YES" if isHeap(array, n) else "NO")