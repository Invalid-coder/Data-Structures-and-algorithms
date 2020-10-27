class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def hasNoChildren(self):
        return self.leftChild is None and self.rightChild is None

    def setNode(self, item):
        if isinstance(item, BinaryTree):
            self.key = item.key
            self.leftChild = item.leftChild
            self.rightChild = item.rightChild
        else:
            self.key = item

    def setLeft(self, item):
        if isinstance(item, BinaryTree):
            self.leftChild = item
        elif self.hasLeft():
            self.leftChild.setNode(item)
        else:
            self.leftChild = BinaryTree(item)

        self.leftChild.parent = self

    def setRight(self, item):
        if isinstance(item, BinaryTree):
            self.rightChild = item
        elif self.hasRight():
            self.rightChild.setNode(item)
        else:
            self.rightChild = BinaryTree(item)

        self.rightChild.parent = self

    def removeLeftChild(self):
        self.leftChild = None

    def removeRightChild(self):
        self.rightChild = None

    def isLeftChild(self):
        return self.parent.leftChild is self if not self.parent is None else False

    def isRightChild(self):
        return self.parent.rightChild is self if not self.parent is None else False

    def insert(self, key):
        self._insert_helper(self, key)

    def search(self, key):
        return self._search_helper(self, key)

    def delete(self, key):
        self._delete_helper(self, key)

    def __str__(self):
        return str(self.key)

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

    @staticmethod
    def _search_helper(root, key):
        if root.key == key:
            return root
        elif root.key > key:
            return BinaryTree._search_helper(root.leftChild, key) if root.hasLeft() else None
        else:
            return BinaryTree._search_helper(root.rightChild, key) if root.hasRight() else None

    @staticmethod
    def _search_max(root):
        return BinaryTree._search_max(root.rightChild) if root.hasRight else root

    @staticmethod
    def _delete_helper(root, key):
        node = BinaryTree._search_helper(root, key)

        if node is None:
            return

        if node.hasNoChildren():
            if node.parent is None:
                node.key = None
            else:
                if node.parent.leftChild == node:
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
        elif node.hasLeft() and not node.hasRight():
            node.setNode(node.leftChild)
        elif node.hasRight() and not node.hasLeft():
            node.setNode(node.rightChild)
        else:
            left_max = BinaryTree._search_max(node.leftChild)
            left_max_key = left_max.key
            node.setNode(left_max_key)

            BinaryTree._delete_helper(node.leftChild, left_max_key)

def DFS(root):
    print(root.key, end=' ')

    if root.hasLeft():
        DFS(root.leftChild)

    if root.hasRight():
        DFS(root.rightChild)

def BFS(root):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        print(node.key, end=' ')

        if node.hasLeft():
            queue.append(node.leftChild)
        if node.hasRight():
            queue.append(node.rightChild)

def createSampleTree():
    node8 = BinaryTree(8)
    node8.setLeft(14)
    node8.setRight(15)

    node4 = BinaryTree(4)
    node4.setLeft(node8)
    node4.setRight(9)

    node7 = BinaryTree(7)
    node7.setLeft(10)
    node7.setRight(11)

    root = BinaryTree(1)
    root.setLeft(node4)
    root.setRight(node7)

    return root

if __name__ == '__main__':
    tree = createSampleTree()
    tree.insert(12)
    node12 = tree.search(12)
    print(node12.parent)
    print(node12.isLeftChild())
    print(node12.isRightChild())
    tree.delete(12)
    node12 = tree.search(12)
    print(node12)


