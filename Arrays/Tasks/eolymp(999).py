"""
On an 8 x 8 chessboard, there is exactly one white rook 'R'
and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
When the rook moves, it chooses one of four cardinal directions (north, east, south, or west),
then moves in that direction until it chooses to stop, reaches the edge
of the board, captures a black pawn, or is blocked by a white bishop.
 A rook is considered attacking a pawn if the rook can capture the pawn
 on the rook's turn. The number of available captures for the white rook is
 the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
"""


class Solution:
    def numRookCaptures(self, board):
        pos = None
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    pos = (i, j)
                    break
        for i in range(pos[0] - 1, -1, -1):
            if board[i][pos[1]] == "B":
                break
            if board[i][pos[1]] == "p":
                count += 1
                break
        for i in range(pos[0] + 1, len(board)):
            if board[i][pos[1]] == "B":
                break
            if board[i][pos[1]] == "p":
                count += 1
                break
        for j in range(pos[1] - 1, -1, -1):
            if board[pos[0]][j] == "B":
                break
            if board[pos[0]][j] == "p":
                count += 1
                break
        for j in range(pos[1] + 1, len(board[0])):
            if board[pos[0]][j] == "B":
                break
            if board[pos[0]][j] == "p":
                count += 1
                break
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))