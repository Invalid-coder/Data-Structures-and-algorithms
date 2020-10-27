#   Problems to solve
#1.ЕСЛИ БЫЛА КОЛЛИЗИЯ И ТЫ УДАЛЯЕШЬ ПЕРВЫЙ ПО ДОБАВЛЕНИЮ ЕЛЕМЕНТ, ТО ОСТАЛЬНЫЕ НЕЛЬЗЯ ДОСТАТЬ
#   (ТАК КАК ПРИ УДАЛЕНИИ МЫ ПО ХЕШУ ПОСТАВИЛИ None И МЕТОД get постоянно возвращает None)
#   Одно из решений - при удалении искать ключи, которые вызывали коллизию





class HashTable:
    """
        HashTable with linear probing collisions resolving method
    """

    def __init__(self):
        self.max_size = 11     #prime in most cases
        self.current_size = 0
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size

    def hash(self, key):
        if isinstance(key, int):
            return key % self.max_size
        elif isinstance(key, str):
            h = 0
            N = 31

            for i in range(len(key)):
                h = h * N + ord(key[i])

            return h % self.max_size

    def occupancy(self):
        return self.current_size / self.max_size

    def expandTable(self):
        self.max_size *= 2
        self.current_size = 0
        keys,values = self.keys, self.values
        self.keys = [None] * self.max_size
        self.values = [None] * self.max_size

        for key, value in zip(keys, values):
            if not key is None:
                self[key] = value


    def put(self, key, value):
        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                self.values[current] = value
                return

            current = (current + 1) % self.max_size


        self.keys[current] = key
        self.values[current] = value
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

    def delete(self, key):
        if not key in self:
            return

        current = self.hash(key)

        while not self.keys[current] is None:
            if self.keys[current] == key:
                self.keys[current] = None
                self.values[current] = None
                self.current_size -= 1


            current = (current + 1) % self.max_size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return not self.get(key) is None

    def __len__(self):
        return self.current_size

    def __str__(self):
        s = ''

        for i in range(self.max_size):
            if not self.keys[i] is None:
                key, value = self.keys[i], self.values[i]
                s += '{}:{} '.format(key, value)

        return s

if __name__ == '__main__':
    table = HashTable()
    table.put(55, 'zz')
    table.put(66, 'AA')
    table.put(66, 66)
    table.put(77, '77')
    table.put('Car', 'Lexus')

    table[56] = 'RR'
    table[55] = '55'
    table['Car'] = 'Lamborghini'

    #print(table.pop(55)) # check problem from above
    print(table[55])
    print(table[66])
    print(table['Car'])
    print(77 in table)
    print(table)