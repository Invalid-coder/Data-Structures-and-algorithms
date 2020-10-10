#https://www.e-olymp.com/uk/submissions/7483115

class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, item): self.items.append(item); return "ok"
    def pop_back(self): return self.items.pop()
    def push_front(self, item): self.items.insert(0, item); return "ok"
    def pop_front(self): return self.items.pop(0)
    def front(self): return self.items[0]
    def back(self): return self.items[-1]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return "ok"
    def exit(self): return "bye"

    def execute(self, command):
        command = command.split()
        name = command[0]
        args = command[1:]

        return getattr(self, name)(*args)


if __name__ == '__main__':
    deque = Deque()

    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            for line in input:
                res = deque.execute(line.rstrip())
                print(res, file=output)

                if res == "bye":
                    break
