"""
Given a string of capital letters of the Latin alphabet.
It is necessary to find the length of the largest palindrome,
which can be obtained by deleting some letters from the given string.
"""

if __name__ == '__main__':
    s = input("s = ")
    n = len(s)
    L = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for k in range(n - 2, -1, -1):
        for j in range(k + 1):
             i = k - j

             if s[n - i - 1] == s[j]:
                 L[n - i - 1][j] = L[n - i - 2][j + 1] + 2
             else:
                 L[n - i - 1][j] = max(L[n - i - 2][j], L[n - i - 1][j + 1])

    for i in L:
        print(i)

    print(L[n - 1][0])