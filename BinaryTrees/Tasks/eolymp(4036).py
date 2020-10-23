#https://www.e-olymp.com/uk/submissions/7569068

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
        self._insert_helper(self, key)

    @staticmethod
    def _insert_helper(root, key):
        if root.key > key:
            if root.hasLeft():
                BinaryTree._insert_helper(root.leftChild, key)
            else:
                root.setLeft(key)
        elif root.key <= key:
            if root.hasRight():
                BinaryTree._insert_helper(root.rightChild, key)
            else:
                root.setRight(key)

    def PreOrder(self):
        def _PreOrder(node):
            print(node.key, end=' ')

            if node.hasLeft():
                _PreOrder(node.leftChild)
            if node.hasRight():
                _PreOrder(node.rightChild)

        _PreOrder(self)

if __name__ == '__main__':
    n = int(input())
    nodes = tuple(map(int, input().split()))
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    tree.PreOrder()