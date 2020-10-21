#https://www.e-olymp.com/uk/submissions/7529346

class Tree():
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = {}

    def getChildren(self):
        return self.children.values()

    def addChild(self, key):
        self.children[key] = Tree(key, self)

    def DFS(self, node, key, depth):
        if node.key == key:
            return node, depth

        for child in node.getChildren():
            res = self.DFS(child, key, depth + 1)

            if res:
                return res

    def add(self, a, b):
        a, h = self.DFS(self, a, 0)
        a.addChild(b)

    def get(self, a, b):
        a, h1 = self.DFS(self, a, 0)
        b, h2 = self.DFS(self, b, 0)

        while h1 != h2:
            if h1 > h2:
                a = a.parent
                h1 -= 1
            else:
                b = b.parent
                h2 -= 1

        while a != b:
            a = a.parent
            b = b.parent

        return a.key

    def execute(self, data):
        data = data.split()
        name = data[0]
        args = data[1:]

        return getattr(self, name.lower())(*args)

if __name__ == '__main__':
    k = int(input())
    tree = Tree('1')

    for i in range(k):
        data = input()
        res = tree.execute(data)

        if res:
            print(res)