#https://www.e-olymp.com/uk/submissions/7563612

import sys
sys.setrecursionlimit(1000000)

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def setLeft(self, item):
        self.leftChild = BinaryTree(item)

    def setRight(self, item):
        self.rightChild = BinaryTree(item)

    def insert(self, key):
        self._insert_helper(self, key)

    def get_height(self):
        def _height(node):
            left_height = _height(node.leftChild) if node.hasLeft() else 0
            right_height = _height(node.rightChild) if node.hasRight() else 0

            return max(left_height, right_height) + 1

        return _height(self)

    @staticmethod
    def _insert_helper(root, key):
        if root.key > key:
            if root.hasLeft():
                BinaryTree._insert_helper(root.leftChild, key)
            else:
                root.setLeft(key)
        elif root.key < key:
            if root.hasRight():
                BinaryTree._insert_helper(root.rightChild, key)
            else:
                root.setRight(key)

if __name__ == '__main__':
    nodes = list(map(int, input().split()))

    if nodes[0] == 0:
        print(0)
    else:
        tree = BinaryTree(nodes[0])
        i = 1

        while i < len(nodes) and nodes[i] != 0:
            tree.insert(nodes[i])
            i += 1

        print(tree.get_height())
