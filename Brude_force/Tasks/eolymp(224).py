maxProfit = 0

def findMaxProfit(expences, curr):
    global maxProfit

    if curr == N:
        profit = sum(profits) - expences

        if profit > maxProfit:
            maxProfit = profit

        return

    for A,B,wayCost in ways:
        if A == curr:
            if B != N:
                taxes = sum(map(lambda x, y: x * y / 100, profits, percentages[B - 2]))
                expences += taxes
                expences += wayCost
                findMaxProfit(expences, B)
            else:
                findMaxProfit(expences + wayCost, B)

if __name__ == '__main__':
    N, M = map(int, input().split())
    products = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    profits = list(map(lambda x, y: x * y, products, prices))
    percentages = [list(map(int, input().split())) for _ in range(N - 2)]
    ways = [list(map(int, input().split())) for _ in range(M)]
    findMaxProfit(0, 1)

    print('%.2f' % maxProfit)