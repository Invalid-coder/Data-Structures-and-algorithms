#https://www.e-olymp.com/uk/submissions/7484106

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue():
    def __init__(self, items):
        self.front = None
        self.back = None
        self.initQueue(items)

    def initQueue(self, items):
        for item in items.split():
            self.append(int(item))

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

def winner_card(card1, card2, n):
    if card1 == 0 and card2 == n - 1:
        return card1
    elif card2 == 0 and card1 == n - 1:
        return card2
    else:
        return card1 if card1 > card2 else card2

if __name__ == '__main__':
    n = int(input())
    p1 = Queue(input())
    p2 = Queue(input())
    counter = 0

    while counter < 2 * (10 ** 5):
        if p1.empty() or p2.empty():
            break

        c1 = p1.pop()
        c2 = p2.pop()

        if winner_card(c1, c2, n) == c1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c1)
            p2.append(c2)

        counter += 1

    if p1.empty():
        print("second", counter)
    elif p2.empty():
        print("first", counter)
    else:
        print("draw")

