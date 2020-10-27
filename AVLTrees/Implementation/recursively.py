from BinaryTrees.Implementation.recursively import *

class AVLTree(BinaryTree):
    def __init__(self, key):
        super().__init__(key)
        self.balanceFactor = 0
        self.isRoot = False

    def setLeft(self, item):
        if isinstance(item, AVLTree):
            self.leftChild = item
        elif self.hasLeft():
            self.leftChild.setNode(item)
        else:
            self.leftChild = AVLTree(item)

        self.leftChild.parent = self
        self.updateBalance(self.leftChild)

    def setRight(self, item):
        if isinstance(item, AVLTree):
            self.rightChild = item
        elif self.hasRight():
            self.rightChild.setNode(item)
        else:
            self.rightChild = AVLTree(item)

        self.rightChild.parent = self
        self.updateBalance(self.rightChild)

    @staticmethod
    def updateBalance(node):
        if node.balanceFactor < -1 or node.balanceFactor > 1:
            AVLTree.rebalance(node)
            return

        if not node.isRoot:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                AVLTree.updateBalance(node.parent)

    @staticmethod
    def rebalance(node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                AVLTree.rotateRight(node.rightChild)
                AVLTree.rotateLeft(node)
            else:
                AVLTree.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                AVLTree.rotateLeft(node.leftChild)
                AVLTree.rotateRight(node)
            else:
                AVLTree.rotateRight(node)

    @staticmethod
    def rotateLeft(node):
        node_parent = node.parent

        if node.isLeftChild():
            node_parent.leftChild = AVLTree.__rotateLeft(node)
        elif node.isRightChild():
            node_parent.rightChild = AVLTree.__rotateLeft(node)

    @staticmethod
    def rotateRight(node):
        node_parent = node.parent

        if node.isLeftChild():
            node_parent.leftChild = AVLTree.__rotateRight(node)
        elif node.isRightChild():
            node_parent.rightChild = AVLTree.__rotateRight(node)

    @staticmethod
    def __rotateLeft(root):
        pivot = root.rightChild
        root.rightChild = pivot.leftChild

        if pivot.leftChild:
            pivot.leftChild.parent = root

        pivot.leftChild = root

        node_parent = root.parent
        root.parent = pivot
        pivot.parent = node_parent

        root.balanceFactor = root.balanceFactor + 1 - min(pivot.balanceFactor, 0)
        pivot.balanceFactor = pivot.balanceFactor + 1 + max(root.balanceFactor, 0)

        return pivot

    @staticmethod
    def __rotateRight(root):
        pivot = root.leftChild
        root.leftChild = pivot.rightChild

        if pivot.rightChild:
            pivot.rightChild.parent = root

        pivot.rightChild = root

        node_parent = root.parent
        root.parent = pivot
        pivot.parent = node_parent

        root.balanceFactor = root.balanceFactor - 1 - max(pivot.balanceFactor, 0)
        pivot.balanceFactor = pivot.balanceFactor - 1 + min(root.balanceFactor, 0)

        return pivot
