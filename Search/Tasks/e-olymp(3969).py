#https://www.e-olymp.com/uk/submissions/7170979

def binary_search(w, h, n):
    left = 0
    right = max(w, h) * n

    while left < right:
        m = (left + right) // 2
        wn = m // w
        hn = m // h

        if wn * hn < n:
            left = m + 1
        else:
            right = m

    return left

if __name__ == '__main__':
    w,h,n = map(int, input().split())
    print(binary_search(w, h, n))