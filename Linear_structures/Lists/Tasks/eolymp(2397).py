#https://www.e-olymp.com/uk/submissions/7501814

class Window():
    def __init__(self, x, y, w, h):
        self.prev = None
        self.rect = [[1] * w for _ in range(h)]
        self.properties = (x, y, x + w, y + h)

    def isVisible(self):
        for row in self.rect:
            for col in row:
                if col == 1:
                    return True

        return False

class Screen():
    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def addWindow(self, x, y, w, h):
        win = Window(x, y, w, h)
        win.prev = self.top
        self.top = win

    def intersection(self, win, cover):
        if win.isVisible:
            x1, y1, x2, y2 = cover.properties
            x3, y3, x4, y4 = win.properties
            x1, x2 = max(x1, x3), min(x2, x4)
            y1, y2 = max(y1, y3), min(y2, y4)
            a, b = x2 - x1, y2 - y1

            if a * b > 0:
                for i in range(y1 - y3, y2 - y3):
                    for j in range(x1 - x3, x2 - x3):
                        win.rect[i][j] = 0

    def countVisibleWindows(self):
        cover = self.top
        counter = 1

        while not cover.prev is None:
            win = cover.prev

            while not win is None:
                self.intersection(win, cover)
                win = win.prev

            cover = cover.prev

        win = self.top.prev

        while not win is None:
            if win.isVisible():
                counter += 1

            win = win.prev

        return counter

if __name__ == '__main__':
    n = int(input())
    screen = Screen()

    for i in range(n):
        screen.addWindow(*map(int, input().split()))

    print(screen.countVisibleWindows())



