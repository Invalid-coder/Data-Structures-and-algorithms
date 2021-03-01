"""
Direct order:
The states are sequentially recalculated based on those already calculated.
"""
if __name__ == '__main__':
    n = int(input())
    fib = [0 for i in range(n)]
    fib[0], fib[1] = 1, 1

    for i in range(2, n):
        fib[i] += fib[i - 1] + fib[i - 2]

    print(fib)