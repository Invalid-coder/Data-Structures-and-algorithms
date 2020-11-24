def hasLeft(i, heap):
    return heap[i][0] != -1

def leftChild(i, heap):
    return heap[i][0]

def hasRight(i, heap):
    return heap[i][1] != -1

def rightChild(i, heap):
    return heap[i][1]

def hasTwoChildren(i, heap):
    return hasLeft(i, heap) and hasRight(i, heap)

def hasNoChildren(i, heap):
    return not hasLeft(i, heap) and not hasRight(i, heap)

def hasParent(i):
    return i // 2 > 1

def parent(i):
    return i // 2

def getPotential(i, heap):
    if hasNoChildren(i, heap) or i == -1:
        return 0

    minDistance = int(1e9)
    queue = []
    visited = {i:True}

    if hasLeft(i, heap):
        queue.append((leftChild(i, heap), 1))
    if hasRight(i, heap):
        queue.append((rightChild(i, heap), 1))
    if hasParent(i):
        queue.append((parent(i), 1))

    while len(queue) > 0:
        j, d = queue.pop(0)
        visited[j] = True

        if not hasTwoChildren(j, heap):
            if minDistance > d:
                minDistance = d

        if hasLeft(j, heap) and not leftChild(i, heap) in visited:
            queue.append((leftChild(i, heap), d + 1))
        if hasRight(j, heap) and not rightChild(i, heap) in visited:
            queue.append((rightChild(i, heap), d + 1))
        if hasParent(i) and not parent(i) in visited:
            queue.append((parent(i), d + 1))

    return minDistance

def isLeftHeap(heap):
    size = len(heap)

    for i in range(1, size):
        if hasRight(i, heap) and not hasLeft(i, heap):
            return i

        #left = leftChild(i, heap)
        #right = rightChild(i, heap)
        #leftP = getPotential(left, heap)
        #rightP = getPotential(right, heap)

        #if leftP < rightP:
            #return i

    return None

if __name__ == '__main__':
    n = int(input())
    heap = [None]

    for _ in range(n):
        l, r = map(int, input().split())
        heap.append((l, r))

    i = isLeftHeap(heap)

    if not i is None:
        print(i)
    else:
        print(-1)