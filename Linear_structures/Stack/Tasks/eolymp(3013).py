class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def __len__(self):
        return len(self.items)

def reduce(brackets):
    n = len(brackets)

    for i in range(n - 1, -1, -1):
        if brackets[i] > 1:
            brackets[i] -= 1

def bracketsChecker(brackets):
    stack = Stack()
    magicBrackets = []
    counter = 0

    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)

            if counter < 0:
                counter = 0

            counter += 1
        elif bracket == ')':
            if stack.empty():
                return None, None

            stack.pop()
            counter -= 1

            if len(stack) < len(magicBrackets):
                return None,None

            if counter < 0:
                reduce(magicBrackets)
        else:
            if len(stack) < len(magicBrackets) or stack.empty():
                return None,None

            magicBrackets.append(counter if counter > 0 else len(stack))
            counter = 0

    if counter > 0:
        return None, None

    return magicBrackets, len(stack)

if __name__ == '__main__':
    n, m = map(int, input().split())
    brackets = input()
    res, amount = bracketsChecker(brackets)

    if res:
        print(1)

        for i in res:
            k = amount // m

            if k <= i:
                print(k)
                amount -= k
            else:
                print(i)
                amount -= i

            m -= 1
    else:
        print(0)