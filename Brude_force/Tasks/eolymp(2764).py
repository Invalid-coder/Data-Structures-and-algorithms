ans = []

def isRight(figures):
    checked = []

    for col,row in enumerate(figures):
        for r,c in checked:
            if abs(row - r) == abs(col - c):
                return False

        checked.append((row,col))

    return True

def set_figures(settled, i):
    global ans

    if i == n:
        if isRight(settled):
            ans = settled

        return

    for j in range(1, n + 1):
        if j not in settled:
            next_list = settled[:]
            next_list.append(j)
            set_figures(next_list, i + 1)

if __name__ == '__main__':
    n = int(input())
    set_figures([],0)
    print(*ans)