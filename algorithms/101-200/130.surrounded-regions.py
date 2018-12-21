class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m = len(board)
        n = len(board[0])
        res = [k for i in range(m + n)
               for k in ((0, i), (m - 1, i), (i, 0), (i, n - 1))]

        while res:
            i, j = res.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                res.extend(((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))

        board[:] = [["XO"[c == "S"] for c in row] for row in board]
