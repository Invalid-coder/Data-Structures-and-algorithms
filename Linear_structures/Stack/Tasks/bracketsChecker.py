from Linear_structures.Stack.Realization.recursively import *

def bracketsChecker(brackets_sequence):
    stack = Stack()

    for bracket in brackets_sequence:
        if bracket == '(':
            stack.push(bracket)
        else:
            if stack.empty():
                return False
            else:
                stack.pop()

    return stack.empty()

if __name__ == '__main__':
    print(bracketsChecker('(())'))
    print(bracketsChecker('(())((('))