#https://www.e-olymp.com/uk/submissions/7374649

class Stack():
    def __init__(self):
        self.items = []

    def empty(self): return len(self.items) == 0
    def push(self, item): self.items.append(item); return 'ok'
    def back(self): return self.items[-1]
    def pop(self): return self.items.pop()
    def clear(self): self.items.clear(); return 'ok'
    def size(self): return len(self.items)
    def exit(self): return 'bye'

    def execute(self, command):
        if command.startswith('push'):
            return self.push(command[5:])
        else:
            return getattr(self, command)()

if __name__ == '__main__':
    stack = Stack()

    with open('input.txt') as input:
        with open('output.txt', 'w') as output:
            for line in input:
                result = stack.execute(line.rstrip())
                print(result, file=output)

                if result == 'bye':
                    break