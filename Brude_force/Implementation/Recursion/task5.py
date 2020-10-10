#https://www.e-olymp.com/uk/submissions/7324736

maxScore = 0

def findMaxScore(score, weight, curr):
    global maxScore

    if weight == W or curr >= n:
        if score > maxScore:
            maxScore = score

        return

    findMaxScore(score, weight, curr + 1)
    findMaxScore(score + c[curr], weight + 1, curr + 1)

if __name__ == '__main__':
    W, n = map(int, input().split())
    c = list(map(int, input().split()))
    findMaxScore(0, 0, 0)
    print(maxScore)
