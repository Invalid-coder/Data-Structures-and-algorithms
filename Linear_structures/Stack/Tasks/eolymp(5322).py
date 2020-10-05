#https://www.e-olymp.com/uk/submissions/7389924

class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def getCharDigit(digit):
    assert digit <= 16

    if digit <= 9:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def convert(num):
    stack = Stack()

    if len(num) % 4 != 0:
        num = '0' * (4 - (len(num) % 4)) + num

    n = len(num)

    for i in range(n - 1, -1, -4):
        digit = 0

        for j in range(0, 4):
            digit += int(num[i - j]) * (2 ** j)

        stack.push(digit)

    converted = ''

    while not stack.empty():
        converted += getCharDigit(stack.pop())

    return converted

if __name__ == '__main__':
    print(convert(input()))