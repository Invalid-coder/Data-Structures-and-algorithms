#https://www.e-olymp.com/uk/submissions/7288661

def hasWord(words, part):
    for word in words:
        i = 0
        j = 0
        chunk = ''

        while i < len(word) and j < len(part):
            if part[j] == word[i]:
                chunk += part[j]
                i += 1

            j += 1

        if chunk == word:
            return True

    return False

def check(words, text):
    chunk = ''

    for i, c in enumerate(text):
        chunk += c

        if hasWord(words, chunk):
            print("{} {}".format('YES', i + 1))

            return

    print('NO')

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    T = input()

    check(words, T)

