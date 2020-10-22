#https://www.e-olymp.com/uk/submissions/7563886
import sys
sys.setrecursionlimit(100000000)

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def hasNoChildren(self):
        return self.leftChild is None and self.rightChild is None

    def setLeft(self, key):
        self.leftChild = BinaryTree(key)

    def setRight(self, key):
        self.rightChild = BinaryTree(key)

    def insert(self, key):
        node = self

        while True:
            if node.key == key:
                break
            elif node.key > key:
                if node.hasLeft():
                    node = node.leftChild
                else:
                    node.setLeft(key)
                    break
            else:
                if node.hasRight():
                    node = node.rightChild
                else:
                    node.setRight(key)
                    break

    def find_leafs(self):
        leafs = []
        queue = []
        queue.append(self)

        while len(queue) > 0:
            node = queue.pop(0)

            if node.hasNoChildren():
                leafs.append(node.key)
            else:
                if node.hasLeft():
                    queue.append(node.leftChild)
                if node.hasRight():
                    queue.append(node.rightChild)

        return leafs

    def findLeafs(self):
        leafs = []

        def _leafs(node):
            if node.hasLeft():
                _leafs(node.leftChild)
            if node.hasRight():
                _leafs(node.rightChild)
            if node.hasNoChildren():
                leafs.append(node.key)

        _leafs(self)

        return leafs

if __name__ == '__main__':
    nodes = list(map(int, input().split()))

    if nodes[0] == 0:
        pass
    else:
        tree = BinaryTree(nodes[0])
        i = 1

        while nodes[i] != 0:
            tree.insert(nodes[i])
            i += 1

        print(*sorted(tree.findLeafs()))