#https://www.e-olymp.com/uk/submissions/7458335

OPERATORS = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
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

def convert_to_polish(infix):
    operand = ""
    stack = Stack()
    postfixList = []

    for token in infix:
        if token in OPERATORS:
            if operand:
                postfixList.append(operand)
                operand = ""

            while not stack.empty():
                prev = stack.back()

                if prev in OPERATORS and OPERATORS[token] <= OPERATORS[prev]:
                    stack.pop()
                    postfixList.append(prev)
                else:
                    break

            stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            it = stack.pop()

            if operand:
                postfixList.append(operand)
                operand = ""

            while it != "(":
                postfixList.append(it)
                it = stack.pop()
        else:
            operand += token

    if operand:
        postfixList.append(operand)

    while not stack.empty():
        postfixList.append(stack.pop())

    return postfixList

def simple_operations(left, right, operator):
    res = 0

    if len(left) > 90:
        return None
    if len(right) > 90:
        return None

    left, right = int(left), int(right)

    if operator == "+":
        res = left + right
    elif operator == "-":
        res = left - right
    elif operator == "*":
        res = left * right
    else:
        if right != 0:
            res = left // right
        else:
            res = -1

    if len(str(res)) > 90 or res < 0:
        return None
    else:
        return str(res)

def calculate_by_polish(postfixList):
    stack = Stack()

    for token in postfixList:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()

            res = simple_operations(left, right, token)
            stack.push(res)

            if not res:
                break
        else:
            stack.push(token)

    return stack.pop()

if __name__ == '__main__':
    with open("input.txt") as inp:
        for line in inp.readlines():
            line = line.rstrip()
            res = calculate_by_polish(convert_to_polish(line))

            if res:
                print(res)
            else:
                print("Error")
