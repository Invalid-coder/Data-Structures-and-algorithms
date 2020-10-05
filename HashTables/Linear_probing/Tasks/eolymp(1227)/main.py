#https://www.e-olymp.com/uk/submissions/7278631

class HashTable():
    def __init__(self):
        self.max_size = 11
        self.current_size = 0
        self.keys = [None] * self.max_size

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
        keys = self.keys
        self.keys = [None] * self.max_size

        for key in keys:
            if not key is None:
                self.put(key)

    def put(self, key):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                return

            current = (current + 1) % self.max_size

        self.keys[current] = key
        self.current_size += 1

        if self.occupancy() >= 0.7:
            self.expandTable()

    def print(self):
        keys = [key for key in self.keys if not key is None]

        for key in sorted(keys):
            print(key)

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
    dictionary = HashTable()

    with open('input.txt') as inp:
        for line in inp:
            words = line.split()

            for word in words:
                word = word.lower().rstrip('"').strip('.,":;')
                add(word, dictionary)

    dictionary.print()