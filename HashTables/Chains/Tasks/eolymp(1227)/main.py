#https://www.e-olymp.com/uk/submissions/7282880

class Node():
    def __init__(self, key):
        self.key = key
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

    def put(self, key):
        hash = HashTable.hash(key)
        slot = self.slots[hash]

        while not slot is None:
            if slot.key == key:
                if not slot.valid:
                    slot.valid = True
                    self.current_size += 1

                return

            slot = slot.next

        node = Node(key)
        node.next = self.slots[hash]
        self.slots[hash] = node
        self.current_size += 1

    def print(self):
        valid = []

        for i in range(HashTable.MAX_SIZE):
            slot = self.slots[i]

            while not slot is None:
                valid.append(slot)
                slot = slot.next

        valid = sorted(valid, key=lambda x: x.key)

        for item in valid:
            print(item.key)

def isLetter(letter):
    if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        return True
    else:
        return False

def add(word, hashTable):
    chunk = ''
    i = 0

    while i < len(word):
        while i < len(word) and isLetter(word[i]):
            chunk += word[i]
            i += 1

        if chunk:
            hashTable.put(chunk)
            chunk = ''

        while i < len(word) and not isLetter(word[i]):
            i += 1

if __name__ == '__main__':
    hashTable = HashTable()

    with open("input.txt") as inp:
        for line in inp:
            words = line.split()

            for word in words:
                word = word.lower().strip('"').rstrip('":;,.')
                add(word, hashTable)

    hashTable.print()