#https://www.e-olymp.com/uk/submissions/7366704

maxProfit = 0

def findMaxProfit(profit, time, served):
    global maxProfit

    if len(served) >= n:
        if profit > maxProfit:
            maxProfit = profit

        return

    for i in range(n):
        if i not in served:
            nextServed = served[:]
            nextServed.append(i)
            tips = arr[i] - time
            findMaxProfit(profit + tips if tips > 0 else profit, time + 1, nextServed)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    findMaxProfit(0, 0, [])

    print(maxProfit)

