class HashTable():
    def __init__(self, N, M):
        self.max_size = N
        self.slots = [None] * self.max_size
        self.collisions = 0
        self.initTable(M)

    def initTable(self, M):
        for i in range(M):
            self.put(i)

    def hash(self, key):
        return key % self.max_size

    def put(self, key):
        current = self.hash(key)

        while not self.slots[current] is None:
            if self.slots[current] != key:
                self.collisions += 1
            else:
                return

            current = (current + 1) % self.max_size

        self.slots[current] = key

    def averageCollisionAmount(self, total):
        return self.collisions / total

if __name__ == '__main__':
    N, M = map(int, input().split())
    hashTable = HashTable(N,M)
    print("%.9f" % hashTable.averageCollisionAmount(M))