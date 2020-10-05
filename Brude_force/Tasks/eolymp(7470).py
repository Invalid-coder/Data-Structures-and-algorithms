payable = False

def checkPayability(suma, bills, num):
    global payable

    if num >= n:
        payable = True

        return

    for bill in bills:
        next_bills = bills[:]
        next_bills.remove(bill)

        if suma + bill == salaries[num]:
            checkPayability(0, next_bills, num + 1)
        elif suma + bill < salaries[num]:
            checkPayability(suma + bill, next_bills, num)


if __name__ == '__main__':
    n, m = map(int, input().split())
    salaries = list(map(int, input().split()))
    bills = list(map(int, input().split()))
    checkPayability(0, bills, 0)

    print('Yes' if payable else 'No')
