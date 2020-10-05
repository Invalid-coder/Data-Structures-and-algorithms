#https://www.e-olymp.com/uk/submissions/7282787

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.valid = True
        self.next = None

class HashTable():
    MAX_SIZE = 11

    def __init__(self):
        self.slots = [None] * HashTable.MAX_SIZE
        self.current_size = 0

    @staticmethod
    def hash(key):
        h = 0
        N = 31

        for c in key:
            h = h * N + ord(c)

        return h % HashTable.MAX_SIZE

    def put(self, key, value):
        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                if not slot.valid:
                    slot.valid = True
                    self.current_size += 1

                slot.value.append(value)
                return

            slot = slot.next

        node = Node(key, value)
        node.next = self.slots[hash]
        self.slots[hash] = node
        self.current_size += 1

    def get(self, key):
        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                if slot.valid:
                    return slot.value
                else:
                    return None

            slot = slot.next

        return None

    def print(self):
        valid = []

        for i in range(HashTable.MAX_SIZE):
            slot = self.slots[i]

            while not slot is None:
                valid.append(slot)
                slot = slot.next

        lexicographical = sorted(valid, key=lambda x: x.key)

        for item in lexicographical:
            value = sorted(item.value)

            print("{} - {}".format(item.key, ', '.join(value)))

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __len__(self):
        return self.current_size

if __name__ == '__main__':
    latin = HashTable()

    with open('input.txt') as inp:
        for line in inp:
            eng, trans = line.rstrip().split(' - ')
            trans = trans.split(', ')

            for t in trans:
                t = t.rstrip()
                latin[t] = eng

    print(len(latin))
    latin.print()