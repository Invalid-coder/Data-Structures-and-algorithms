#https://www.e-olymp.com/uk/submissions/7326627

def findMinBudget(budget, lst, curr):
    global minBudget

    if curr >= n:
        if budget < minBudget:
            minBudget = budget

        return

    for i in range(n):
        if i not in lst:
            next_lst = lst[:]
            next_lst.append(i)
            findMinBudget(budget + arr[curr][i], next_lst, curr + 1)

if __name__ == '__main__':
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    minBudget = 1000 * n
    lst = []
    findMinBudget(0, lst, 0)
    print(minBudget)

