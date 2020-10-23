#https://www.e-olymp.com/uk/submissions/7568665

class BinnaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def hasLeft(self):
        return not self.leftChild is None

    def hasRight(self):
        return not self.rightChild is None

    def setLeft(self, key):
        self.leftChild = BinnaryTree(key)

    def setRight(self, key):
        self.rightChild = BinnaryTree(key)

    def insert(self, key):
        self._insert_helper(self, key)

    @staticmethod
    def _insert_helper(root, key):
        if ord(root.key) > ord(key):
            if root.hasLeft():
                BinnaryTree._insert_helper(root.leftChild, key)
            else:
                root.setLeft(key)
        elif ord(root.key) < ord(key):
            if root.hasRight():
                BinnaryTree._insert_helper(root.rightChild, key)
            else:
                root.setRight(key)

    def __str__(self):
        s = ""

        def _str(node):
            nonlocal s

            s += node.key

            if node.hasLeft():
                _str(node.leftChild)
            if node.hasRight():
                _str(node.rightChild)

        _str(self)

        return s

if __name__ == '__main__':
    with open("input.txt") as input:
        with open("output.txt", 'w') as output:
            queue = []

            for line in input.readlines():
                queue.insert(0, line.rstrip())

            if len(queue) > 0:
                tree = BinnaryTree(queue[1])
                i = 1

                while i < len(queue):
                    for x in queue[i]:
                        tree.insert(x)

                    i += 1

                print(tree, file=output)
            else:
                print('', file=output)