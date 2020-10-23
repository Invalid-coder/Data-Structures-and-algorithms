#https://www.e-olymp.com/uk/submissions/7568786

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

    def maxDepth(self):
        def _maxDepth(node):
            left_depth = _maxDepth(node.leftChild) if node.hasLeft() else 0
            right_depth = _maxDepth(node.rightChild) if node.hasRight() else 0

            return max(left_depth, right_depth) + 1

        return _maxDepth(self)

if __name__ == '__main__':
    n = int(input())
    nodes = tuple(map(int, input().split()))
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    print(tree.maxDepth())