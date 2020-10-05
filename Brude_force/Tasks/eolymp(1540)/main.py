#https://www.e-olymp.com/uk/submissions/7325825

possible = False
operators = '+-*'

def simple_operation(left, right, operator):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    else:
        return left * right

def findPossibility(result, lst):
    global possible, operators

    if len(lst) == 0:
        if result == 23:
            possible = True

        return

    for i in range(len(lst)):
        for operator in operators:
            next_lst = lst[:]
            nextResult = simple_operation(result, next_lst.pop(i),  operator)

            if nextResult < 0 or nextResult > 23:
                break

            findPossibility(nextResult, next_lst)

if __name__ == '__main__':
    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.rstrip()

            if line != '0 0 0 0 0':
                arr = list(map(int, line.split()))

                for i in range(len(arr)):
                    findPossibility(arr[i], arr[:i] + arr[i + 1:])

                print('Possible' if possible else 'Impossible')

                possible = False
