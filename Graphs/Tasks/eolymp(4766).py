#https://www.e-olymp.com/uk/submissions/7687434

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        row = list(map(int, input().split()))

        for j in range(n):
            if row[j] == 1:
                print(f"{i} {j + 1}")
