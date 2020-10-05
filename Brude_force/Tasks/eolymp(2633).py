maxWeight = 0

def findMaxWeight(weight, cookies, index):
    global maxWeight

    if cookies >= n:
        if weight > maxWeight:
            maxWeight = weight

        return

    if index >= 2 * n:
        return

    findMaxWeight(weight, cookies, index + 1)
    findMaxWeight(weight + weights[index], cookies + 1, index + 2)

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    findMaxWeight(weights[0], 1, 2)

    print(maxWeight)