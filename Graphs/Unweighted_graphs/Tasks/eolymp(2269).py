#https://www.e-olymp.com/uk/submissions/7765128

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def get_components_count(self):
        remaining = set(range(len(self.adjacentMatrix)))
        connected_component = 0
        stack = []
        counter = 0

        while remaining:
            if stack:
                current = stack.pop()
            else:
                current = remaining.pop()
                counter += 1

            for neighbor, edge in enumerate(self[current]):
                if edge == 1:
                    if neighbor in remaining:
                        stack.append(neighbor)
                        remaining.remove(neighbor)

        return counter

    """
       #Second option by dfs

       def dfs(self, start, visited):
           visited.add(start)

           for neighbor, edge in enumerate(self[start]):
               if edge == 1:
                   if not neighbor in visited:
                       self.dfs(neighbor, visited)

       def get_components_count(self):
           connected_component = 0
           n = len(self.adjacentMatrix)
           visited = set()

           for v in range(n):
               if not v in visited:
                   connected_component += 1
                   self.dfs(v, visited)

           return connected_component
       """

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(graph.get_components_count())