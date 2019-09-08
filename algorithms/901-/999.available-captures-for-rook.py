# 车的可用捕获量
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        R_i = -1
        R_j = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    R_i = i
                    R_j = j
        up = R_j - 1
        down = R_j + 1
        left = R_i - 1
        right = R_i + 1
        count = 0
        while up >= 0:
            if board[R_i][up] == 'p':
                count += 1
                break
            elif board[R_i][up] == "B":
                break
            else:
                up -= 1

        while down < m:
            if board[R_i][down] == 'p':
                count += 1
                break
            elif board[R_i][down] == 'B':
                break
            else:
                down += 1

        while left >= 0:
            if board[left][R_j] == 'p':
                count += 1
                break
            elif board[left][R_j] == 'B':
                break
            else:
                left -= 1

        while right < n:
            if board[right][R_j] == 'p':
                count += 1
                break
            elif board[right][R_j] == 'B':
                break
            else:
                right += 1
        return count


board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

print(Solution().numRookCaptures(board))
