from Trees.RegularTree.implementation import *

def DFS(root):
    print(root.key(), end="->")

    for child in root.getChildren():
        DFS(child)


def DFS1(root):
    for child in root.getChildren():
        DFS1(child)

    print(root.key(), end="->")

if __name__ == '__main__':
    tree = createSampleTree()
    DFS(tree)
    print()
    DFS1(tree)