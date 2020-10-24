#https://www.e-olymp.com/uk/submissions/7568767

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

    def isSameTree(self, tree):
        ans = True

        def _isSameTree(node1, node2):
            nonlocal ans

            if node1.key == node2.key:
                if node1.hasLeft() and node2.hasLeft():
                    _isSameTree(node1.leftChild, node2.leftChild)
                else:
                    if node1.hasLeft() and not node2.hasLeft():
                        ans = False
                    elif node2.hasLeft() and not node1.hasLeft():
                        ans = False

                if node1.hasRight() and node2.hasRight():
                    _isSameTree(node1.rightChild, node2.rightChild)
                else:
                    if node1.hasRight() and not node2.hasRight():
                        ans = False
                    elif node2.hasRight() and not node1.hasRight():
                        ans = False
            else:
                ans = False

        _isSameTree(self, tree)

        return int(ans)

if __name__ == '__main__':
    n = int(input())
    nodes1 = tuple(map(int, input().split()))
    m = int(input())
    nodes2 = tuple(map(int, input().split()))
    tree1 = BinaryTree(nodes1[0])
    tree2 = BinaryTree(nodes2[0])
    i, j = 1, 1

    while i < n:
        tree1.insert(nodes1[i])
        i += 1

    while j < n:
        tree2.insert(nodes2[j])
        j += 1

    print(tree1.isSameTree(tree2))