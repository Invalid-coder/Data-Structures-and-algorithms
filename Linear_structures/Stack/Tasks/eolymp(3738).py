def by_stack(expression):
    stack = []
    print('stack')
    for token in expression:
        print(stack)
        if token.isupper():
            right = stack.pop()
            left = stack.pop()

            res = left + token + right
            stack.append(res)
        else:
            stack.append(token)

    return stack.pop()

def by_queue(expression):
    queue = []
    print('queue')
    print(expression)

    for token in expression:
        print(queue)
        if token.isupper():
            right = queue.pop(0)
            left = queue.pop(0)

            res = left + token + right
            queue.append(res)
        else:
            queue.append(token)

    return queue.pop()

#https://www.e-olymp.com/uk/submissions/7401244

import sys

sys.setrecursionlimit(1500000)

index = 0

def get_levels(expression, depth, answer):
    global index

    if index < 0 or depth >= len(answer) - 1:
        return

    answer[depth] += expression[index]
    index -= 1

    if expression[index + 1].isupper():
        get_levels(expression, depth + 1, answer)
        get_levels(expression, depth + 1, answer)

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        expression = input()
        n = len(expression)
        answer = [''] * n
        index = n - 1
        get_levels(expression, 0, answer)
        converted = ''

        for level in answer[::-1]:
            if level:
                converted += level

        print(converted)



