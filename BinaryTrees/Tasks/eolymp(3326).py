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

    def isSameTree(self, tree):
        ans = True

        def _isSameTree(node1, node2):
            nonlocal ans

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

        _isSameTree(self, tree)

        return ans

def createTree(nodes):
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    return tree

def findSequences(tree, n, m):
    sequences = []

    def _findSequences(sequence):
        if len(sequence) == n:
            tree1 = createTree(sequence)

            if tree.isSameTree(tree1):
                if not sequence in sequences:
                    sequences.append(sequence)

            return

        for i in range(1, m + 1):
            if not i in sequence:
                next_seq = sequence[:]
                next_seq.append(i)
                _findSequences(next_seq)

    _findSequences([])

    return len(sequences)

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        nodes = tuple(map(int, input().split()))
        tree = BinaryTree(nodes[0])
        i = 1

        while i < len(nodes):
            tree.insert(nodes[i])
            i += 1

        print(findSequences(tree, n, m))

