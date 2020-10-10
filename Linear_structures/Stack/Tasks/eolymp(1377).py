#https://www.e-olymp.com/uk/submissions/7458662

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

def findNotations(x, y):
    for b1 in range(2, 37):
        for b2 in range(2, 37):
            if b1 != b2:
                x1, y1 = decimal(x, b1), decimal(y, b2)

                if x1 and y1:
                    if x1 == y1:
                        return (b1, b2)

    return None

if __name__ == '__main__':
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.rstrip()
            x,y = line.split()
            bases = findNotations(x, y)

            if bases:
                print("{} (base {}) = {} (base {})".format(x, bases[0], y, bases[1]))
            else:
                print("{} is not equal to {} in any base 2..36".format(x, y))