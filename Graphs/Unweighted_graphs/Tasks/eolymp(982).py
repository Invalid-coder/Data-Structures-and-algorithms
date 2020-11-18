#https://www.e-olymp.com/uk/submissions/7764797

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def isConnected(self):
        remaining = set(self.vertices.keys())
        stack = [remaining.pop()]

        while stack:
            current = stack.pop()
            for neighbour in self.vertices[current]:
                if neighbour in remaining:
                    stack.append(neighbour)
                    remaining.remove(neighbour)

        return not remaining

    """
    #Second option by dfs(this one is slower than implementation by bfs)
    
        def dfs(self, start, visited):
        visited.add(start)

        for neighbor in self[start]:
            if not neighbor in visited:
                self.dfs(neighbor, visited)

    def isConnected(self):
        visited = set()
        self.dfs(1, visited)
        n = len(self.vertices)

        for v in range(1, n + 1):
            if not v in visited:
                return False

        return True
    
    """
    
    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.addEdge(u, v)

    print("YES" if graph.isConnected() else "NO")