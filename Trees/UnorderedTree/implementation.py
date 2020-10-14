class Node():
    def __init__(self, key):
        self.mKey = key

    def setKey(self, key):
        self.mKey = key

    def key(self):
        return self.mKey

    def __str__(self):
        return str(self.mKey)

class UnorderedTree():
    def __init__(self, key):
        super().__init__(key)
        self.mChildren = {}

    def addChild(self, child):
        self.mChildren[child.key()] = child

    def removeChild(self, key):
        if key in self.mChildren:
            del self.mChildren[key]
            return True
        else:
            return False

    def getChild(self, key):
        if key in self.mChildren:
            return self.mChildren[key]
        else:
            return None

    def getChildren(self, key):
        return self.mChildren.values()
    