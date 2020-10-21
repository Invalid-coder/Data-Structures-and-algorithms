#https://www.e-olymp.com/uk/submissions/7546403

import sys

sys.setrecursionlimit(100000000)

def dfs(v):
    if len(s[colors[v]]) > 0:
        ans[v] = s[colors[v]][-1]

    s[colors[v]].append(v)

    for u in nodes[v]:
        dfs(u)

    s[colors[v]].pop()

if __name__ == '__main__':
    n, c = map(int, input().split())
    parents = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    nodes = [[] for _ in range(n)]
    ans = [-2 for _ in range(n)]
    s = [[] for _ in range(c + 1)]

    for i in range(n - 1):
        nodes[parents[i] - 1].append(i + 1)

    print(nodes)
    dfs(0)

    for x in ans:
        print(x + 1, end=' ')

"""
#https://www.e-olymp.com/uk/submissions/7546202

def bfs(root):
    node = nodes[root]

    while node != -1:
        if colors[node] == colors[root]:
            return node + 1

        node = nodes[node]

    return -1

if __name__ == '__main__':
    n, c = map(int, input().split())
    parents = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    nodes = [-1 for _ in range(n)]

    for i in range(n - 1):
        nodes[i + 1] = parents[i] - 1

    for i in range(n):
        print(bfs(i), end=' ')
"""

