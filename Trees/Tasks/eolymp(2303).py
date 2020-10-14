#https://www.e-olymp.com/uk/submissions/7510869

class Tree:
    def __init__(self): self.children = {}
    def has_children(self): return bool(self.children)
    def add_child(self, digit): self.children[digit] = Tree()
    def has_child(self, digit): return bool(self.children.get(digit))
    def get_child(self, digit): return self.children[digit]
    def clear(self): self.children.clear()

def addPhoneNumber(phoneNumber, tree):
    i = 0
    node = tree

    while i < len(phoneNumber) and node.has_child(phoneNumber[i]):
        node = node.get_child(phoneNumber[i])
        i += 1

    if i == len(phoneNumber):
        return False

    if i != 0 and not node.has_children():
        return False

    while i < len(phoneNumber):
        node.add_child(phoneNumber[i])
        node = node.get_child(phoneNumber[i])
        i += 1

    return True

if __name__ == '__main__':
    t = int(input())
    tree = Tree()

    for i in range(t):
        n = int(input())
        competiable = True

        for j in range(n):
            phoneNumber = input()

            if competiable:
                competiable = addPhoneNumber(phoneNumber, tree)

        print("YES" if competiable else "NO")
        tree.clear()



