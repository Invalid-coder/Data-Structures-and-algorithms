import sys

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

permutations = []

def findPermutations(brackets):
    global counter

    if not '?' in brackets:
        if bracketsChecker(brackets):
            if not brackets in permutations:
                permutations.append(brackets)

        return

    for i in range(len(brackets)):
        if brackets[i] == '?':
            for bracket in '()':
                next_lst = brackets[:]
                next_lst[i] = bracket
                findPermutations(next_lst)

counter = 0

def find_permutations_amount(n, k):
    global counter

    if k < 0:
        return

    if n == length:
        if k == 0:
            counter += 1

        return

    if expression[n] == '(':
        find_permutations_amount(n + 1, k + 1)
    elif expression[n] == ')':
        find_permutations_amount(n + 1, k - 1)
    else:
        find_permutations_amount(n + 1, k + 1)
        find_permutations_amount(n + 1, k - 1)

if __name__ == '__main__':
    sys.setrecursionlimit(1500000)
    expression = list(input())
    length = len(expression)
    findPermutations(expression)
    print(len(permutations))
    find_permutations_amount(0,0)
    print(counter)