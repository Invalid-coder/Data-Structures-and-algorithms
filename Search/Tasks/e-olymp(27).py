from math import log10
#https://www.e-olymp.com/uk/submissions/7169994

def binary(num):
    binary = 0
    i = 1

    while num > 0:
        binary += (num % 2) * i
        num //= 2
        i *= 10

    return binary, int(log10(i))

def decimal(num):
    dec = 0
    i = 0

    while num > 0:
        dec += (num % 10) * (2 ** i)
        num //= 10
        i += 1

    return dec

def max_shift(num):
    curr, length = binary(num)
    max_value = curr

    for i in range(length):
        remainder = curr % 10
        curr //= 10
        curr += remainder * (10 ** (length - 1))

        if decimal(curr) > decimal(max_value):
            max_value = curr

    return decimal(max_value)

if __name__ == '__main__':
    n = int(input())
    print(max_shift(n))

