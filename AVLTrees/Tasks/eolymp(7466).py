#https://www.e-olymp.com/uk/submissions/7587224

class Tree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.balanceFactor = 0
        self.isRoot = False

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def isLeftChild(self):
        return self.parent.leftChild is self if not self.isRoot else False

    def isRightChild(self):
        return self.parent.rightChild is self if not self.isRoot else False

    def setLeft(self, key):
        self.leftChild = Tree(key)
        self.leftChild.parent = self
        self.updateBalance(self.leftChild)

    def setRight(self, key):
        self.rightChild = Tree(key)
        self.rightChild.parent = self
        self.updateBalance(self.rightChild)

    def insert(self, key):
        node = self

        while True:
            if node.key > key:
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

    def isBalanced(self):
        queue = []
        queue.append(self)

        while len(queue) > 0:
            node = queue.pop(0)

            if node.balanceFactor > 1 or node.balanceFactor < -1:
                return False

            if node.hasLeft():
                queue.append(node.leftChild)
            if node.hasRight():
                queue.append(node.rightChild)

        return True

    @staticmethod
    def updateBalance(node):
        if not node.isRoot:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                Tree.updateBalance(node.parent)

if __name__ == '__main__':
    n = int(input())
    nodes = tuple(map(int, input().split()))
    tree = Tree(nodes[0])
    tree.isRoot = True
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    print(int(tree.isBalanced()))