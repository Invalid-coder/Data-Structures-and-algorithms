#https://www.e-olymp.com/uk/submissions/7482704

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item); return "ok"
    def pop(self): return self.items.pop(0)
    def front(self): return self.items[0]
    def size(self): return len(self.items)
    def clear(self): self.items.clear(); return "ok"
    def exit(self): return "bye"

    def execute(self, command):
        if command.startswith("push"):
            return self.push(command[5:])
        else:
            return getattr(self, command)()

if __name__ == '__main__':
    queue = Queue()

    with open("input.txt") as input:
        with open("output.txt", "w") as output:
            for line in input:
                res = queue.execute(line.rstrip())
                print(res, file=output)
                if res == "bye":
                    break
