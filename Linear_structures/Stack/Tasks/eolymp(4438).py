import sys

class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

def bracketsChecker(brackets):
    stack = Stack()

    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)
        else:
            if stack.empty():
                return False

            stack.pop()

    return stack.empty()

minAmount = 100500

def findMinCycleShifts(brackets, amount):
    global minAmount

    if bracketsChecker(brackets):
        if amount < minAmount:
            minAmount = amount

        return

    for i in range(1, len(brackets)):
        findMinCycleShifts(brackets[i:] + brackets[:i], amount + 1)

def funk(brackets):
    stack = Stack()
    counter = 0

    while not bracketsChecker(brackets):
        brackets = brackets[-1] + brackets[:-1]
        counter += 1

    return counter

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    brackets = input()
    findMinCycleShifts(brackets, 0)
    print(minAmount if minAmount != 100500 else 0)
    print(funk(brackets))