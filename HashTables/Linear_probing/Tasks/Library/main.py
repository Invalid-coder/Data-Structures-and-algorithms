import time
import HashTables.Linear_probing.Tasks.Library.user as user
from random import randint

N_MAXKEY = 10000000
TIME_MULTIPLIER = 100000
TIME_TEST_LIMIT = 200

_array = {}
_deleted = set()


def generate_pairs(fname, N):
    f_out = open(fname, "w", encoding='utf-8')
    for i in range(N):
        key = randint(0, N_MAXKEY)
        chars = randint(2, 50)
        value = ""
        for j in range(chars):
            ch = randint(0, 25)
            value += chr(ord('a') + ch)
        word = str(key) + "=" + value
        print(word, file=f_out, end="\n")
    f_out.close()


def readData(fname):
    with open(fname, encoding='utf-8') as f_in:
        for line in f_in:
            pair = line.strip().split('=')
            key, value = int(pair[0]), pair[1]
            add(key, value)


def add(key, value):
    global _array, _deleted
    _array[key] = value
    user.set(key, value)
    if key in _deleted:
        _deleted.remove(key)


def delete():
    global _array, _deleted
    size = len(_array)

    num = randint(0, size - 1)
    key = list(_array)[num]

    del _array[key]
    _deleted.add(key)

    t = time.time()
    user.delete(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return dt < TIME_TEST_LIMIT


def checkFind():
    global _array, _deleted
    size = len(_array)
    num = randint(0, size - 1)
    key = list(_array)[num]

    val = _array[key]

    t = time.time()
    user_val = user.get(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return user_val == val and dt < TIME_TEST_LIMIT


def checkFindDeleted():
    global _array, _deleted

    size = len(_deleted)
    if size == 0:
        return True

    num = randint(0, size - 1)
    key = list(_deleted)[num]

    t = time.time()
    user_find = user.get(key)
    dt = (time.time() - t) * TIME_MULTIPLIER

    return user_find is None and dt < TIME_TEST_LIMIT


def main():
    global _array, _deleted

    _array = {}
    _deleted = set()

    user.init()

    # generate_pairs("input.txt", 100000)
    readData("input.txt")

    test_num = 10000
    error = 0

    for i in range(test_num):
        case = randint(0, 2)
        res = True
        if case == 0:
            res = delete()
        elif case == 1:
            res = checkFind()
        elif case == 2:
            res = checkFindDeleted()

        if not res:
            error += 1

    score = 100 * (test_num - error) / test_num
    print("Score: %d%%" % score)


if __name__ == "__main__":
    main()
