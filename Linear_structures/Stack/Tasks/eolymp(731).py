#https://www.e-olymp.com/uk/submissions/7391485

OPERATORS = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
}

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

def convert_to_infix(expression):
    stack = Stack()
    infix_list = []
    prev = 2

    for token in expression[::-1]:
        if token in OPERATORS:
            left = stack.pop()
            right = stack.pop()
            done = False

            if token == '-':
                if '-' in right or '+' in right:
                    done = True

            left = ''.join(left) if isinstance(left, list) else left
            right = ''.join(right) if isinstance(right, list) else right

            if done:
                right = '({})'.format(right)

            if prev < OPERATORS[token]:
                if len(right) > 1:
                    right = '({})'.format(right)

                if len(left) > 1:
                    left = '({})'.format(left)

            res = [left, token, right]
            prev = OPERATORS[token]
            stack.push(res)
        else:
            stack.push(token)

    return ''.join(stack.pop())


if __name__ == '__main__':
    expression = input()
    print(convert_to_infix(expression))
