#https://www.e-olymp.com/uk/submissions/7385719

class Stack:
    """
        Implementation by built-in list
    """

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def back(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to an empty container")
        else:
            return self.items[-1]

    def pop(self):
        if self.empty():
            raise Exception("Stack 'pop' applied to an empty container")
        else:
            return self.items.pop()

    def clear(self):
        self.items.clear()

def isPossible(n, permutation, stack):
    i = 0

    for j in range(1, n + 1):
        stack.push(j)

        while not stack.empty() and stack.back() == permutation[i]:
            stack.pop()
            i += 1

    return stack.empty()

if __name__ == '__main__':
    stack = Stack()

    with open('input.txt') as inp:
        text = inp.readlines()
        n = int(text[0])
        i = 1

        while i < len(text) - 1:
            permutation = list(map(int, text[i].split()))

            if len(permutation) == 1:
                n = int(text[i + 1])
                i += 1
                print()
            else:
                stack.clear()
                print('Yes' if isPossible(n, permutation, stack) else 'No')

            i += 1
