#https://www.e-olymp.com/uk/submissions/7563844

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

    def second_max(self):
        node = self
        right_side = [node.key]

        while node.hasRight():
            node = node.rightChild
            right_side.append(node.key)

        right_side.pop()

        while True:
            if node.hasRight():
                node = node.rightChild
                right_side.append(node.key)
            elif node.hasLeft():
                node = node.leftChild
                right_side.append(node.key)
            else:
                break

        return max(right_side)

if __name__ == '__main__':
    nodes = list(map(int, input().split()))

    if nodes[0] == 0:
        print(0)
    else:
        tree = BinaryTree(nodes[0])
        i = 1

        while nodes[i] != 0:
            tree.insert(nodes[i])
            i += 1

        print(tree.second_max())