#https://www.e-olymp.com/uk/submissions/7563686

import sys
sys.setrecursionlimit(10000000)

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

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

    def size(self):
        def _size(node):
            left_size = _size(node.leftChild) if node.hasLeft() else 0
            right_size = _size(node.rightChild) if node.hasRight() else 0

            return left_size + right_size + 1

        return _size(self)

if __name__ == '__main__':
    nodes = list(map(int, input().split()))

    if nodes[0] == 0:
        print(0)
    else:
        tree = BinaryTree(nodes[0])
        i = 1

        while nodes[i] != 0:
            tree.insert(nodes[i])
            i += 1

        print(tree.size())
