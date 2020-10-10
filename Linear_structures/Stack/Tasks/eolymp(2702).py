#https://www.e-olymp.com/uk/submissions/7458544

def get_int_digit(digit):
    if digit.isdigit():
        return int(digit)
    else:
        return ord(digit) - ord('A') + 10

def decimal(num, base):
    d = 0

    for i, c in enumerate(num[::-1]):
        digit = get_int_digit(c)

        if digit >= base:
            return None

        d += digit * (base ** i)

    return d

def findMinNotation(a, b, c):
    for base in range(2, 37):
        a1, b1, c1 = decimal(a, base), decimal(b, base), decimal(c, base)

        if a1 and b1 and c1:
            if a1 + b1 == c1:
                return base

    return -1

if __name__ == '__main__':
    AB,C = input().split("=")
    A,B = AB.split("+")

    print(findMinNotation(A,B,C))
