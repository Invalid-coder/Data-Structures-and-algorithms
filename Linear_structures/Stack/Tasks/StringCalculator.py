from Linear_structures.Stack.Realization.recursively import *

#Operator's priorities
OPERATORS = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
}

class StrCalculator():
    def __init__(self, expression):
        self.infixStr = expression
        self.postfix_list = self.convert_to_polish()

    def set_expression(self, expression):
        self.infixStr = expression
        self.postfix_list = self.convert_to_polish()

    def convert_to_polish(self):
        stack = Stack()
        postfix_list = []
        infixList = self.infixStr.split()

        for token in infixList:
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

    @staticmethod
    def simple_operations(left, right, operator):
        assert operator in OPERATORS

        left = float(left)
        right = int(right)

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        else:
            return left / right

    def calculate_by_polish(self):
        stack = Stack()

        for token in self.postfix_list:
            if token in OPERATORS:
                right = stack.pop()
                left = stack.pop()

                res = StrCalculator.simple_operations(left, right, token)
                stack.push(res)
            else:
                stack.push(token)

        return stack.pop()


if __name__ == '__main__':
    calculator = StrCalculator('25 * ( 3 + 5 )')
    print(calculator.calculate_by_polish())