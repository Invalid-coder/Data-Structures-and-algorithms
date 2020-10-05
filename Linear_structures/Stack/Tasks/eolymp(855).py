#https://www.e-olymp.com/uk/submissions/7394286

B = {')' : '(', ']' : '['}

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


def bracektsChecker(brackets):
    stack = Stack()

    for bracket in brackets:
        if bracket in '([':
            stack.push(bracket)
        else:
            if stack.empty():
                return False

            if stack.back() != B[bracket]:
                return False
            else:
                stack.pop()

    return stack.empty()

def findBrackets(brackets):
    if len(brackets) == n:
        if bracektsChecker(brackets):
            print(brackets)

        return

    for bracket in '()[]':
        findBrackets(brackets + bracket)

#https://www.e-olymp.com/uk/submissions/7394389
permutations = []

def brude_force(brackets):
    global permutations

    if len(brackets) == n:
        if not brackets in permutations:
            permutations.append(brackets)

        return

    for i in range(len(brackets)):
        for b in ['()', '[]']:
            brude_force(brackets[:i] + b + brackets[i:])

if __name__ == '__main__':
    n = int(input())
    #First solution
    findBrackets('')

    #Second solution
    brude_force('()')
    brude_force('[]')

    for p in permutations:
        print(p)




