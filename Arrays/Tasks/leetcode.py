inf = -(10**7)
class Node():
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord

class Trie:
    def __init__(self):
        self.trie = None


    def build(self, words):
        self.trie = Node({}, False)
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node({}, False)
                current = current.children[char]
            current.isWord = True


    def autocomplete(self, prefix):
        current = self.trie
        for char in prefix:
            if not char in current.children:
                return []
            current = current.children[char]
        return self.findWordsFromNode(current, prefix)


    def findWordsFromNode(self, node, prefix):
        words = []
        if node.isWord:
            words.append(prefix)
        for char in node.children:
            words += self.findWordsFromNode(node.children[char], prefix + char)
        return words


def findKthLargest(array, k=3):
    max1, max2, max3 = inf, inf, inf
    for x in array:
        if x > max1:
            max3 = max2
            max2 = max1
            max1 = x
        elif x < max1 and x > max2:
            max3 = max2
            max2 = x
        elif x < max2 and x > max3:
            max3 = x

    return max3

class Solution:
    def findKthLargest(self, arr, k):
        left = 0
        right = len(arr) - 1
        while left <= right:
            pivotIndex = self._partition(arr, left, right)
            if pivotIndex == len(arr) - k:
                return arr[pivotIndex]
            elif pivotIndex > len(arr) - k:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
        return - 1

    def _partition(self, arr, low, high):
        pivot = arr[high]
        index = low
        print(pivot, low, high)
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[index], arr[j] = arr[j], arr[index]
                index += 1
        arr[index], arr[high] = arr[high], arr[index]
        print(arr, index)
        return index

class Solution1:
    def findAlConcatenatedWords(self, words):
        wordDict = set(words)
        cache = {}
        return [word for word in words if self._canForm(word, wordDict, cache)]

    def _canForm(self, word, wordDict, cache):
        if word in cache:
            return cache[word]

        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]

            if prefix in wordDict:
                if suffix in wordDict or self._canForm(suffix, wordDict, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False

if __name__ == '__main__':
    s = Solution1()
    print(s.findAlConcatenatedWords(['cat', 'cats', 'dog', 'catsdog']))
    #print(findKthLargest([5, 7, 2, 3, 4, 1, 6, 10, 9]))
    s = Solution()
    print(s.findKthLargest([5, 6, 2, 3, 4, 1, 7], 3))
    t = Trie()
    words = ['dog', 'dark', 'cat', 'dooc', 'dodge']
    t.build(words)
    print(t.autocomplete('do'))
