#https://www.e-olymp.com/uk/submissions/7276977

class HashTable:
    def __init__(self):
        self.max_size = 11
        self.current_size = 0
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size

    def hash(self, key):
        if isinstance(key, int):
            return key % self.max_size
        elif isinstance(key, str):
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
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size

        for key, value in zip(keys, values):
            if not key is None:
                for v in value:
                    self[key] = v

    def put(self, key, value):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                self.values[current].append(value)
                return

            current = (current + 1) % self.max_size

        self.keys[current] = key
        self.values[current] = [value]
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

    def print(self):
        words = [(self.keys[i], i) for i in range(self.max_size) if not self.keys[i] is None]
        lexicographical = sorted(words, key=lambda x: x[0])

        for word, i in lexicographical:
            trans = sorted(self.values[i])
            print('{} - {}'.format(word,', '.join(trans)))

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
            eng, trans = line.split(' - ')
            trans = trans.split(', ')

            for word in trans:
                word = word.rstrip()
                latin[word] = eng

    print(len(latin))
    latin.print()
