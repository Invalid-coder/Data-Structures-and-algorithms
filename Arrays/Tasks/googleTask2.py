class Solution:
    def findMaxNumberOfOrders(self, A, B, C, D):
        orders = 0
        while A and B and A + B + C + D >= 4:
            A -= 1
            B -= 1
            elements = 2
            if C > 0:
                C -= 1
                elements += 1
            if D > 0:
                D -= 1
                elements += 1
            while elements < 4:
                if A > B:
                    A -= 1
                elif B > A:
                    B -= 1
                elif A != 0:
                    A -= 1
                elements += 1
            if elements == 4:
                orders += 1
        return orders

if __name__ == '__main__':
    t = int(input())
    s = Solution()

    for _ in range(t):
        A,B,C,D = map(int, input().split())
        print(s.findMaxNumberOfOrders(A,B,C,D))