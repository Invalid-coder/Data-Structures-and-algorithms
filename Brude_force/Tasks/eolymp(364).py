#https://www.e-olymp.com/uk/submissions/7352002

searchedWord = ''
num = 0

def findWord(chunk):
    global searchedWord, num

    if len(chunk) == N:
        num += 1

        if num == k:
            searchedWord = chunk

        return

    for c in range(ord('a'), ord('a') + N):
        if not chr(c) in chunk:
            findWord(chunk + chr(c))

if __name__ == '__main__':
    N, k = map(int, input().split())
    findWord('')
    print(searchedWord)