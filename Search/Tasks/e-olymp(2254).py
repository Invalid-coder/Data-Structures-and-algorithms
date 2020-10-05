def get_amount(point, coords, b):
    budget = 0
    amount = 0

    for c in coords:
        if abs(c - point) + budget > b:
            continue
        else:
            budget += abs(c - point)
            amount += 1

    return amount

def binary_search(coords, l, b):
    left = 0
    right = l
    max_amount = 0

    while right - left != 1:
        mid = (left + right) // 2
        amount = get_amount(mid, coords, b)

        if amount < max_amount:
            left = mid
        else:
            right = mid
            max_amount = amount

    return max_amount

if __name__ == '__main__':
    r,l,b = map(int, input().split())
    x = [int(input()) for i in range(r)]
    print(binary_search(x, l, b))