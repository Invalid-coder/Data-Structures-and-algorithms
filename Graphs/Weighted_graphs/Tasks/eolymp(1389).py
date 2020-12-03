import sys

INF = sys.maxsize

class Vertex:
    def __init__(self):
        self.mNeighbors = {}
        self.mDistance = INF

    def distance(self):
        return self.mDistance

    def setDistance(self, distance):
        self.mDistance = distance

    def addNeighbor(self, neighbor, weight):
        if not neighbor in self.mNeighbors:
            self.mNeighbors[neighbor] = [weight]
        else:
            self.mNeighbors[neighbor].append(weight)

    def weight(self, neighbor):
        return self.mNeighbors[neighbor]

    def neighbors(self):
        return self.mNeighbors.keys()

class Graph:
    def __init__(self, n):
        self.vertices = {}

        for i in range(1, n + 1):
            self.vertices[i] = Vertex()

    def addEdge(self, source, destination, weight):
        self[source].addNeighbor(destination, weight)

    def Dijkstra(self, start, end):
        fixed = [False] * len(self)
        self[start].setDistance(0)
        current = start

        while True:
            fixed[current - 1] = True

            if current == end:
                break

            vertex = self[current]
            curr_time = vertex.distance()

            for neighbor_key in vertex.neighbors():
                neighbor = self[neighbor_key]

                for weight in vertex.weight(neighbor_key):
                    move_time, arrive_time = weight

                    if move_time < curr_time:
                        continue

                    if arrive_time < neighbor.distance():
                        neighbor.setDistance(arrive_time)

            distance = INF

            for neighbor_key in vertex.neighbors():
                neighbor = self[neighbor_key]

                if not fixed[neighbor_key - 1] and neighbor.distance() < distance:
                    current = neighbor_key
                    distance = neighbor.distance()

            if distance == INF:
                break

        return self[end].distance()

    def __getitem__(self, item):
        return self.vertices[item]

    def __len__(self):
        return len(self.vertices)

if __name__ == '__main__':
    n = int(input())
    s, e = map(int, input().split())
    m = int(input())
    graph = Graph(n)

    if m != 0:
        for i in range(m):
            s, t1, d, t2 = map(int, input().split())
            graph.addEdge(s, d, (t1, t2))

        ans = graph.Dijkstra(s, e)

        if ans == INF:
            print(-1)
        else:
            print(ans)
    else:
        print(-1)