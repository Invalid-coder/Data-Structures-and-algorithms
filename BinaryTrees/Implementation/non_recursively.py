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

    def __str__(self):
        return str(self.key)

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
            elif node.key < key:
                if node.hasRight():
                    node = node.rightChild
                else:
                    node.setRight(key)
                    break

    def search(self, key):
        node = self

        while not node is None:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.leftChild
            elif node.key < key:
                node = node.rightChild

        return None

    def search_max(self, root):
        while root.rightChild:
            root = root.rightChild

        return root

    def delete(self, key):
        node = self.search(key)

        if node is None:
            return None

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
            left_max = self.search_max(node.leftChild)

            left_max_key = left_max.key
            node.setNode(left_max_key)

            if left_max != node.leftChild:
                if left_max.parent.leftChild == left_max:
                    left_max.parent.leftChild = None
                else:
                    left_max.parent.rightChild = None
            else:
                node.setLeft(left_max.leftChild)

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
