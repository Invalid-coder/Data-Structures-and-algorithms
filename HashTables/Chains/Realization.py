class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.valid = True
        self.next = None

class HashTable():
    MAX_SIZE = 11

    def __init__(self):
        self.slots = [None] * HashTable.MAX_SIZE
        self.current_size = 0

    @staticmethod
    def hash(key):
        if isinstance(key, int):
            return key % HashTable.MAX_SIZE
        elif isinstance(key, str):
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

                slot.value = value

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

    def remove(self, key):
        if not key in self:
            raise Exception("")

        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                if not slot.valid:
                    raise Exception("")
                else:
                    slot.valid = False
                    self.current_size -= 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return not self[item] is None

    def __len__(self):
        return self.current_size
