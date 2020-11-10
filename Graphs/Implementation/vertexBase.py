class VertexBase:
    def __init__(self, key):
        self.mKey = key
        self.mData = None

    def key(self):
        return self.mKey

    def setData(self, data):
        self.data = data

    def data(self):
        return self.mData

