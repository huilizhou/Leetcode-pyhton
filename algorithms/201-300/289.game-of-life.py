class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        rows = len(board)
        cols = len(board[0])
        for i in range(0, rows):
            for j in range(0, cols):
                self.changeStatus(board, i, j, rows, cols)
        for i in range(0, rows):
            for j in range(0, cols):
                board[i][j] = board[i][j] % 2

    def changeStatus(self, board, i, j, rows, cols):
        # 0->3 1->2
        live_neighbors = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x == i and y == j:
                    continue
                if x < 0 or x >= rows:
                    continue
                if y < 0 or y >= cols:
                    continue
                neighbor = board[x][y]
                if neighbor == 1 or neighbor == 2:
                    live_neighbors += 1
        if board[i][j] == 1:
            if live_neighbors < 2:
                board[i][j] = 2
            elif live_neighbors > 3:
                board[i][j] = 2
        else:
            if live_neighbors == 3:
                board[i][j] = 3
