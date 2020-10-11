#https://www.e-olymp.com/uk/submissions/7489309

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None and self.back is None

    def append(self, item):
        node = Node(item)

        if self.empty():
            self.front = node
        else:
            self.back.next = node

        self.back = node

    def pop(self):
        front = self.front
        item = front.item
        self.front = self.front.next
        del front

        if self.front is None:
            self.back = None

        return item

    def getFront(self):
        return self.front.item

    def getBack(self):
        return self.back.item

def sort(n, arr, k):
    queues = [Queue() for _ in range(k)]
    I = []
    ans = None

    for item in arr:
        inserted = False

        for i, queue in enumerate(queues):
            if queue.empty():
                queue.append(item)
                I.append(i)
                inserted = True
            else:
                if queue.getBack() <= item:
                    queue.append(item)
                    I.append(i)
                    inserted = True

            if inserted:
                break

        if not inserted:
            print("NO")
            return

    print("YES")

    for i in I:
        print("I({})".format(i + 1))

    while n > 0:
        minpos = 0
        i = 0

        while i < len(queues):
            if not queues[i].empty():
                if queues[i].getFront() < queues[minpos].getFront():
                    minpos = i
            else:
                queues.pop(i)

            i += 1

        queues[minpos].pop()
        print("R({})".format(minpos + 1))
        n -= 1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    sort(n, arr, k)

