"""
Lazy dynamics:
Recursive memoized dynamics recalculation function.
It's like a depth-first search on an acyclic state graph,
where the edges are the dependencies between them.
"""

def get_fib(n):
    if n <= 1:
        return 1
    if fib[n] != -1:
        return fib[n]

    fib[n] = get_fib(n - 1) + get_fib(n - 2)

    return fib[n]

if __name__ == '__main__':
    n = int(input())
    fib = [-1 for _ in range(n)]
    print(get_fib(n - 1))