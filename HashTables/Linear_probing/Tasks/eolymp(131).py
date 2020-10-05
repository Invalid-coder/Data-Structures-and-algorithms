#https://www.e-olymp.com/uk/submissions/7278686

class HashTable():
    def __init__(self, item):
        self.max_size = 11
        self.current_size = 0
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size
        self.initTable(item)

    def initTable(self, item):
        for c in item:
            self.put(c)

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

    def put(self, key, value=1):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                self.values[current] += 1
                return

            current = (current + 1) % self.max_size

        self.keys[current] = key
        self.values[current] = value
        self.current_size += 1

        if self.occupancy() >= 0.7:
            pass

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
        return not self[item] is None

if __name__ == '__main__':
    word = input()
    N = int(input())
    dictionary = [input() for _ in range(N)]
    word = HashTable(word)
    counter = 0

    for item in dictionary:
        s = set(item)
        item = HashTable(item)
        done = True

        for letter in s:
            if not letter in word or word[letter] < item[letter]:
                done = False
                break

        if done:
            counter += 1

    print(counter)

