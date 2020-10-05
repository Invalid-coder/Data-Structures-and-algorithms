#https://www.e-olymp.com/uk/submissions/7285479

class Node():
    def __init__(self, key, value=1):
        self.key = key
        self.value = value
        self.next = None

class HashTable():
    MAX_SIZE = 11

    def __init__(self, item):
        self.slots = [None] * HashTable.MAX_SIZE
        self.current_size = 0
        self.initTable(item)

    def initTable(self, item):
        for c in item:
            self.put(c)

    @staticmethod
    def hash(key):
        return ord(key) % HashTable.MAX_SIZE

    def put(self, key):
        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                slot.value += 1
                return

            slot = slot.next

        node = Node(key)
        node.next = self.slots[hash]
        self.slots[hash] = node
        self.current_size += 1

    def get(self, key):
        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                return slot.value

            slot = slot.next

        return None

    def __getitem__(self, item):
        return self.get(item)


if __name__ == '__main__':
    word = input()
    N = int(input())
    dictionary = [input() for _ in  range(N)]
    table = HashTable(word)
    counter = 0

    for item in dictionary:
        itemTable = HashTable(item)
        isDone = True

        for c in item:
            if table[c] is None or table[c] < itemTable[c]:
                isDone = False
                break

        if isDone:
            counter += 1

    print(counter)
