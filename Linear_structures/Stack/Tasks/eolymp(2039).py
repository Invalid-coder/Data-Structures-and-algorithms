class Stack():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return " ".join(self.items)

def getHeight(latex, s, d):
    i = 0
    stack = Stack()
    maxHeight = float("-inf")
    curr = 0

    while i < len(latex) - 1:
        if latex[i] == "\\":
            i += 5

            if latex[i] != "{":
                i += 1
                curr += s
                curr += d

                if latex[i + 1] == " ":
                    i += 2
                    curr += s
                else:
                    if stack.empty():
                        curr += s
                        maxHeight = max(maxHeight, curr)
                        curr = 0

                    i += 2
            else:
                curr += s

        if latex[i] == "{":
            stack.push(latex[i])
        elif latex[i] == "}":
            stack.pop()

            if latex[i + 1] != "{" and not latex[i + 1].isalnum():
                maxHeight = max(maxHeight, curr)
                curr = 0
            else:
                curr += d

                if stack.empty():
                    curr += s

        i += 1

    return maxHeight

if __name__ == '__main__':
    S, D = map(int, input().split())
    latex = input()
    print(getHeight(latex, S, D))