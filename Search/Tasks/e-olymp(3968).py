import math
#https://www.e-olymp.com/uk/submissions/7170139

def binary_continuous(f, c, a, b):
    left = a
    right = b
    mid = (left + right) / 2.0

    while left != mid and right != mid:
        if f(mid) < c:
            left = mid
        else:
            right = mid

        mid = (left + right) / 2.0

    return left

print(binary_continuous(lambda x: x*x + math.sqrt(x), float(input()), 1.0, 10**10))