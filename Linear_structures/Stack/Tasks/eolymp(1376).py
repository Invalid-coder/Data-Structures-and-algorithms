def get_int_digit(digit, base):
    if digit.isdigit():
        if int(digit) >= base:
            return None
        else:
            return int(digit)
    else:
        if ord(digit) - ord('A') + 10 >= base:
            return None
        else:
            return ord(digit) - ord('A') + 10

def get_char_digit(digit):
    if digit <= 9:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def to_decimal(num, base):
    dec = 0

    if base == 10:
        return int(num)

    for i,c in enumerate(num[::-1]):
        digit = get_int_digit(c, base)

        if digit is None:
            return None

        dec += digit * (base ** i)

    return dec

def convert(num, base):
    if num is None:
        return None

    if base == 10:
        return num

    stack = []

    while num > 0:
        stack.append(num % base)
        num //= base

    converted = ''

    while len(stack) != 0:
        converted += get_char_digit(stack.pop())

    return converted

if __name__ == '__main__':
    with open('input.txt') as inp:
        for line in inp.readlines():
            b1, b2, num = line.rstrip().split()
            b1, b2 = int(b1), int(b2)
            number = convert(to_decimal(num, b1), b2)

            if number:
                print("{} base {} = {} base {}".format(num, b1, number, b2))
            else:
                print("{} is an illegal base {} number".format(num, b1))