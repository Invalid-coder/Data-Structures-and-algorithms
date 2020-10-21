import sys
#https://www.e-olymp.com/uk/submissions/7545719

sys.setrecursionlimit(1000000000)

def DFS(v):
    sets[v].add(colors[v])

    for next in nodes[v]:
        DFS(next)

        if len(sets[v]) < len(sets[next]):
            sets[v], sets[next] = sets[next], sets[v]

        for el in sets[next]:
            sets[v].add(el)

        sets[next].clear()

    ans[v] = len(sets[v])

if __name__ == '__main__':
    n = int(input())
    root = -1
    colors = []
    ans = [None] * n
    sets = [set() for i in range(n)]
    nodes = []  #nodes list , each node is a list of its posterity

    for i in range(n):
        nodes.append([])

    for i in range(n):
        p, c = map(int, input().split())
        colors.append(c)
        p -= 1

        if p == -1: root = i
        else: nodes[p].append(i)

    DFS(root)

    for i in range(n):
        print(ans[i], end=' ')
