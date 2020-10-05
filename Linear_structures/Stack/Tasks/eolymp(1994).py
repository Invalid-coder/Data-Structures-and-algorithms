#https://www.e-olymp.com/uk/submissions/7390351

b = {'(': ')', ')': '('}

class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def isCorrect(brackets):
    stack = Stack()

    for bracket in brackets:
        if bracket == '(':
            stack.push(bracket)
        else:
            if stack.empty():
                return False
            else:
                stack.pop()

    return stack.empty()

if __name__ == '__main__':
    brackets = list(input())
    k = int(input())

    for i in range(k):
        j = int(input())
        brackets[j] = b[brackets[j]]

        print('+' if isCorrect(brackets) else '-')
