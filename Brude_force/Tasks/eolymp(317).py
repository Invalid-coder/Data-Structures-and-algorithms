import math

def digitsAmount(num):
    return 1 if num == 0 else int(math.ceil(math.log10(abs(num) + 0.5)))

def splitNumber(num, mid):
    right = 0
    i = 0

    while i < mid and num > 0:
        right += (num % 10) * (10 ** i)
        num //= 10
        i += 1

    return num, right

def karatsuba_mul(a, b):
    n = max(digitsAmount(a), digitsAmount(b))
    mid = n // 2

    if n == 1:
        return a * b
    else:
        x_l, x_r = splitNumber(a, mid)
        y_l, y_r = splitNumber(b, mid)
        p1 = karatsuba_mul(x_l, y_l)
        p2 = karatsuba_mul(x_r, y_r)
        p3 = karatsuba_mul(x_l + x_r, y_l + y_r)

        return p1 * (10 ** n) + (p3 - p1 - p2) * (10 ** (n // 2)) + p2

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(karatsuba_mul(a, b))