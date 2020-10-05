#https://www.e-olymp.com/uk/submissions/7352188

maxN = 14
d = [0] * maxN
c = [0] * maxN
maxProfit = 0

def findMaxProfit(profit, sold, day):
    global maxProfit

    if len(sold) == n:
        if profit > maxProfit:
            maxProfit = profit

        return

    for i in range(n):
        if not i in sold:
            next_sold = sold[:]
            next_sold.append(i)
            diff = d[i] - day
            nextProfit = profit + c[i] * diff if diff > 0 else profit
            findMaxProfit(nextProfit, next_sold, day + 1)

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        d[i], c[i] = map(int, input().split())

    findMaxProfit(0, [], 0)
    print(maxProfit)
