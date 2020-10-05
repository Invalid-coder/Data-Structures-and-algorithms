#https://www.e-olymp.com/uk/submissions/7394611

class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def back(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

def get_int_digit(digit):
    if digit.isdigit():
        return int(digit)
    else:
        return ord(digit) - ord('A') + 10

def get_char_digit(digit):
    if digit <= 9:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def to_decimal(num, base):
    d = 0

    for i, c in enumerate(num[::-1]):
        d += (get_int_digit(c)) * (base ** i)

    return d

def convert(num, base):
    stack = Stack()

    while num > 0:
        stack.push(num % base)
        num //= base

    converted = ''

    while not stack.empty():
        converted += get_char_digit(stack.pop())

    return converted

if __name__ == '__main__':
    m, k = map(int, input().split())
    num = input()
    print(convert(to_decimal(num, m), k))