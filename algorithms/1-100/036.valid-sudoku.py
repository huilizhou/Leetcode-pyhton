class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # # 我的想法，根据题意来直接判断
        # # 注意3*3小格子时，各子中的数字不与本身相同。但是这样的算法复杂度较大
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    # 判断行的重复性
                    for k in range(j + 1, 9):
                        if board[i][j] == board[i][k]:
                            return False
                    # 判断列的重复性
                    for h in range(i + 1, 9):
                        if board[i][j] == board[h][j]:
                            return False
                    # 判断格子里面的重复性：
                    for g in range(i // 3 * 3, i // 3 * 3 + 3):
                        for q in range(j // 3 * 3, j // 3 * 3 + 3):
                            if board[i][j] == board[g][q] and i != g and j != q:
                                return False
        return True

        # 人家的解法，没有必要使用dict，我们只关心某个数字有没有出现过
        # 只循环一次完成数据分类，用存储空间来换取算法的效率
        # Cell = [[] for i in range(9)]
        # Col = [[] for i in range(9)]
        # Row = [[] for i in range(9)]

        # for i, row in enumerate(board):
        #     for j, num in enumerate(row):
        #         if num != ".":
        #             k = (i // 3) * 3 + j // 3
        #             if num in Row[i] + Col[j] + Cell[k]:
        #                 return False
        #             Row[i].append(num)
        #             Col[j].append(num)
        #             Cell[k].append(num)
        # return True


print(Solution().isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
