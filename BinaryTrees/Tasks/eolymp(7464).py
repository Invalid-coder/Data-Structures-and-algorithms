#https://www.e-olymp.com/uk/submissions/7568926

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

    def minDepth(self):
        queue = []
        min_depth = int(1e9)
        queue.append((self, 1))

        while len(queue) > 0:
            node, depth = queue.pop(0)

            if node.hasNoChildren():
                if depth < min_depth:
                    min_depth = depth

            if node.hasLeft():
                queue.append((node.leftChild, depth + 1))
            if node.hasRight():
                queue.append((node.rightChild, depth + 1))

        return min_depth

if __name__ == '__main__':
    n = int(input())
    nodes = tuple(map(int, input().split()))
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    print(tree.minDepth())