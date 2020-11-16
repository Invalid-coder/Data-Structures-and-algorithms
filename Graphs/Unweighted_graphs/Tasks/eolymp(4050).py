#https://www.e-olymp.com/uk/submissions/7745578

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = list()

    def addEdge(self, source, destination):
        self[source].append(destination)
        self[destination].append(source)

    def bfs(self, start):
        current = start
        playerTurn = True
        visited = set()
        level = 1

        def isCorrect(graph, start, level, visited):
            nonlocal playerTurn

            queue = [start]
            levels = {start:level}

            while queue:
                current = queue.pop(0)
                visited.add(current)
                deadlock = True

                for neighbor in graph[current]:
                    if not neighbor in visited:
                        queue.append(neighbor)
                        levels[neighbor] = levels[current] + 1
                        deadlock = False

                if deadlock:
                    if levels[current] % 2 == 1:# appropriate way for second player
                        if playerTurn:
                            return False
                        else:
                            return True
                    else:
                        if playerTurn:
                            return True
                        else:
                            return False

        while True:
            visited.add(current)
            next_node = None

            for neighbor in self[current]:
                if not neighbor in visited:
                    if isCorrect(self, neighbor, level + 1, visited.copy()):
                        if not next_node:
                            next_node = neighbor
                        elif neighbor < next_node:
                            next_node = neighbor

            if next_node:
                if playerTurn:
                    playerTurn = False
                else:
                    playerTurn = True

                current = next_node
                level += 1
            else:
                break

        return playerTurn, current

    def __getitem__(self, item):
        return self.vertices[item]

if __name__ == '__main__':
    n, k = map(int, input().split())
    graph = Graph(n)

    for _ in range(n - 1):
        source, destination = map(int, input().split())
        graph.addEdge(source, destination)

    res = graph.bfs(k)

    if res[0]:
        print("First player loses")
    else:
        print("First player wins flying to airport {}".format(res[1]))
