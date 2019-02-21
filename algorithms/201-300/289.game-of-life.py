# 生命游戏
'''
生命游戏，每个格子的生死遵循以下原则：
1.如果一个细胞周围有3个细胞为生，则该细胞为生（即该细胞若原先为死，则转为生，若原先为生，则保持不变）。
2.如果一个细胞周围有2个细胞为生，则该细胞的生死状态保持不变。
3.其他情况下，该细胞为死（即该细胞若原先为生，则转为死，若原先为死，则保持不变）。
'''


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 人家的解法
    #     if not board:
    #         return []
    #     rows = len(board)
    #     cols = len(board[0])
    #     for i in range(0, rows):
    #         for j in range(0, cols):
    #             self.changeStatus(board, i, j, rows, cols)
    #     for i in range(0, rows):
    #         for j in range(0, cols):
    #             board[i][j] = board[i][j] % 2

    # def changeStatus(self, board, i, j, rows, cols):
    #     # 0->3 1->2
    #     live_neighbors = 0
    #     for x in range(i - 1, i + 2):
    #         for y in range(j - 1, j + 2):
    #             if x == i and y == j:
    #                 continue
    #             if x < 0 or x >= rows:
    #                 continue
    #             if y < 0 or y >= cols:
    #                 continue
    #             neighbor = board[x][y]
    #             if neighbor == 1 or neighbor == 2:
    #                 live_neighbors += 1
    #     if board[i][j] == 1:
    #         if live_neighbors < 2:
    #             board[i][j] = 2
    #         elif live_neighbors > 3:
    #             board[i][j] = 2
    #     else:
    #         if live_neighbors == 3:
    #             board[i][j] = 3

        # 人家的解法
        # 我们使用二维数组来表示面板。在边缘上填充0，原则上，面板是无限的。
        # 很有意义
#         for i in board:
#             i.insert(0, 0)
#             i.append(0)
#         board = [[0] * len(board[0])] + board + [[0] * len(board[0])]
#         m = len(board)
#         n = len(board[0])
#         t = []
#         for i in range(1, m - 1):
#             for j in range(1, n - 1):
#                 x = board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j - 1] + \
#                     board[i][j + 1] + board[i + 1][j - 1] + \
#                     board[i + 1][j] + board[i + 1][j + 1]
#                 if board[i][j] == 0:
#                     if x == 3:
#                         t.append((i, j, 1))
#                 elif board[i][j] == 1:
#                     if x < 2 or x > 3:
#                         t.append((i, j, 0))
#         for x in t:
#             board[x[0]][x[1]] = x[2]

#         board.pop(0)
#         board.pop(-1)

#         for i in board:
#             i.pop(0)
#             i.pop(-1)
#         return board


# print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))

        for i in board:
            i.insert(0, 0)
            i.append(0)
        board = [[0] * len(board[0])] + board + [[0] * len(board[0])]

        m = len(board)
        n = len(board[0])
        t = []

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                x = board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j - 1] + \
                    board[i][j + 1] + board[i + 1][j - 1] + \
                    board[i + 1][j] + board[i + 1][j + 1]
                if board[i][j] == 0:
                    if x == 3:
                        t.append((i, j, 1))
                elif board[i][j] == 1:
                    if x < 2 or x > 3:
                        t.append((i, j, 0))

        for x in t:
            board[x[0]][x[1]] = x[2]
        board.pop(0)
        board.pop(-1)
        for i in board:
            i.pop(0)
            i.pop(-1)
        return board


print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
