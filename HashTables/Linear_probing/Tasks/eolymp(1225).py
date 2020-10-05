#https://www.e-olymp.com/uk/submissions/7282623

if __name__ == '__main__':
    m,n = map(int, input().split())
    A = list(map(int, input().split()))
    U = list(map(int, input().split()))

    i = 0

    for u in U:
        a = sorted(A[:u])
        print(a[i])
        i += 1