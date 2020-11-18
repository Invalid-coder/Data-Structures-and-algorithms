#https://www.e-olymp.com/uk/submissions/7764528

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def dfs(self, start, visited):
        visited.add(start)

        for neighbor, edge in enumerate(self[start]):
            if edge == 1:
                if not neighbor in visited:
                    self.dfs(neighbor, visited)

    def sizeOfConnectedComponent(self, start):
        visited = set()
        self.dfs(start, visited)

        return len(visited)

    """
    #Second option by bfs
    
    def getVerticesCount(self, vertex):
        visited = {vertex}
        stack = [vertex]   
        count = 0              
        
        while stack:
            current = stack.pop() 
            count += 1            
            for neighbour, edge in enumerate(self.matrix[current]):
                if edge:
                    if neighbour not in visited: 
                        stack.append(neighbour)  
                        visited.add(neighbour)   
        return count
    """

    def __getitem__(self, item):
        return self.adjacentMatrix[item]

if __name__ == '__main__':
    n, s = map(int, input().split())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    print(graph.sizeOfConnectedComponent(s - 1))