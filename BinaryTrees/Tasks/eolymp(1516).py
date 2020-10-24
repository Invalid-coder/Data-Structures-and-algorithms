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

    def height(self):
        def _height(node):
            leftHeight = _height(node.leftChild) if node.hasLeft() else 0
            rightHeight = _height(node.rightChild) if node.hasRight() else 0

            return max(leftHeight, rightHeight) + 1

        return _height(self)

def createTree(nodes):
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    return tree

def findOrder(n, h):
    orders = []

    def _findOrder(order):
        nonlocal orders

        if len(order) == n:
            tree = createTree(order)

            if tree.height() <= h:
                orders.append(order)

            return

        for i in range(1, n + 1):
            if not i in order:
                next_order = order[:]
                next_order.append(i)
                _findOrder(next_order)

    _findOrder([])

    if orders:
        minOrder = orders[0]

        for i in range(1, len(orders)):
            for j in range(len(orders[i])):
                if minOrder[j] < orders[i][j]:
                    break
                elif minOrder[j] > orders[i][j]:
                    minOrder = orders[i]
                    break

        return minOrder
    else:
        return None

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            lines = input.readlines()

            for i in range(len(lines) - 1):
                n, h = map(int, lines[i].rstrip().split())
                order = findOrder(n, h)

                print("Case {}: {}".format(i + 1, " ".join(map(str, order)) if not order is None else "Impossible."), file=output)

