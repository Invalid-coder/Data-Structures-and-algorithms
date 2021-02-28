"""
A sequence of integers is given.
It is necessary to find its longest strictly increasing subsequence.
"""

if __name__ == '__main__':
    A = list(map(int, input().split()))
    L = [1 for _ in range(len(A))]
    N = [-1 for _ in range(len(A))]
    n = len(A)

    for k in range(1, len(A)):
        i_s = [i for i in range(k) if A[i] < A[k]]

        if not i_s:
            continue

        i = max(i_s, key=lambda x: L[x])
        N[k] = i
        L[k] = L[i] + 1

    stack = []
    current = max(range(n), key=lambda x: L[x])

    while current != -1:
        stack.append(A[current])
        current = N[current]

    way = []

    while stack:
        way.append(stack.pop())

    print(way)


