#https://www.e-olymp.com/uk/submissions/7528674

class Tree():
    def __init__(self): self.children = {}
    def hasChild(self, key): return bool(self.children.get(key))
    def hasChildren(self): return bool(self.children)
    def addChild(self, key): self.children[key] = Tree()
    def getChild(self, key): return self.children[key]
    def clear(self): self.children.clear()

    def addNumber(self, number):
        i = 0
        node = self

        while i < len(number) and node.hasChild(number[i]):
            node = node.getChild(number[i])
            i += 1

        if i == len(number):
            return False

        if i != 0 and not node.hasChildren():
            return False

        while i < len(number):
            node.addChild(number[i])
            node = node.getChild(number[i])
            i += 1

        return True



if __name__ == '__main__':
    t = int(input())
    tree = Tree()

    for i in range(t):
        n = int(input())
        compatiable = True

        for j in range(n):
            number = input()

            if compatiable:
                compatiable = tree.addNumber(number)

        print('YES' if compatiable else 'NO')
        tree.clear()