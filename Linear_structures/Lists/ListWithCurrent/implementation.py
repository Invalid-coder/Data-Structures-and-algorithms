class ListInterator():
    def __init__(self, lst):
        self.cursor = lst.head

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        else:
            curr = self.cursor.item
            self.cursor = self.cursor.next
            return curr

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class ListWithCurrent():
    def __init__(self):
        self.head = None
        self.curr = None

    def empty(self):
        return self.head is None

    def reset(self):
        self.curr = self.head

    def current(self):
        if self.curr is None:
            return None
        else:
            return self.curr.item

    def next(self):
        if self.empty() or self.curr.next is None:
            raise StopIteration
        else:
            self.curr = self.curr.next

    def insert(self, item):
        node = Node(item)

        if self.empty():
            self.head = node
            self.curr = node
        else:
            node.next = self.curr.next
            self.curr.next = node

    def __str__(self):
        return str(self.current())

    def __iter__(self):
        return ListInterator(self)


if __name__ == '__main__':
    l = ListWithCurrent()
    l.insert(1)
    l.insert(2)
    l.insert(3)

    for el in l:
        print(el)

    it = iter(l)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break