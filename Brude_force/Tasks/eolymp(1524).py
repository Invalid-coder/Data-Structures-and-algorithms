#https://www.e-olymp.com/uk/submissions/7343763

amount = 0

def findWaysAmount(suma, num):
    global amount

    if num >= n:
        if suma == t:
            amount += 1

        return

    for grade in range(p, maxGrade + 1):
        if suma + grade <= t:
            findWaysAmount(suma + grade, num + 1)

if __name__ == '__main__':
    tests = int(input())

    for i in range(tests):
        n, t, p = map(int, input().split())
        maxGrade = (t - p * (n - 1))
        findWaysAmount(0, 0)

        print(amount)

        amount = 0