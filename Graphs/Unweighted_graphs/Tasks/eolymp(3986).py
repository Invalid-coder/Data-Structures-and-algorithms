#https://www.e-olymp.com/uk/submissions/7687866

class Graph:
    def __init__(self, matrix):
        self.adjacentMatrix = matrix

    def getOutFlows(self):
        n = len(self.adjacentMatrix)
        outflows = []

        for i in range(n):
            isOutFlow = True

            for j in range(i - 1, -1, -1):
                if self.adjacentMatrix[j][i] == 1:
                    isOutFlow = False
                    break

            if isOutFlow:
                for j in range(i + 1, n):
                    if self.adjacentMatrix[j][i] == 1:
                        isOutFlow = False
                        break

            if isOutFlow:
                outflows.append(i + 1)

        return outflows

    def getInFlows(self):
        inflows = []
        n = len(self.adjacentMatrix)

        for i in range(n):
            neighbors = 0

            for j in range(n):
                if self.adjacentMatrix[i][j] == 1:
                    neighbors += 1

            if neighbors == 0:
                inflows.append(i + 1)

        return inflows

if __name__ == '__main__':
    n = int(input())
    matrix = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    graph = Graph(matrix)
    outflows = graph.getOutFlows()
    inflows = graph.getInFlows()

    print(len(outflows), end=' ')
    print(*outflows)
    print(len(inflows), end=' ')
    print(*inflows)