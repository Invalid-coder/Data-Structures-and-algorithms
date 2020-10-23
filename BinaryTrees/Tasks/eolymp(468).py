#https://www.e-olymp.com/uk/submissions/7568296

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    left = -2147483648
    right = 2147483647
    prev = arr[0]
    ans = True

    for x in arr[1:]:
        if x > right or x < left:
            ans = False

        if prev > x:
            right = prev
        else:
            left = prev

        prev = x

    print('YES' if ans else 'NO')

"""
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
            else:
                if node.hasRight():
                    node = node.rightChild
                else:
                    node.setRight(key)
                    break

    def wayExists(self, way):
        node = self
        i = 0

        while i < len(way):
            if node.key == way[i]:
                i += 1

                if node.hasLeft():
                    if node.leftChild.key == way[i]:
                        node = node.leftChild
                        continue
                if node.hasRight():
                    if node.rightChild.key == way[i]:
                        node = node.rightChild
            else:
                return False

        return True

if __name__ == '__main__':
    nodes = tuple(map(int, input().split()))
    tree = BinaryTree(nodes[0])
    i = 1

    while i < len(nodes):
        tree.insert(nodes[i])
        i += 1

    print("YES" if tree.wayExists(nodes) else "NO")
"""


