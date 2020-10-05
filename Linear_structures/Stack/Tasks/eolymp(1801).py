#https://www.e-olymp.com/uk/submissions/7419759

OPERATORS = {
    '+': 1,
    '*': 2,
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

def insertMul(exp):
    exp = list(exp)
    i = 1

    while True:
        if i >= len(exp):
            break

        if exp[i - 1].isalpha() and exp[i].isalpha():
            exp.insert(i, '*')
            i += 1
        elif exp[i - 1].isalpha() and exp[i] == '(':
            exp.insert(i, '*')
            i += 1
        elif exp[i - 1] == ')' and exp[i].isalpha():
            exp.insert(i, '*')
            i += 1
        elif exp[i - 1] == ')' and exp[i] == '(':
            exp.insert(i, '*')
            i += 1

        prev = exp[i]
        i += 1

    return ''.join(exp)

def convert_to_polish(infix):
    stack = Stack()
    postfix_list = []

    for token in infix:
        if token in OPERATORS:
            while not stack.empty():
                prev = stack.back()

                if prev in OPERATORS and OPERATORS[token] <= OPERATORS[prev]:
                    stack.pop()
                    postfix_list.append(prev)
                else:
                    break

            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            it = stack.pop()

            while it != '(':
                postfix_list.append(it)
                it = stack.pop()
        else:
            postfix_list.append(token)

    while not stack.empty():
        postfix_list.append(stack.pop())

    return postfix_list

def simple_operations(left, right, token):
    isLeft, isRight = False, False

    if token == '*':
        if '+' in left:
            isLeft = True
        if '+' in right:
            isRight = True

    left = ''.join(left) if isinstance(left, list) else left
    right = ''.join(right) if isinstance(right, list) else right

    if isLeft:
        left = '({})'.format(left)

    if isRight:
        right = '({})'.format(right)

    return [left, token, right]

def calculate_by_polish(postfix_list):
    stack = Stack()

    for token in postfix_list:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            res = simple_operations(left, right, token)
            stack.push(res)
        else:
            stack.push(token)

    return ''.join(stack.pop()).replace('*', '')

if __name__ == '__main__':
    with open('input.txt') as inp:
        for line in inp.readlines():
            infixStr = line.rstrip()

            print(calculate_by_polish(convert_to_polish(insertMul(infixStr))))