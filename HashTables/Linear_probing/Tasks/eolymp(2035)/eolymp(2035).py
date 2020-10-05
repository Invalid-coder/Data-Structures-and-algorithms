class HashTable():
    def __init__(self, items):
        self.max_size = 1001
        self.current_size = 0
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size
        self.initTable(items)

    def initTable(self, items):
        for item in items:
            self.put(item)

    def hash(self, key):
        h = 0
        N = 31

        for c in key:
            h = h * N + ord(c)

        return h % self.max_size

    def occupancy(self):
        return self.current_size / self.max_size

    def expandTable(self):
        self.max_size *= 2
        self.current_size = 0
        keys, values = self.keys, self.values

        for key, value in zip(keys, values):
            if not key is None:
                self[key] = value

    def put(self, key):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                return

            current = (current + 1) % self.max_size

        self.keys[current] = key
        self.values[current] = current
        self.current_size += 1

        if self.occupancy() >= 0.7:
            self.expandTable()

    def get(self, key):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                return self.values[current]

            current = (current + 1) % self.max_size

        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return not item is None

if __name__ == '__main__':
    with open('input.txt') as inp:
        n = int(inp.readline())
        dictionary = [inp.readline().rstrip('\n') for _ in range(n)]
        hashTable = HashTable(dictionary)

        for line in inp:
            line = line.rstrip('\n').split()

            for i,word in enumerate(line):
                pass



