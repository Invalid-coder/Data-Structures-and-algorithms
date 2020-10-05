class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack():
    def __init__(self):
        self.top_node = None
        self.size = 0

    def empty(self):
        return self.top_node is None

    def push(self, item):
        node = Node(item)

        if not self.empty():
            node.next = self.top_node

        self.top_node = node
        self.size += 1

    def back(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to an empty container")
        else:
            return self.top_node.item

    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to an empty container")
        else:
            current_top = self.top_node
            item = current_top.item
            self.top_node = self.top_node.next
            del current_top
            return item