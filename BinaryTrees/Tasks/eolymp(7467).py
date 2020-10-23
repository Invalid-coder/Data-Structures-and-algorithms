#https://www.e-olymp.com/uk/submissions/7569026

class BinaryTree:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def hasNoChildren(self):
        return self.leftChild is None and self.rightChild is None

    def setLeft(self, key, val):
        self.leftChild = BinaryTree(key, val)

    def setRight(self, key, val):
        self.rightChild = BinaryTree(key, val)

    def insert(self, key, val):
        self._insert_helper(self, key, val)

    @staticmethod
    def _insert_helper(root, key, val):
        if root.key > key:
            if root.hasLeft():
                BinaryTree._insert_helper(root.leftChild, key, val)
            else:
                root.setLeft(key, val)
        elif root.key <= key:
            if root.hasRight():
                BinaryTree._insert_helper(root.rightChild, key, val)
            else:
                root.setRight(key, val)

    def isSymmetric(self):
        ans = True

        def _isSymmetric(node1, node2):
            nonlocal ans

            if node1.val != node2.val:
                ans = False
            else:
                if node1.hasLeft() and node2.hasRight():
                    _isSymmetric(node1.leftChild, node2.rightChild)
                else:
                    if node1.hasLeft() and not node2.hasLRight():
                        ans = False
                    elif node2.hasRight() and not node1.hasLeft():
                        ans = False

                    return
                if node1.hasRight() and node2.hasLeft():
                    _isSymmetric(node1.rightChild, node2.leftChild)
                else:
                    if node1.hasRight() and not node2.hasLeft():
                        ans = False
                    elif node2.hasLeft() and not node1.hasRight():
                        ans = False

        if self.hasLeft() and self.rightChild:
            _isSymmetric(self.leftChild, self.rightChild)
        else:
            ans = False

        return int(ans)

if __name__ == '__main__':
    n = int(input())
    keys = tuple(map(int, input().split()))
    values = tuple(map(int, input().split()))

    if n > 1:
        tree = BinaryTree(keys[0], values[0])
        i = 1

        while i < n:
            tree.insert(keys[i], values[i])
            i += 1

        print(tree.isSymmetric())
    else:
        print(1)