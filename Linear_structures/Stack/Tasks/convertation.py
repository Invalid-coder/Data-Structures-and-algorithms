from Linear_structures.Stack.Realization.recursively import *

def getIntValue(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - ord('A') + 10

def decimal(num, base):
    s = 0

    for i,c in enumerate(str(num)[::-1]):
        s += getIntValue(c) * (base ** i)

    return s

def getCharDigit(digit):
    assert digit <= 16

    if digit <= 9:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def convert(num, base):
    """
    :param num: decimal number
    :param base: the new base of the future number
    :return: converted number with a new base
    """
    assert 2 <= base <= 16

    stack = Stack()

    while num > 0:
        stack.push(num % base)
        num //= base

    converted = ''

    while not stack.empty():
        converted += getCharDigit(stack.pop())

    return converted

if __name__ == '__main__':
    print(convert(decimal(1033, 8), 8))
    print(convert(2286755, 16))