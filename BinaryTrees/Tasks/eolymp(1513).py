#https://www.e-olymp.com/uk/submissions/7572824

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def print(self):
        def _print(node):
            if node.hasLeft():
                _print(node.leftChild)
            if node.hasRight():
                _print(node.rightChild)

            print(node.key, end='')

        _print(self)

def createTree(n, s1, s2):
    index = 0

    def search(s, left, right, x):
        for i in range(left, right + 1):
            if s[i] == x:
                return i

    def _createTree(s1, s2, left, right):
        nonlocal index

        if left > right:
            return None

        node = BinaryTree(s1[index])
        index += 1

        if left == right:
            return node

        pivot = search(s2, left, right, node.key)
        node.leftChild = _createTree(s1, s2, left, pivot - 1)
        node.rightChild = _createTree(s1, s2, pivot + 1, right)

        return node

    return _createTree(s1, s2, 0, n - 1)

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, s1, s2 = input().split()
        tree = createTree(int(n), s1, s2)
        tree.print()
        print()
