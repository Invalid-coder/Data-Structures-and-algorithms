"""
Reverse order:
All states based on the current state are updated.
"""

if __name__ == '__main__':
    n = int(input())
    fib = [0 for _ in range(n)]
    fib[0] = 1
    for i in range(n - 2):
        fib[i + 1] += fib[i]
        fib[i + 2] += fib[i]
    fib[n - 1] += fib[n - 2]
    print(fib)