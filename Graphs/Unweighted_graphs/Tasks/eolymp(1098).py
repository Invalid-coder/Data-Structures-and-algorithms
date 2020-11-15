#https://www.e-olymp.com/uk/submissions/7731475

ROWS = 8
COLS = 8

class Graph():
    def __init__(self, array):
        self.positions = array
        self.newPositions = [-1] * 8

    def getMinSteps(self):
        minSteps = 9

        def isBeating(graph, col):
            for i in range(COLS):
                if graph.newPositions[i] < 0:
                    break

                if i == col:
                    continue

                if graph.newPositions[col] == graph.newPositions[i]:# horizontal check
                    return True
                if col + graph.newPositions[col] == i + graph.newPositions[i]: # descending diagonal check
                    return True
                if col - graph.newPositions[col] == i - graph.newPositions[i]: # ascending diagonal check
                    return True

            return False

        def findPosition(graph, col):
            nonlocal minSteps

            if col > COLS - 1:
                return

            for i in range(1, ROWS + 1):
                graph.newPositions[col] = i

                if not isBeating(graph, col):
                    if col == COLS - 1:
                        currSteps = 0

                        for j in range(COLS):
                            if graph.positions[j] != graph.newPositions[j]:
                                currSteps += 1

                        minSteps = min(minSteps, currSteps)
                    else:
                        findPosition(graph, col + 1)

                graph.newPositions[col] = -1

        findPosition(self, 0)

        return minSteps

if __name__ == '__main__':
    array = list(map(int, input().split()))
    T = array[0]

    for t in range(T):
        graph = Graph(array[t * 8 + 1:t * 8 + 9])
        print(graph.getMinSteps(), end='')