#https://www.e-olymp.com/uk/submissions/7718179

def increase_first_digit(number):
    first_digit = number // 1000
    first_digit += 1
    return first_digit * 1000 + number % 1000

def decrease_last_digit(number):
    last_digit = number % 10
    last_digit -= 1
    return (number // 10) * 10 + last_digit

def right_cyclic_shift(number):
    last_digit = number % 10
    return last_digit * 1000 + number // 10

def left_cyclic_shift(number):
    first_digit = number // 1000
    return (number % 1000) * 10 + first_digit

class Graph:
    def __init__(self, start, end):
        self.vertices = {}
        self.vertices[start] = list()
        self.vertices[end] = list()
        self.init_graph(start, end)

    def addEdge(self, source, destination):
        self[source].append(destination)

        if not destination in self:
            self[destination] = list()

    def init_graph(self, start, end):
        queue = [start]

        while queue:
            current = queue.pop(0)

            if current == end:
                break

            neighbors = [right_cyclic_shift(current), left_cyclic_shift(current)]

            if current // 1000 != 9:
                neighbors.append(increase_first_digit(current))
            if current % 10 != 1:
                neighbors.append(decrease_last_digit(current))

            for neighbor in neighbors:
                if not neighbor in self[current]:
                    self.addEdge(current, neighbor)
                    queue.append(neighbor)

    def way_search(self, start, end):
        sources = {start:None}
        queue = [start]

        while queue:
            current = queue.pop(0)

            for neighbor in self[current]:
                if not neighbor in sources:
                    sources[neighbor] = current
                    queue.append(neighbor)

        stack = []
        current = end

        while not current is None:
            stack.append(current)
            current = sources[current]

        way = []

        while stack:
            way.append(stack.pop())

        return way

    def __contains__(self, vertex):
        return vertex in self.vertices

    def __getitem__(self, vertex):
        return self.vertices[vertex]

    def __setitem__(self, vertex, value):
        self.vertices[vertex] = value

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    graph = Graph(a, b)
    way = graph.way_search(a, b)

    for v in way:
        print(v)

